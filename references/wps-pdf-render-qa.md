# WPS PDF Render QA Reference

## Purpose

This reference compresses reusable PDF workflow principles into public-safe guidance for final document verification.

## Key Principles

- PDF is often the final submission evidence and should be inspected directly.
- Page count, margins, clipping, font appearance, headers, footers, and table overflow matter more than conversion success alone.
- If a WPS-exported PDF is wrong, fix the upstream `.docx` or `.xlsx` when possible.
- Image-only PDFs need OCR or screenshot review for reliable content extraction.
- Temporary page renders and screenshots should be deleted after inspection unless kept as explicit evidence.

## Useful Checks

- Does every expected page exist?
- Are page numbers visible and consistent?
- Are CJK fonts visually correct?
- Are tables and figures contained inside margins?
- Is text selectable, or is the PDF image-only?
