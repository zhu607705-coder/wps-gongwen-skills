---
name: wps-pdf-render-qa
description: "Use when reading, creating, exporting, inspecting, or validating PDFs produced from WPS/Word/Excel, especially final submission PDFs, visual layout QA, page count checks, form-like documents, tables, fonts, and rendering drift."
type: skill
version: "1.0"
category: documents
---

# WPS PDF Render QA

Use this skill when PDF is the final evidence layer or the safest way to verify how a WPS/Word/Excel document will be submitted.

## Trigger Phrases

- “导出 PDF”
- “PDF 检查”
- “WPS 导出的 PDF”
- “版式最终确认”
- “页数 / 页码 / 字体 / 表格”
- “PDF 和 docx 不一致”
- “渲染截图”

## Core Rule

Use PDF as rendered evidence, not as a blind conversion target. A PDF must be inspected for page count, font appearance, margins, clipping, table overflow, headers, footers, and page numbers.

## Source Notes

Read `../../references/wps-pdf-render-qa.md` when you need the compressed rationale from existing PDF workflows.

## Routes

- `READ`: extract text or review a PDF.
- `EXPORT`: create a PDF from WPS/Word/Excel.
- `VERIFY`: inspect a generated PDF for submission readiness.
- `COMPARE`: compare `.docx` or `.xlsx` source with exported PDF.
- `REPAIR`: find what must be fixed upstream, then regenerate PDF.

## Workflow

1. Establish the source of truth.

If PDF is the final submission file, verify PDF directly. If PDF is an intermediate proof, trace issues back to the source `.docx` or `.xlsx`.

2. Render or inspect pages.

Use available tools to inspect:

- page count;
- margins and page breaks;
- CJK font appearance;
- headers, footers, and page numbers;
- tables, figures, and form-like fields;
- clipped or overlapping text.

3. Prefer upstream fixes.

If a PDF exported from WPS has layout issues, fix the source document in WPS/Word/Excel, then export again. Avoid patching the PDF directly unless the source is unavailable or the user explicitly asks.

4. Handle image-only PDFs separately.

If text extraction fails because pages are scanned images, report that OCR or screenshot review is required.

5. Clean temporary images.

Temporary page renders and screenshots should be deleted after inspection unless kept as requested evidence.

## Output Contract

```markdown
PDF status: PASS / PARTIAL / BLOCKED
Route: READ / EXPORT / VERIFY / COMPARE / REPAIR
Source app: WPS / Word / Excel / unknown
Page check: ...
Font/layout findings: ...
Temporary artifacts cleaned: yes/no
Next action: ...
```

## Common Findings

- WPS exports with substituted CJK fonts.
- Page breaks differ from the editable document view.
- Tables overflow after export.
- Headers or footers disappear on the first page or section break.
- PDF text is image-only and needs OCR for reliable extraction.
