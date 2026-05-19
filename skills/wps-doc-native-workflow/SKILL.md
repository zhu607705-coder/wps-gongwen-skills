---
name: wps-doc-native-workflow
description: "Use when creating, editing, filling, formatting, or validating .docx documents that must look correct in WPS/Word, including templates, reports, official-document drafts, institutional forms, headers/footers, tables, and printable layout."
type: skill
version: "1.0"
category: documents
---

# WPS DOC Native Workflow

Use this skill for `.docx` work where final appearance matters in WPS Writer or Word. It complements `wps-gongwen-mode` for official-document style and `officemcp-wps-native-control` for app-level automation.

## Trigger Phrases

- “docx / Word / WPS 文档”
- “填 Word 模板”
- “格式套到这个模板”
- “WPS 打开后错位”
- “表格变形 / 页眉页脚 / 页码”
- “渲染检查 / 导出 PDF 检查”

## Core Rule

The document is complete only after rendered layout has been checked. XML validity or successful `.docx` save is necessary but insufficient for layout-sensitive work.

## Source Notes

Read `../../references/wps-doc-native-workflow.md` when you need the compressed rationale from existing DOCX workflows.

## Routes

Choose one route first:

- `CREATE`: build a new `.docx` from content.
- `EDIT`: revise existing content while preserving structure.
- `FILL`: fill placeholders or institutional forms.
- `FORMAT`: restyle to match a template or WPS official-document layout.
- `VERIFY`: inspect rendered output and report drift.

If the task spans several routes, complete content work before formatting, then verify.

## Workflow

1. Inspect before writing.

Check:

- sections and page breaks;
- headers and footers;
- page numbering;
- tables, merged cells, and column widths;
- styles and heading hierarchy;
- CJK fonts and mixed Chinese-English typography.

2. Work on a safe copy.

For existing files, create or ask for a working copy unless the user explicitly wants the original edited.

3. Preserve structure.

Avoid changing section count, table geometry, numbering schemes, and header/footer settings unless the route requires it. Structural loss is more expensive than a local formatting mistake.

4. Use the right layer.

- Use `python-docx` or OpenXML for controlled text insertion and light formatting.
- Use WPS official-document mode or WPS native APIs for rendering-sensitive CJK layout.
- Use OfficeMCP when the task requires real app open/save/export evidence.

5. Render and inspect.

Prefer WPS-exported PDF or direct WPS visual inspection. If WPS is unavailable, use LibreOffice/PDF rendering as fallback and clearly mark WPS-native verification as missing.

6. Clean temporary evidence.

Screenshots and rendered page images are temporary unless requested as deliverables. Inspect them, record the conclusion, and delete them.

## Output Contract

```markdown
DOCX status: PASS / PARTIAL / BLOCKED
Route: CREATE / EDIT / FILL / FORMAT / VERIFY
App/render check: WPS / Word / LibreOffice fallback / not available
Structure preserved: yes/no/unknown
Font/layout findings: ...
Artifacts: ...
Next action: ...
```

## Escalation Rules

- If a school or organization template exists, match the template rather than inventing a new style.
- If WPS and Word disagree, report the target application and optimize for the user’s actual submission environment.
- If personal documents are involved, keep them out of public fixtures, screenshots, and GitHub commits.
