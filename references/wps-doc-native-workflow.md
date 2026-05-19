# WPS DOC Native Workflow Reference

## Purpose

This reference compresses reusable DOCX workflow principles into public-safe guidance for WPS-native document work.

## Key Principles

- Rendered layout is the completion gate for layout-sensitive `.docx` work.
- Existing templates should be preserved before new styling is applied.
- Headers, footers, section breaks, page numbering, and table geometry are high-risk areas.
- WPS and Word can render the same `.docx` differently, especially with CJK fonts and page setup.
- Temporary visual QA artifacts should be cleaned after inspection.

## Recommended Tool Layers

- `python-docx` or OpenXML for content insertion and controlled structural edits.
- WPS official-document mode for CJK official-document layout.
- OfficeMCP or WPS/Word native APIs for app-opened verification and PDF export.
- LibreOffice rendering as fallback only when WPS is unavailable.
