# WPS Office Native Router Reference

## Purpose

This reference explains the suite-level integration of WPS-native document, PDF, spreadsheet, official-document, and OfficeMCP workflows.

## Design Rationale

The shared problem across DOCX, PDF, and Excel workflows is rendered fidelity:

- DOCX files can have valid XML while WPS displays wrong fonts or layout.
- PDFs can exist while pages contain clipping, font substitution, or table overflow.
- Spreadsheets can save formulas while calculated values remain stale or errors are hidden.

The router keeps the agent from treating file creation as completion. It sends the task to the narrow skill, then requires a named verification layer.

## Route Order

For multi-file tasks:

1. Create or edit the editable source file.
2. Apply WPS/Word/Excel-native formatting or recalculation.
3. Export PDF if needed.
4. Inspect final rendered evidence.
5. Report PASS, PARTIAL, or BLOCKED with remaining drift.
