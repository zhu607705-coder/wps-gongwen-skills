# WPS Gongwen Mode Reference

## Primary Sources

- WPS official help page for 公文模式: https://www.wps.cn/learning/question/detail/id/333099.html
- WPS solution API overview for Office add-ins and client APIs: https://solution.wps.cn/docs/client/api/overview.html
- WPS Word Font API reference: https://solution.wps.cn/docs/client/api/Word/Font.html

## Practical Interpretation

WPS 公文模式 is useful when the user needs WPS-native layout behavior, especially for official-document-like files where a generated `.docx` looks acceptable in XML but fails in WPS visual rendering.

Use the official mode or native APIs for:

- document setup;
- font assignment;
- paragraph and heading formatting;
- page number behavior;
- official-document sections such as版记 and attachments;
- final PDF export.

## Fonts To Check

Common Chinese official-document workflows often depend on these fonts:

- `方正小标宋简体`;
- `仿宋_GB2312`;
- `楷体_GB2312`;
- `黑体`.

Installed font availability matters. A style name written into `.docx` is insufficient evidence because WPS can substitute fonts during rendering or export.

## Verification Notes

One local WPS check counts as one validation. Keep it at hypothesis level until repeated on more documents or machines.
