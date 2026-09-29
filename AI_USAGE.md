
### `AI_USAGE.md`

```markdown
| Date/commit | Tool | Prompt | Disposition (Accepted/Modified/Rejected) | What changed & why (if modified) | In my own words, how this works |
|---|---|---|---|---|---|
| 2026-09-30 | Cursor | Give me the first-commit files: startup contract for Lend (PORT, DATA_DIR, 0.0.0.0, SQLite schema) plus ADR-1. | Accepted |  | `main` calls `init_db`, reads `PORT` (default 5000), and runs Flask on `0.0.0.0` with the reloader off. `database_path` joins `DATA_DIR` (default `data`) with `lend.db`. `connect` creates that directory, opens SQLite, turns on foreign keys, and returns rows as `sqlite3.Row`. `init_db` runs `SCHEMA`, which creates `tools`, `members`, `loans`, and the partial unique index `one_open_loan_per_tool` on `loans.tool_id` where `returned_at` is null. |