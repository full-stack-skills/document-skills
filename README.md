<div align="center">

# document-skills

**Documentation skills — Mermaid, PlantUML, ProcessOn, API docs, full-stack-doc**

[![GitHub](https://img.shields.io/badge/github-full--stack--skills%2Fdocument-skills-green.svg)](https://github.com/full-stack-skills/document-skills)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-Compatible-purple.svg)](https://agentskills.io)

English | [简体中文](./README.zh-CN.md)

[Introduction](#-introduction) ·
[Install](#-install) ·
[Skills](#-skills) ·
[Supported Agents](#-supported-agents) ·
[Ecosystem](#-ecosystem)

</div>

---

## 📖 Introduction

**Documentation Skills** is a curated collection of Agent Skills for AI coding agents, part of the [Full Stack Skills](https://github.com/partme-ai/full-stack-skills) ecosystem maintained by [PartMe.AI](https://github.com/partme-ai).

This package includes **8 skills**. Each skill is a self-contained `SKILL.md` file that AI agents load on-demand.

## 📦 Install

```bash
npx skills add full-stack-skills/document-skills
```

Or install specific skills:

```bash
npx skills add full-stack-skills/document-skills --skill <skill-name>
```

## 🎯 Skills (8)

| Skill | Description |
|-------|-------------|
| `api-doc-generator` | | |
| `doc-coauthoring` | Guide users through a structured workflow for co-authoring documentation. Use when user wants to write documentation,... |
| `full-stack-doc` | > |
| `mermaid` | 使用 Mermaid 在 Markdown 中生成可渲染图表（```mermaid``` 代码块），适用于流程图/时序图/类图/状态图/ER/Gantt/思维导图/时间线等；当用户提到 Mermaid、Markdown 图表，或需要在... |
| `plantuml` | 使用 PlantUML 输出 UML/架构图（```plantuml``` 代码块或 .puml，含 @startuml/@enduml），适用于类图/时序图/组件图/部署图/状态图/C4 模型等；当用户明确提到 PlantUML/U... |
| `processon-diagram-generator` | | |
| `processon-mindmap` | Provides comprehensive guidance for ProcessOn mind mapping including mind map creation, node management, and collabor... |
| `technical-blog-doc` | > |

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
| **Full Stack Skills** | [github.com/partme-ai/full-stack-skills](https://github.com/partme-ai/full-stack-skills) |
| **All Skill Groups** | [github.com/full-stack-skills](https://github.com/full-stack-skills) |
| **Agent Skills Spec** | [agentskills.io](https://agentskills.io) |
| **Skills CLI** | [github.com/vercel-labs/skills](https://github.com/vercel-labs/skills) |

## 📄 License

Apache 2.0 — see [LICENSE](LICENSE).
