---
name: wps-office-native-router
description: "Use when a user mentions WPS Office, Word/WPS documents, PDFs, Excel/WPS spreadsheets, OfficeMCP, native rendering, fonts, formulas, PDF export, or wants an integrated workflow across docx, pdf, and xlsx skills."
type: skill
version: "1.0"
category: productivity
---

# WPS Office Native Router

Use this skill as the suite entry point for WPS-native Office workflows. Its job is to pick the right specialized skill and keep the final verification tied to the application-rendered result.

## Trigger Phrases

- “WPS 原生”
- “把 doc/pdf/Excel skills 融在一起”
- “WPS 里格式错”
- “OfficeMCP 控制 Office/WPS”
- “Word/PDF/Excel 一起处理”
- “字体、公式、导出 PDF 都要检查”

## Routing

Choose the narrowest matching route:

| Request | Route |
|---|---|
| GB/T 9704, 公文模式, 公文字体, 版记, 红头, 页码 | `wps-gongwen-mode` |
| OfficeMCP, app-level open/save/export, `WPS.word`, `wps.excel` | `officemcp-wps-native-control` |
| `.docx`, Word template, fill/edit/format, headers/footers/tables | `wps-doc-native-workflow` |
| PDF export, PDF inspection, final visual proof, PDF/source mismatch | `wps-pdf-render-qa` |
| `.xlsx`, `.xlsm`, `.csv`, formulas, recalculation, WPS Spreadsheets | `wps-excel-native-workflow` |

If the task spans multiple files, run routes in dependency order:

1. source content/data route;
2. native app formatting route;
3. PDF/export verification route;
4. final status report.

## Core Rule

For WPS-sensitive work, the final claim must name the verification layer:

- WPS/Word/Excel native check;
- OfficeMCP operation output;
- WPS-exported PDF;
- LibreOffice or file-level fallback;
- unavailable.

## Source Notes

Read `../../references/wps-office-native-router.md` for the suite-level design rationale.

## Output Contract

```markdown
Office suite status: PASS / PARTIAL / BLOCKED
Routes used: ...
Native verification layer: ...
File types handled: docx/pdf/xlsx/csv/other
Findings: ...
Next action: ...
```

## Public Repo Rule

Do not include user documents, exported PDFs, screenshots, or workbook fixtures in this repository unless they are synthetic or explicitly approved public examples.
