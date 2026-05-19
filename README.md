# WPS Gongwen Skills

Public skills for working with Chinese official-document formatting and Office files in WPS/Word/Excel with native-rendering awareness.

The core problem these skills address is simple: many file-generation workflows write valid XML but still look wrong after WPS opens the file. Fonts may fall back, page setup may shift, formulas may remain stale, and exported PDFs can drift from the editable file. These skills push the workflow toward WPS-native formatting, recalculation, export, and rendered verification.

## Included Skills

| Skill | Use when |
|---|---|
| `wps-office-native-router` | You need one entry point that routes WPS/Word/PDF/Excel/OfficeMCP tasks to the right specialized skill. |
| `wps-gongwen-mode` | You need WPS Writer's built-in official-document mode or WPS-native rendering to fix GB/T 9704-style fonts, margins, page numbers,版记, headings, or final PDF appearance. |
| `officemcp-wps-native-control` | You have or can set up OfficeMCP and want an agent to operate Word/WPS as the rendering authority for document creation, formatting, export, and inspection. |
| `wps-doc-native-workflow` | You need to create, edit, fill, format, or verify `.docx` files where WPS/Word rendered layout matters. |
| `wps-pdf-render-qa` | You need to export, inspect, compare, or verify PDFs from WPS/Word/Excel as final visual evidence. |
| `wps-excel-native-workflow` | You need to create, edit, recalculate, format, or export `.xlsx`/`.xlsm`/`.csv` files for WPS Spreadsheets or Excel. |

## Recommended Workflow

1. Draft content or data in the simplest editable source.
2. Apply WPS/Word/Excel-native formatting for layout-sensitive parts.
3. Verify fonts inside WPS, especially `仿宋_GB2312`, `楷体_GB2312`, `黑体`, and `方正小标宋简体`.
4. Recalculate spreadsheets and scan formula errors before delivery.
5. Export from WPS/Word/Excel to PDF when the PDF is the final evidence.
6. Report unresolved substitutions, stale formulas, or layout drift instead of claiming full compliance.

## Integration Notes

This repo does not vendor private local skills. It compresses reusable, public-safe behavior from existing DOCX, PDF, and spreadsheet workflows into WPS-native skills:

- DOCX: preserve templates and verify rendered pages.
- PDF: treat exported pages as visual evidence and clean temporary screenshots.
- Excel: prefer formulas for dynamic work, recalculate, and scan spreadsheet errors.

## References

- WPS official help: `references/wps-gongwen-mode.md`
- OfficeMCP integration notes: `references/officemcp-wps-native-control.md`
- Suite routing notes: `references/wps-office-native-router.md`
- DOCX workflow notes: `references/wps-doc-native-workflow.md`
- PDF render QA notes: `references/wps-pdf-render-qa.md`
- Excel workflow notes: `references/wps-excel-native-workflow.md`

## Validation

Run the package check:

```bash
python3 scripts/validate_package.py
```

This verifies that every skill has required metadata, matching references, and eval coverage.
