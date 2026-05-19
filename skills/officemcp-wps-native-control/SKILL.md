---
name: officemcp-wps-native-control
description: "Use when a user wants Codex/Claude to control Word or WPS through OfficeMCP for native document formatting, WPS.word automation, official-document layout, PDF export, or font/rendering verification."
type: skill
version: "1.0"
category: documents
---

# OfficeMCP WPS Native Control

Use this skill when the user wants agentic control over Word/WPS as the document rendering environment, especially for WPS font issues, official-document layout drift, PDF export, or repeatable document QA.

## Trigger Phrases

- “OfficeMCP”
- “MCP 控制 WPS”
- “WPS.word”
- “让 Codex 直接操作 WPS”
- “WPS 原生验证”
- “打开 Word/WPS 后导出 PDF”
- “字体实际显示错误”
- “公文格式自动检查”

## Core Rule

Use OfficeMCP as the bridge to the live Office/WPS application when available. File-level editing remains a staging step; the final answer should be based on what the application opened, formatted, saved, or exported.

## Source Notes

Read `../../references/officemcp-wps-native-control.md` before installing, configuring, or citing OfficeMCP behavior.

## Preconditions

Confirm these before claiming native automation:

- OfficeMCP is installed or the user has asked you to set it up.
- Word or WPS Writer exists on the target machine.
- The target app name is known, such as `WPS.word`, `wps.excel`, or Word.
- The target document path is local and safe to open.
- Public publication will exclude private documents and absolute local paths.

If one precondition is missing, state the blocker and continue with the best verified fallback.

## Workflow

1. Define the document operation.

Classify the request:

- Create: generate content and open it in WPS/Word.
- Format: apply page setup, fonts, styles, headings, page numbers, and official-document sections.
- Inspect: read back styles, font names, page setup, and visible layout.
- Export: save `.docx`, export PDF, or create comparison evidence.
- Repair: fix font fallback or layout drift observed in WPS.

2. Start with a safe copy.

When editing an existing document, make a working copy unless the user explicitly asks to modify the original. Keep private content out of the skill repo and public examples.

3. Use native operations for rendering-sensitive work.

Prefer OfficeMCP or app-level APIs for:

- opening the document in the real application;
- applying fonts and paragraph styles;
- setting page margins and page numbering;
- exporting to PDF from the application;
- inspecting the final visible document state.

Use `python-docx`, Pandoc, or OpenXML only for draft creation, bulk text insertion, or fixture-free preprocessing.

4. Verify the application result.

Evidence can include:

- OfficeMCP command output;
- WPS/Word readback of styles and properties;
- WPS-exported PDF existence and page count;
- representative visual inspection;
- a concise diff between expected and observed font/layout properties.

5. Handle missing WPS/OfficeMCP gracefully.

If OfficeMCP is unavailable:

- do not pretend native automation happened;
- produce a file-level draft if useful;
- tell the user exactly what native check remains;
- suggest the minimal OfficeMCP setup path.

## Output Contract

Return a concise status:

```markdown
Native control status: PASS / PARTIAL / BLOCKED
App used: WPS.word / Word / file-level fallback
Operations completed: ...
Verification evidence: ...
Font/layout findings: ...
Public-safe artifacts: yes/no
Next action: ...
```

## Safety And Publication Rules

- Never publish user documents, screenshots, generated PDFs, or school forms unless explicitly requested.
- Do not commit tokens, OfficeMCP local config, logs containing private paths, or MCP server secrets.
- If a command affects files outside a disposable copy, disclose the path and risk before running it.
- If the workflow has only one validation, label the pattern as a hypothesis.

## Best Pairing

Use `wps-gongwen-mode` first when the main task is official-document formatting. Use this skill when the task needs repeatable native automation through OfficeMCP.
