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
[使用指南](#-使用指南) ·
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

## 🚀 使用指南

### 调用技能

安装后，显式写出技能名，并说明期望产物、输入资料、输出位置和验证要求。不同客户端的调用语法可能不同：部分客户端使用 `/skill-name`，兼容 Codex 的提示词可以使用 `$skill-name`，支持自动发现的客户端也可以直接写技能名。

下面三种写法表达同一个意图：

```text
/full-stack-doc 基于当前仓库输出详细的架构文档。
$full-stack-doc 基于当前仓库输出详细的架构文档。
使用 full-stack-doc 技能，基于当前仓库输出详细的架构文档。
```

下文统一使用 `/skill-name` 举例；如果你的客户端使用其他前缀，请替换为对应写法。

### 选择合适的技能

| 技能 | 适用场景 | 示例提示词 |
|------|----------|------------|
| `api-doc-generator` | 接口清单和可追溯的 API 参考文档 | `使用 /api-doc-generator 技能，从当前 Spring 项目的控制器、DTO 和测试生成 API 文档，并为每个接口标注证据来源。` |
| `doc-coauthoring` | 协作编写提案、RFC、技术规格并做读者测试 | `使用 /doc-coauthoring 技能，与我协作编写一份缓存重构 RFC，并进行独立读者检查。` |
| `full-stack-doc` | 产品文档体系、PRD、架构、UI、版本、交付文档和项目 README | `使用 /full-stack-doc 技能，审计现有 product-docs，并补齐产品级和版本级文档。` |
| `markitdown-awesome` | 了解 MarkItDown 能力边界并完成工具选型 | `使用 /markitdown-awesome 技能，比较 MarkItDown、Pandoc 和 Docling，给出 PDF 转 Markdown 方案。` |
| `markitdown-cli` | 获取准确的 `markitdown` 命令、参数、管道和批量转换方案 | `使用 /markitdown-cli 技能，给出批量转换 docs/ 下 DOCX 和 PPTX 文件的命令。` |
| `markitdown-ocr` | 对扫描页及 PDF、Office 文件中的图片做 OCR | `使用 /markitdown-ocr 技能，把这份扫描 PDF 转为 Markdown，并说明模型配置、成本和失败回退。` |
| `mermaid` | 生成可嵌入 Markdown 的流程、时序、状态、旅程、时间线和轻量架构图 | `使用 /mermaid 技能，把订单退款流程画成可在 README.md 渲染的时序图。` |
| `plantuml` | 生成精确的 UML、C4、部署图和企业架构图源码 | `使用 /plantuml 技能，为鉴权系统生成 C4 容器图和部署图源码。` |
| `processon-diagram-generator` | 生成可在线编辑的 ProcessOn 图表及可选渲染结果 | `使用 /processon-diagram-generator 技能，生成可编辑的登录泳道图，并返回 DSL 和渲染结果。` |
| `processon-mindmap` | 整理可导入 ProcessOn 的层级思维导图 | `使用 /processon-mindmap 技能，把这份会议纪要整理为可导入 ProcessOn 的思维导图。` |
| `technical-blog-doc` | 编写可复现的技术教程、集成指南、部署文章和验证记录 | `使用 /technical-blog-doc 技能，基于当前仓库写一篇可复现的部署教程，并附验证记录。` |

`processon-diagram-generator` 远程生成时需要配置 `PROCESSON_API_KEY`。其他示例可以从本地源码或对话中提供的资料开始；外部服务是否可用仍取决于当前客户端和运行环境。

### `full-stack-doc` 常用示例

```text
使用 /full-stack-doc 技能，输出详细的架构文档。
使用 /full-stack-doc 技能，输出详细的中英文 README 文档。
使用 /full-stack-doc 技能，输出详细的技术细分文档。
使用 /full-stack-doc 技能，初始化产品根级 10 份文档和 V1 的 7 份版本文档。
使用 /full-stack-doc 技能，基于当前仓库证据输出 V2 PRD、版本架构和功能菜单规划。
使用 /full-stack-doc 技能，审计现有 product-docs 的目录、命名、交叉引用和内容缺口，并区分事实、推断与待确认项。
```

为了获得更可靠的结果，可以把请求写得更具体：

```text
使用 /full-stack-doc 技能，基于 {目标仓库或资料}，面向 {目标读者}，输出 {文档类型} 到 {输出目录}。先检查现有文档和源码，保留已确认的项目约定，标注假设与待确认项，并在交付前执行适用的校验。
```

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

第三方组件归属声明：详见 [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md)。
