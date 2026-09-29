## [1]. Backend language and framework
Date: 2026-09-30
Status: Decided
Context: Lend is one process with server-rendered pages and a single SQLite file. Startup has to be one command, bound to 0.0.0.0, configured only through PORT and DATA_DIR. Every layer of this app has to be explainable on paper.
Decision: Use Python with Flask, Jinja templates, and the standard-library sqlite3 module.
Alternatives considered: Django, rejected because its ORM, admin, and auth would sit unused on two small domains. FastAPI, rejected because the interface is HTML forms, so Flask's built-in template rendering is the smaller fit.
Consequences: Runtime dependencies stay at Flask. SQL stays visible in lend/db.py, and there is no second frontend process to deploy in Assignment 2.