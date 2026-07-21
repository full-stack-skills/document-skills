#!/usr/bin/env python3
"""Run deterministic repository-level quality checks for document skills."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
ALLOWED_FRONTMATTER = {"name", "description"}
LOCAL_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
_PRIVATE_BRAND = "Part" + "Me"
_PRIVATE_PRODUCT_PREFIX = "Oc" + "to"
_PRIVATE_DOCS = "part" + "me-docs"
_PRIVATE_WORKSPACE = "workspace-part" + "me-ai"
_MAC_HOME_PREFIX = "/" + "Users/"
FORBIDDEN_CONTENT_RE = re.compile(
    rf"(?i:{_PRIVATE_BRAND}|{_PRIVATE_PRODUCT_PREFIX}[A-Za-z]*|{_PRIVATE_DOCS}|{_PRIVATE_WORKSPACE})|"
    rf"{_MAC_HOME_PREFIX}|/home/[^/\s`]+/(?:workspaces?|projects?)/"
)


def parse_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError("unclosed YAML frontmatter")
    data = yaml.safe_load(parts[1])
    if not isinstance(data, dict):
        raise ValueError("frontmatter must be a mapping")
    return data


def check_local_links(path: Path) -> list[str]:
    errors = []
    for raw in LOCAL_LINK_RE.findall(path.read_text(encoding="utf-8")):
        target = raw.strip().split(maxsplit=1)[0].strip("<>")
        if not target or target.startswith(("#", "http://", "https://", "mailto:", "data:")):
            continue
        file_part = unquote(target.split("#", 1)[0])
        if file_part and not (path.parent / file_part).resolve().exists():
            errors.append(f"{path.relative_to(ROOT)}: broken link -> {target}")
    return errors


def validate_skill(skill_dir: Path) -> list[str]:
    errors = []
    skill_path = skill_dir / "SKILL.md"
    try:
        frontmatter = parse_frontmatter(skill_path)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        return [f"{skill_path.relative_to(ROOT)}: {exc}"]

    extra = set(frontmatter) - ALLOWED_FRONTMATTER
    if extra:
        errors.append(f"{skill_path.relative_to(ROOT)}: unexpected frontmatter keys {sorted(extra)}")
    if frontmatter.get("name") != skill_dir.name:
        errors.append(f"{skill_path.relative_to(ROOT)}: name must match directory")
    description = frontmatter.get("description")
    if not isinstance(description, str) or not description.strip():
        errors.append(f"{skill_path.relative_to(ROOT)}: missing description")
    elif len(description) > 1024:
        errors.append(f"{skill_path.relative_to(ROOT)}: description exceeds 1024 characters")
    if len(skill_path.read_text(encoding="utf-8").splitlines()) > 500:
        errors.append(f"{skill_path.relative_to(ROOT)}: SKILL.md exceeds 500 lines")

    agent_path = skill_dir / "agents" / "openai.yaml"
    if not agent_path.is_file():
        errors.append(f"{agent_path.relative_to(ROOT)}: missing")
    elif agent_path.is_file():
        try:
            agent = yaml.safe_load(agent_path.read_text(encoding="utf-8")) or {}
            interface = agent.get("interface", {})
            short = interface.get("short_description", "")
            prompt = interface.get("default_prompt", "")
            if not 25 <= len(short) <= 64:
                errors.append(f"{agent_path.relative_to(ROOT)}: short_description length must be 25-64")
            if f"${skill_dir.name}" not in prompt:
                errors.append(f"{agent_path.relative_to(ROOT)}: default_prompt must mention ${skill_dir.name}")
        except yaml.YAMLError as exc:
            errors.append(f"{agent_path.relative_to(ROOT)}: invalid YAML: {exc}")

    errors.extend(check_local_links(skill_path))
    for reference in sorted((skill_dir / "references").glob("*.md")):
        errors.extend(check_local_links(reference))
    readmes = list(skill_dir.glob("README*.md"))
    for readme in readmes:
        errors.append(f"{readme.relative_to(ROOT)}: auxiliary README is not allowed inside a skill")
    return errors


def validate_full_stack_templates() -> list[str]:
    errors = []
    template_root = SKILLS_DIR / "full-stack-doc" / "templates"
    expected = {"root": 10, "version": 7, "module": 3, "delivery": 5}
    for scope, count in expected.items():
        actual = len(list((template_root / scope).glob("*.md")))
        if actual != count:
            errors.append(f"full-stack-doc templates/{scope}: expected {count}, found {actual}")
    return errors


def validate_evals(skill_names: set[str]) -> list[str]:
    errors = []
    trigger_path = ROOT / "evals" / "trigger-cases.yaml"
    artifact_path = ROOT / "evals" / "artifact-cases.yaml"
    for path in (trigger_path, artifact_path):
        if not path.is_file():
            errors.append(f"{path.relative_to(ROOT)}: missing")
            continue
        try:
            yaml.safe_load(path.read_text(encoding="utf-8"))
        except yaml.YAMLError as exc:
            errors.append(f"{path.relative_to(ROOT)}: invalid YAML: {exc}")
    if trigger_path.is_file():
        data = yaml.safe_load(trigger_path.read_text(encoding="utf-8")) or {}
        cases = data.get("skills", {})
        if set(cases) != skill_names:
            errors.append("evals/trigger-cases.yaml: skill coverage does not match skills directory")
        for name, value in cases.items():
            if len(value.get("positive", [])) < 3 or len(value.get("negative", [])) < 3:
                errors.append(f"evals/trigger-cases.yaml: {name} needs at least 3 positive and 3 negative cases")
    return errors


def validate_forbidden_content() -> list[str]:
    errors = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path.name.startswith("LICENSE"):
            continue
        if path.resolve() == Path(__file__).resolve():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        match = FORBIDDEN_CONTENT_RE.search(text)
        if match:
            errors.append(f"{path.relative_to(ROOT)}: forbidden content {match.group(0)!r}")
    return errors


def main() -> int:
    skill_dirs = sorted(path for path in SKILLS_DIR.iterdir() if (path / "SKILL.md").is_file())
    errors = []
    for skill_dir in skill_dirs:
        errors.extend(validate_skill(skill_dir))
    for readme in (ROOT / "README.md", ROOT / "README.zh-CN.md"):
        errors.extend(check_local_links(readme))
    errors.extend(validate_full_stack_templates())
    errors.extend(validate_evals({path.name for path in skill_dirs}))
    errors.extend(validate_forbidden_content())

    for error in errors:
        print(f"ERROR    {error}")
    print(f"SUMMARY  skills={len(skill_dirs)} errors={len(errors)}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
