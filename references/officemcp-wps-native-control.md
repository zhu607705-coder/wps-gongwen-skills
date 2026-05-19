# OfficeMCP WPS Native Control Reference

## Primary Source

- OfficeMCP repository: https://github.com/OfficeMCP/OfficeMCP

## What It Provides

OfficeMCP is an MCP server for controlling Microsoft Office applications. Its repository documents support for Office applications and WPS-compatible app names such as `WPS.word`, `wps.excel`, and `wps.powerpoint`.

## Why It Matters For WPS Documents

For rendering-sensitive documents, the reliable authority is the application result:

- whether WPS or Excel opens the file;
- whether fonts are available and applied;
- whether page setup survives reopening;
- whether spreadsheet formulas recalculate in the target app;
- whether the exported PDF matches the intended layout.

OfficeMCP can turn those checks into agent-operable steps when the target environment supports it.

## Recommended Use

Use OfficeMCP for:

- opening an existing `.docx` or `.xlsx`;
- applying formatting through the real app;
- saving a working copy;
- exporting PDF;
- collecting verifiable operation output.

Do not use OfficeMCP as a reason to publish private documents or logs. Keep public skill repositories limited to instructions, tests, and fixture-free examples.
