# WPS Excel Native Workflow Reference

## Purpose

This reference compresses reusable spreadsheet workflow principles into public-safe guidance for WPS/Excel-native workbook work.

## Key Principles

- Formula strings saved into `.xlsx` need recalculation before delivery.
- Zero formula errors is the default quality target.
- Existing templates should keep sheet order, styles, formulas, hidden sheets, merged cells, widths, and number formats.
- Use formulas for dynamic calculations rather than hardcoded computed values.
- WPS/Excel native checks matter for print area, charts, page setup, and PDF export.
- CSV cannot preserve formulas, styles, charts, macros, merged cells, or page setup.

## Error Types To Scan

- `#REF!`
- `#DIV/0!`
- `#VALUE!`
- `#N/A`
- `#NAME?`

## Recommended Tool Layers

- `pandas` for data inspection and tabular transformations.
- `openpyxl` or equivalent workbook libraries for formulas and formatting.
- LibreOffice, Excel, WPS, or OfficeMCP for recalculation and visible export checks.
