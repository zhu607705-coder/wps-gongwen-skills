---
name: wps-gongwen-mode
description: "Use when a user needs WPS-native Chinese official-document formatting, GB/T 9704-style layout, 公文模式, WPS 公文排版, or fixes for fonts/layout that look wrong after opening a generated .docx in WPS."
type: skill
version: "1.0"
category: documents
---

# WPS Gongwen Mode

Use this skill when the task depends on how a document actually renders in WPS Writer, especially for Chinese official-document layouts, party/government documents, red-head documents, study records,思想汇报, reports, notices, or any `.docx` whose fonts or page layout look wrong after opening in WPS.

## Trigger Phrases

- “WPS 公文模式”
- “WPS 里字体不对”
- “WPS 打开格式错了”
- “公文排版”
- “GB/T 9704”
- “仿宋_GB2312 / 楷体_GB2312 / 小标宋”
- “版记 / 红头 / 页码 / 页边距”
- “导出 PDF 后再检查”

## Core Rule

Treat WPS-rendered output as the verification authority. `python-docx`, Markdown converters, and OpenXML edits can prepare content, but completion requires a WPS-opened check or a clear statement that WPS verification was unavailable.

## Source Notes

Read `../../references/wps-gongwen-mode.md` when you need exact source references or want to compare the workflow against WPS official help.

## Workflow

1. Identify the input and target.

Ask only if the missing detail changes the outcome. Otherwise infer safely and state the assumption.

- Input: `.md`, `.docx`, `.pdf`, pasted text, or images.
- Target: `.docx`, WPS-exported PDF, or both.
- Standard: GB/T 9704-style official-document layout, course template, school form, or custom house style.
- App reality: WPS Writer available locally, OfficeMCP available, or only file-level generation available.

2. Preserve text before formatting.

Save or identify a clean text source before applying WPS formatting. Formatting work should not silently rewrite political statements, names, dates, organization names, or quoted policy language.

3. Apply WPS-native formatting first.

Prefer WPS Writer’s built-in official-document mode or official-document tools for:

- page margins and grid;
- title, main text, heading levels, attachments, and seals/signature areas;
- page number placement;
-版记 and issue metadata;
- font families and sizes used by the target format.

If the user needs repeatable automation, move to `officemcp-wps-native-control` or WPS JSAPI after this manual/native path is understood.

4. Check fonts as installed fonts, not only style names.

Verify whether the required fonts are actually available in WPS:

- `方正小标宋简体` or the local target title font;
- `仿宋_GB2312`;
- `楷体_GB2312`;
- `黑体`;
- any school-provided template font.

If a font is missing or substituted, report it as a blocking issue or a known deviation. Do not claim strict compliance from a style name alone.

5. Verify with WPS-rendered evidence.

Use the strongest available check:

- WPS-exported PDF;
- WPS visual inspection through the desktop app;
- screenshot inspection for representative pages;
- OfficeMCP or WPS automation readback when available.

For screenshot artifacts, inspect and delete temporary files after recording the conclusion unless the user explicitly wants them kept.

6. Report status with validation count.

Use this shape:

```markdown
WPS formatting status: PASS / PARTIAL / BLOCKED
Validation count: 1, current conclusion remains a hypothesis
Checked in: WPS Writer / OfficeMCP / exported PDF / file-level only
Font status: ...
Remaining drift: ...
Next action: ...
```

## Decision Rules

- If WPS is available, open and verify in WPS before finalizing.
- If WPS is unavailable, produce a draft `.docx` and state that WPS-rendered compliance is unverified.
- If the document is private or identity-related, avoid copying it into public repos, fixtures, or screenshots.
- If public GitHub publication is requested, strip personal documents and keep only reusable instructions, sample-free scripts, and source references.

## Common Failure Modes

- `仿宋_GB2312` appears in XML but WPS falls back to another font.
- Title font looks correct in Word but changes in WPS export.
- Page numbers shift after WPS reopens the file.
-版记 alignment changes after PDF export.
- Generated `.docx` passes a script check but fails visual inspection.

When these happen, prefer WPS-native correction and exported-PDF verification over another round of raw XML edits.
