# notes-cicd-app

Small Flask learning project: app factory, one blueprint, and a simple notes-style homepage. No database or authentication yet.

## Prerequisites

- Python 3.10+ (3.11+ recommended)
- A virtual environment (see below)

## Setup

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
python run.py
```

Then open [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Tests

```bash
pytest
```

## Project layout

| Path | Purpose |
|------|---------|
| `app/` | Application package (`create_app`, routes blueprint) |
| `templates/` | Jinja templates |
| `static/` | CSS and other static assets |
| `tests/` | Unit tests |
| `run.py` | Local development entry point |

`instance/` (Flask) and local `.env` files are ignored by Git and are intended for later configuration and data.
