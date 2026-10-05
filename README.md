# Lend

A one-desk tool library for a volunteer workshop.

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000

The home page shows the SQLite path and the row counts for tools, members, and loans. `/tools` adds a tool, lists tools, and retires a tool when it has no open loan. `/loans` registers a member and lends an available tool for 7 days. The process binds to `0.0.0.0`. `PORT` defaults to `5000`. The SQLite file is `$DATA_DIR/lend.db`, and `DATA_DIR` defaults to `data`. Both variables are optional.

```bash
PORT=8000 DATA_DIR=/tmp/lend python app.py
```

## Tests

Coverage is added with the catalog and loan rules. The command will be:

```bash
pytest --cov=lend --cov-report=term-missing
```
