# WPS Gongwen Skills

Public skills for working with Chinese official-document formatting in WPS/Word with native-rendering awareness.

The core problem these skills address is simple: many `.docx` generation workflows write valid XML but still look wrong after WPS opens the file. Fonts may fall back, page setup may shift, and official-document layout can drift. These skills push the workflow toward WPS-native formatting and WPS-rendered verification.

## Included Skills

| Skill | Use when |
|---|---|
| `wps-gongwen-mode` | You need WPS Writer's built-in official-document mode or WPS-native rendering to fix GB/T 9704-style fonts, margins, page numbers,版记, headings, or final PDF appearance. |
| `officemcp-wps-native-control` | You have or can set up OfficeMCP and want an agent to operate Word/WPS as the rendering authority for document creation, formatting, export, and inspection. |

## Recommended Workflow

1. Draft content in Markdown or plain `.docx`.
2. Apply WPS-native official-document formatting.
3. Verify fonts inside WPS, especially `仿宋_GB2312`, `楷体_GB2312`, `黑体`, and `方正小标宋简体`.
4. Export from WPS to PDF for final visual verification.
5. Report unresolved substitutions or layout drift instead of claiming full compliance.

## References

- WPS official help: `references/wps-gongwen-mode.md`
- OfficeMCP integration notes: `references/officemcp-wps-native-control.md`

## Validation

Run the package check:

```bash
python3 scripts/validate_package.py
```

This verifies that every skill has required metadata, matching references, and eval coverage.
