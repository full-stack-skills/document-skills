<div align="center">

# document-skills

**Documentation skills — Mermaid, PlantUML, ProcessOn, API docs, full-stack-doc**

[![GitHub](https://img.shields.io/badge/github-full--statck--skills%2Fdocument-skills-green.svg)](https://github.com/full-statck-skills/document-skills)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-兼容-purple.svg)](https://agentskills.io)

[English](./README.md) | 简体中文

[简介](#-简介) ·
[安装](#-安装) ·
[技能列表](#-技能列表) ·
[支持的智能体](#-支持的智能体) ·
[生态](#-生态)

</div>

---

## 📖 简介

**文档技能** 是一组 AI 编码智能体技能，属于 [Full Stack Skills](https://github.com/partme-ai/full-stack-skills) 生态，由 [PartMe.AI](https://github.com/partme-ai) 维护。

本包包含 **8 个技能**。每个技能是一个独立的 `SKILL.md` 文件，AI 智能体按需加载。

## 📦 安装

```bash
npx skills add full-statck-skills/document-skills
```

或按需安装特定技能：

```bash
npx skills add full-statck-skills/document-skills --skill <skill-name>
```

## 🎯 技能列表 (8)

| 技能 | 描述 |
|------|------|
| `api-doc-generator` | | |
| `doc-coauthoring` | Guide users through a structured workflow for co-authoring documentation. Use when user wants to write documentation,... |
| `full-stack-doc` | > |
| `mermaid` | 使用 Mermaid 在 Markdown 中生成可渲染图表（```mermaid``` 代码块），适用于流程图/时序图/类图/状态图/ER/Gantt/思维导图/时间线等；当用户提到 Mermaid、Markdown 图表，或需要在... |
| `plantuml` | 使用 PlantUML 输出 UML/架构图（```plantuml``` 代码块或 .puml，含 @startuml/@enduml），适用于类图/时序图/组件图/部署图/状态图/C4 模型等；当用户明确提到 PlantUML/U... |
| `processon-diagram-generator` | | |
| `processon-mindmap` | Provides comprehensive guidance for ProcessOn mind mapping including mind map creation, node management, and collabor... |
| `technical-blog-doc` | > |

## 🤖 支持的智能体

适用于 [Claude Code](https://code.claude.com)、[Codex](https://developers.openai.com/codex)、[Cursor](https://cursor.com)、[OpenCode](https://opencode.ai)、[Gemini CLI](https://geminicli.com)、[GitHub Copilot](https://github.com/features/copilot)、[Windsurf](https://codeium.com/windsurf) 及 [70+ 其他智能体](https://agentskills.io/clients)。

## 🌐 生态

| 资源 | 链接 |
|------|------|
| **Full Stack Skills** | [github.com/partme-ai/full-stack-skills](https://github.com/partme-ai/full-stack-skills) |
| **全部技能组** | [github.com/full-statck-skills](https://github.com/full-statck-skills) |
| **Agent Skills 规范** | [agentskills.io](https://agentskills.io) |
| **Skills CLI** | [github.com/vercel-labs/skills](https://github.com/vercel-labs/skills) |

## 📄 许可证

Apache 2.0 — 详见 [LICENSE](LICENSE)。
