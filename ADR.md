## [1]. Backend language and framework
Date: 2026-09-30
Status: Decided
Context: Lend is one process with server-rendered pages and a single SQLite file. Startup has to be one command, bound to 0.0.0.0, configured only through PORT and DATA_DIR. Every layer of this app has to be explainable on paper.
Decision: Use Python with Flask, Jinja templates, and the standard-library sqlite3 module.
Alternatives considered: Django, rejected because its ORM, admin, and auth would sit unused on two small domains. FastAPI, rejected because the interface is HTML forms, so Flask's built-in template rendering is the smaller fit.
Consequences: Runtime dependencies stay at Flask. SQL stays visible in lend/db.py, and there is no second frontend process to deploy in Assignment 2.

## [2]. Catalog and loans stay separate domains
Date: 2026-09-30
Status: Decided
Context: Lend needs two feature domains that could become separate services later. Both use the same SQLite file, so the boundary has to live in the code.
Decision: Catalog owns writes to the tools table through lend/catalog.py. Loans will own members and loans. retire_tool may read loans only to refuse retiring a tool that is still out.
Alternatives considered: One module for tools and loans, rejected because Assignment 2 needs a seam to split. A status column on tools updated by both domains, rejected because a return and a catalog edit could disagree about whether the tool is available.
Consequences: lend/catalog.py does not create loans. The loans code can read whether a tool is retired, and it will change a tool only by calling a catalog function.