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

The home page shows how many tools are free, out, and overdue, plus the three steps for adding a tool, adding a member, and lending for 7 days. `/tools` adds a tool, lists tools as available, out, or retired, and retires a tool when it has no open loan. `/loans` registers a member, lends an available tool for 7 days, marks a return, and shows Overdue when an open loan is past its due date. `/loans/history` lists returned loans and can repeat one for another 7 days. The process binds to `0.0.0.0`. `PORT` defaults to `5000`. The SQLite file is `$DATA_DIR/lend.db`, and `DATA_DIR` defaults to `data`. Both variables are optional.

```bash
PORT=8000 DATA_DIR=/tmp/lend python app.py
```

## Tests

Core catalog and loan rules are covered at 96%.

```bash
pytest --cov=lend.catalog --cov=lend.loans --cov-report=term-missing
```

The command covers `lend/catalog.py` and `lend/loans.py`. Route functions in `app.py` are outside that measurement.
