# notes-cicd-app

A minimal Flask notes application using the app factory pattern and a single blueprint.

## Setup

Create and activate a virtual environment, then install dependencies:

```bash
pip install -r requirements.txt
```

## Run locally

```bash
python run.py
```

Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

## Run tests

Uses the standard library only:

```bash
python -m unittest discover -s tests -p "test_*.py"
```

## Layout

- `app/` — application package (`create_app`, blueprint routes)
- `templates/` — Jinja2 templates
- `static/` — CSS, JS, images
- `tests/` — unit tests (expand as you add features)

Database integration can be wired in `create_app` later (for example with Flask-SQLAlchemy).
