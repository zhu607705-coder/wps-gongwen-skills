# Repository Rules

This repository packages public Codex/Claude-style skills for native WPS official-document workflows.

## Structure

- `skills/`: one directory per skill, each with a required `SKILL.md`.
- `references/`: concise source notes and implementation references loaded only when needed.
- `evals/`: prompt-level validation cases for the skills.
- `scripts/`: deterministic local checks for packaging quality.

## Naming

- Skill directories use lowercase kebab-case.
- Reference files use lowercase kebab-case.
- Do not place private course materials, personal identity documents, or generated `.docx` outputs in this repository.

## Cleanup

- Temporary screenshots, rendered PDFs, and WPS export artifacts belong outside this repo unless they are explicit fixtures.
- If visual verification screenshots are created during testing, inspect them and delete them in the same turn unless they are deliverables.

## Publication Safety

- Keep the repository safe for public GitHub publication.
- Do not include tokens, local absolute paths, private documents, or school-specific personal records.
- If a claim depends on one local validation, label it as a hypothesis.
