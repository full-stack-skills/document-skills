<div align="center">

# document-skills

**Documentation skills — Mermaid, PlantUML、ProcessOn、API 文档、full-stack-doc、MarkItDown（awesome / cli / ocr）**

[![GitHub](https://img.shields.io/badge/github-full--stack--skills%2Fdocument-skills-green.svg)](https://github.com/full-stack-skills/document-skills)
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

**文档技能** 是一组面向 AI 编码智能体的可复用技能，发布于 [Full Stack Skills](https://github.com/full-stack-skills) 生态。

本包包含 **11 个技能**。每个技能是一个独立的 `SKILL.md` 文件，AI 智能体按需加载。

## 📦 安装

```bash
npx skills add full-stack-skills/document-skills
```

或按需安装特定技能：

```bash
npx skills add full-stack-skills/document-skills --skill <skill-name>
```

## 🎯 技能列表 (11)

| 技能 | 描述 |
|------|------|
| `api-doc-generator` | 从 OpenAPI、路由、源码和测试生成可追溯的 API 文档 |
| `doc-coauthoring` | 协作收集上下文、起草文档并进行独立读者测试 |
| `full-stack-doc` | 使用生命周期、README、Rust 剖面和完整架构模板族构建详细文档体系 |
| `markitdown-awesome` | MarkItDown 的概览与导航：能力边界、支持格式、三路径决策树（awesome / cli / ocr），并与 textract / unstructured / pandoc / docling / Azure DI / Azure CU 对比选型 |
| `markitdown-cli` | `markitdown` 命令行的完整使用指南：所有参数（`-o/-x/-m/-c/-d/-e/-p/--use-cu/--cu-endpoint/--cu-analyzer/--cu-file-types/--list-plugins/--keep-data-uris`）、输入输出矩阵、与 shell 工具链集成、Azure 后端切换、排错速查 |
| `markitdown-ocr` | 通过 `markitdown-ocr` 插件用 LLM Vision（OpenAI 兼容，含 Azure OpenAI / Gemini / 本地 vLLM / Ollama）对 PDF / DOCX / PPTX / XLSX 内嵌图片与扫描页做 OCR：安装、配置、Python API、扫描 PDF 整页回退、各格式差异、自定义 prompt、成本与失败处理 |
| `mermaid` | 为 Markdown 和 README 生成可直接渲染的 Mermaid 图表 |
| `plantuml` | 生成精确的 UML、C4 和企业架构图源码 |
| `processon-diagram-generator` | 通过 ProcessOn API 生成可编辑 DSL 和渲染图片 |
| `processon-mindmap` | 整理可导入 ProcessOn 的层级化思维导图 |
| `technical-blog-doc` | 编写有环境记录、验证命令和证据来源的技术教程 |

`full-stack-doc` 保留原有的产品级、版本级、模块级和交付级详细模板，并提供 Java、Rust、插件、技能生态及完整参考 README 模板。Rust 公共模板可组合文件格式、上游兼容、工具箱 Workspace、认证框架、纯设计阶段和多语言布局剖面；完整架构母模板可组合运行时、插件、边缘设备、消息事件、AI/RAG 和可观测控制面剖面。API 文档技能按 OpenAPI、Spring、FastAPI、NestJS、Express 和 Gin 分别加载参考。

## ✅ 质量验证

```bash
python3 scripts/validate_repository.py
python3 skills/full-stack-doc/scripts/validate_templates.py
python3 -m unittest discover -s skills/full-stack-doc/tests -p 'test_*.py'
python3 -m unittest discover -s skills/api-doc-generator/tests -p 'test_*.py'
python3 -m unittest discover -s skills/processon-diagram-generator/tests -p 'test_*.py'
python3 scripts/run_artifact_evals.py
```

触发正反例与产物回归用例位于 `evals/`。

## 🤖 支持的智能体

适用于 [Claude Code](https://code.claude.com)、[Codex](https://developers.openai.com/codex)、[Cursor](https://cursor.com)、[OpenCode](https://opencode.ai)、[Gemini CLI](https://geminicli.com)、[GitHub Copilot](https://github.com/features/copilot)、[Windsurf](https://codeium.com/windsurf) 及 [70+ 其他平台](https://agentskills.io/clients)。

### Claude Code 安装

**方式一：npx skills CLI（推荐）**

```bash
npx skills add full-stack-skills/document-skills
```

**方式二：手动安装**

```bash
git clone https://github.com/full-stack-skills/document-skills.git
cp -r document-skills/skills/* .claude/skills/
```

更多详情请参阅 [Claude Code 技能指南](https://code.claude.com/docs/en/skills) 和 [Agent Skills 规范](https://agentskills.io/)。

## 🌐 生态

| 资源 | 链接 |
|------|------|
| **Full Stack Skills** | [github.com/full-stack-skills](https://github.com/full-stack-skills) |
| **全部技能组** | [github.com/full-stack-skills](https://github.com/full-stack-skills) |
| **Agent Skills 规范** | [agentskills.io](https://agentskills.io) |
| **Skills CLI** | [github.com/vercel-labs/skills](https://github.com/vercel-labs/skills) |

## 📄 许可证

Apache 2.0 — 详见 [LICENSE](LICENSE)。
