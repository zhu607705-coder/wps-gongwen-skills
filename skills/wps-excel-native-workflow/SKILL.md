---
name: wps-excel-native-workflow
description: "Use when creating, editing, checking, or exporting .xlsx/.xlsm/.csv spreadsheets for WPS Spreadsheets or Excel, including formulas, formatting, template preservation, recalculation, PDF export, and OfficeMCP/WPS native verification."
type: skill
version: "1.0"
category: spreadsheets
---

# WPS Excel Native Workflow

Use this skill for spreadsheet work where formulas, formatting, recalculation, or WPS/Excel rendering matters.

## Trigger Phrases

- “Excel / WPS 表格 / xlsx / xlsm / csv”
- “公式错误”
- “WPS 表格打开”
- “导出表格 PDF”
- “保留模板格式”
- “公式复算”
- “OfficeMCP 控制 Excel/WPS”

## Core Rule

A spreadsheet is complete only after formulas and visible workbook layout have been verified. Saving a workbook with formula strings is not enough.

## Source Notes

Read `../../references/wps-excel-native-workflow.md` when you need the compressed rationale from existing spreadsheet workflows.

## Routes

- `READ`: inspect workbook data and sheets.
- `CREATE`: build a new workbook.
- `EDIT`: update an existing workbook.
- `FORMAT`: preserve or apply workbook styling.
- `RECALC`: force formula recalculation and scan errors.
- `EXPORT`: export sheets to PDF through WPS/Excel when visual fidelity matters.

## Workflow

1. Inspect workbook shape.

Check:

- sheet names and hidden sheets;
- used ranges;
- formulas and named ranges;
- merged cells and frozen panes;
- existing styles, number formats, and column widths;
- external links and macros.

2. Preserve templates.

When the user provides a template, match its existing style, sheet order, formulas, and visible conventions. Do not impose a new color scheme unless asked.

3. Use formulas for dynamic calculations.

If a result should update when inputs change, write spreadsheet formulas rather than hardcoded Python-calculated values.

4. Recalculate and scan errors.

After creating or editing formulas, recalculate with Excel/WPS/LibreOffice or an available automation bridge. Scan for:

- `#REF!`;
- `#DIV/0!`;
- `#VALUE!`;
- `#N/A`;
- `#NAME?`.

5. Verify native rendering when required.

Use WPS/Excel or OfficeMCP for:

- print area and page setup;
- PDF export;
- chart rendering;
- formula recalculation in the target app;
- workbook display checks.

6. Treat CSV separately.

CSV carries data only. It does not preserve formulas, charts, styles, merged cells, or page setup. Say this when the user asks for Excel-like behavior from CSV.

## Output Contract

```markdown
Spreadsheet status: PASS / PARTIAL / BLOCKED
Route: READ / CREATE / EDIT / FORMAT / RECALC / EXPORT
Native app check: WPS / Excel / LibreOffice fallback / not available
Formula status: ...
Layout/export findings: ...
Artifacts: ...
Next action: ...
```

## Safety Rules

- Do not publish user workbooks or exported PDFs to public repositories.
- Do not preserve external links to private files in public examples.
- For financial or grading spreadsheets, report any formula uncertainty explicitly.
