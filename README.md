<div align="center">

# document-skills

**Documentation skills — Mermaid, PlantUML, ProcessOn, API docs, full-stack-doc, MarkItDown (awesome / cli / ocr)**

[![GitHub](https://img.shields.io/badge/github-full--stack--skills%2Fdocument-skills-green.svg)](https://github.com/full-stack-skills/document-skills)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-Compatible-purple.svg)](https://agentskills.io)

English | [简体中文](./README.zh-CN.md)

[Introduction](#-introduction) ·
[Install](#-install) ·
[Skills](#-skills) ·
[Usage Guide](#-usage-guide) ·
[Supported Agents](#-supported-agents) ·
[Ecosystem](#-ecosystem)

</div>

---

## 📖 Introduction

**Documentation Skills** is a curated collection of Agent Skills for AI coding agents, published in the [Full Stack Skills](https://github.com/full-stack-skills) ecosystem.

This package includes **11 skills**. Each skill is a self-contained `SKILL.md` file that AI agents load on-demand.

## 📦 Install

```bash
npx skills add full-stack-skills/document-skills
```

Or install specific skills:

```bash
npx skills add full-stack-skills/document-skills --skill <skill-name>
```

## 🎯 Skills (11)

| Skill | Description |
|-------|-------------|
| `api-doc-generator` | Generate traceable API documentation from OpenAPI, routes, source, and tests |
| `doc-coauthoring` | Gather context, draft collaboratively, and run independent reader tests |
| `full-stack-doc` | Build an example-rich documentation system from lifecycle, README, Rust-profile, and complete architecture template families |
| `markitdown-awesome` | Overview & navigation for Microsoft MarkItDown — capabilities, supported formats, three-path decision tree (awesome / cli / ocr), and side-by-side comparison with textract / unstructured / pandoc / docling / Azure DI / Azure CU |
| `markitdown-cli` | Complete CLI guide for `markitdown` — every flag (`-o/-x/-m/-c/-d/-e/-p/--use-cu/--cu-endpoint/--cu-analyzer/--cu-file-types/--list-plugins/--keep-data-uris`), I/O matrix, shell-toolchain integration, Azure backends, troubleshooting |
| `markitdown-ocr` | Drive the `markitdown-ocr` plugin to run LLM Vision OCR (OpenAI-compatible, including Azure OpenAI / Gemini / local vLLM / Ollama) on PDF / DOCX / PPTX / XLSX embedded images and scanned pages — install, configuration, Python API, scanned-PDF full-page fallback, per-format behavior, custom prompts, cost & failure handling |
| `mermaid` | Create Mermaid diagrams that render directly in Markdown and README files |
| `plantuml` | Create precise UML, C4, and enterprise architecture source |
| `processon-diagram-generator` | Generate editable DSL and rendered images through the ProcessOn API |
| `processon-mindmap` | Organize a hierarchical mind map ready for ProcessOn |
| `technical-blog-doc` | Write reproducible technical tutorials with environment, commands, and evidence |

`full-stack-doc` includes the original detailed root, version, module, and delivery templates plus Java, Rust, plugin, skill-ecosystem, and complete-reference README templates. The Rust common template composes with profiles for file formats, upstream parity, toolbox workspaces, authentication frameworks, design-only repositories, and multilingual layouts. Its complete architecture master composes with runtime, plugin, edge, event, AI/RAG, and observability/control-plane profiles. API discovery loads focused guidance for OpenAPI, Spring, FastAPI, NestJS, Express, or Gin.

## 🚀 Usage Guide

### Invoke a skill

After installation, name the skill explicitly and describe the expected artifact, source material, output location, and verification requirements. Client syntax varies: some clients expose `/skill-name`, Codex-compatible prompts may use `$skill-name`, and clients with automatic discovery also accept the plain skill name.

These three prompts are equivalent in intent:

```text
/full-stack-doc Create a detailed architecture document from the current repository.
$full-stack-doc Create a detailed architecture document from the current repository.
Use the full-stack-doc skill to create a detailed architecture document from the current repository.
```

The examples below use `/skill-name`; replace the prefix when your client uses another form.

### Choose the right skill

| Skill | Use it for | Example prompt |
|-------|------------|----------------|
| `api-doc-generator` | API inventories and evidence-backed endpoint references | `Use /api-doc-generator to generate API documentation from the current Spring controllers, DTOs, and tests, with a source for every endpoint.` |
| `doc-coauthoring` | Collaborative proposals, RFCs, specifications, and reader tests | `Use /doc-coauthoring to help me draft a cache-refactoring RFC and run an independent reader review.` |
| `full-stack-doc` | Product documentation suites, PRDs, architecture, UI, versions, delivery docs, and project READMEs | `Use /full-stack-doc to audit the existing product-docs tree and complete the missing product-level and version-level documents.` |
| `markitdown-awesome` | MarkItDown capability discovery and tool selection | `Use /markitdown-awesome to compare MarkItDown, Pandoc, and Docling for our PDF-to-Markdown workflow.` |
| `markitdown-cli` | Exact `markitdown` commands, flags, pipelines, and batch conversion | `Use /markitdown-cli to provide commands that batch-convert DOCX and PPTX files under docs/.` |
| `markitdown-ocr` | OCR for scanned pages and images embedded in PDF or Office files | `Use /markitdown-ocr to convert this scanned PDF to Markdown and document model configuration, cost, and fallback behavior.` |
| `mermaid` | Markdown-native flows, sequences, states, journeys, timelines, and lightweight architecture | `Use /mermaid to turn the order-refund flow into a sequence diagram that renders in README.md.` |
| `plantuml` | Precise UML, C4, deployment, and enterprise architecture source | `Use /plantuml to generate C4 container and deployment diagrams for the authentication system.` |
| `processon-diagram-generator` | Hosted, editable ProcessOn diagrams and optional rendering | `Use /processon-diagram-generator to create an editable login swimlane diagram and return its DSL and rendered output.` |
| `processon-mindmap` | ProcessOn-ready hierarchical mind-map outlines | `Use /processon-mindmap to organize these meeting notes into a ProcessOn-ready mind map.` |
| `technical-blog-doc` | Reproducible tutorials, integration guides, deployment articles, and verification records | `Use /technical-blog-doc to write a reproducible deployment tutorial from the current repository and include a verification record.` |

`processon-diagram-generator` requires `PROCESSON_API_KEY` for remote generation. The other examples can begin with local source or material supplied in the conversation; access to external services still depends on the active client and environment.

### `full-stack-doc` prompt examples

```text
Use /full-stack-doc to create a detailed architecture document.
Use /full-stack-doc to create detailed English and Chinese README documents.
Use /full-stack-doc to create a detailed technical deep-dive document.
Use /full-stack-doc to initialize the 10 product-level documents and the 7 V1 documents.
Use /full-stack-doc to create a V2 PRD, version architecture, and feature-menu plan from evidence in the current repository.
Use /full-stack-doc to audit the current product-docs structure, naming, cross-references, and content gaps, separating facts, inferences, and open questions.
```

For more reliable output, make the request concrete:

```text
Use /full-stack-doc with {repository or source material} for {target readers} to create {document type} in {output directory}. Inspect existing documents and source first, preserve confirmed conventions, mark assumptions and open questions, and run the applicable validation checks before delivery.
```

## ✅ Quality checks

```bash
python3 scripts/validate_repository.py
python3 skills/full-stack-doc/scripts/validate_templates.py
python3 -m unittest discover -s skills/full-stack-doc/tests -p 'test_*.py'
python3 -m unittest discover -s skills/api-doc-generator/tests -p 'test_*.py'
python3 -m unittest discover -s skills/processon-diagram-generator/tests -p 'test_*.py'
python3 scripts/run_artifact_evals.py
```

Trigger positive/negative cases and artifact regression cases live under `evals/`.

## 🤖 Supported Agents

Works with [Claude Code](https://code.claude.com), [Codex](https://developers.openai.com/codex), [Cursor](https://cursor.com), [OpenCode](https://opencode.ai), [Gemini CLI](https://geminicli.com), [GitHub Copilot](https://github.com/features/copilot), [Windsurf](https://codeium.com/windsurf), and [70+ others](https://agentskills.io/clients).

### Claude Code Installation

**Option 1: npx skills CLI (Recommended)**

```bash
npx skills add full-stack-skills/document-skills
```

**Option 2: Manual Installation**

```bash
git clone https://github.com/full-stack-skills/document-skills.git
cp -r document-skills/skills/* .claude/skills/
```

For more details, see the [Claude Code Skills Guide](https://code.claude.com/docs/en/skills) and [Agent Skills Spec](https://agentskills.io/).

## 🌐 Ecosystem

| Resource | Link |
|----------|------|
| **Full Stack Skills** | [github.com/full-stack-skills](https://github.com/full-stack-skills) |
| **All Skill Groups** | [github.com/full-stack-skills](https://github.com/full-stack-skills) |
| **Agent Skills Spec** | [agentskills.io](https://agentskills.io) |
| **Skills CLI** | [github.com/vercel-labs/skills](https://github.com/vercel-labs/skills) |

## 📄 License

Apache 2.0 — see [LICENSE](LICENSE).

Third-party attribution notices: see [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md).
