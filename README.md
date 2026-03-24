# notes-cicd-app

## Project overview

`notes-cicd-app` is a beginner-friendly Flask notes app built as a CI/CD portfolio project.

It is intentionally simple: create and delete notes in a web UI, store data in PostgreSQL, run with Docker Compose, test with GitHub Actions CI, and deploy to a Hetzner VPS with GitHub Actions CD over SSH.

## Features

- Add note
- Delete note
- Notes stored in PostgreSQL
- Dockerized app
- CI with GitHub Actions
- CD deployment to Hetzner VPS

## Architecture at a glance

- **Flask app**: serves routes and HTML pages.
- **PostgreSQL**: stores notes in the `notes` table.
- **Docker Compose**: runs `app` and `db` services together locally/on server.
- **GitHub Actions**:
  - CI runs tests on push and pull request.
  - CD deploys on push to `main`.
- **VPS deployment flow**: GitHub Actions SSH -> pull latest code on VPS -> restart with Docker Compose.

## Run locally with Docker Compose

```bash
docker compose up --build -d
```

Open: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

To stop:

```bash
docker compose down
```

## Optional local run without Docker

This is still valid if you have Python and PostgreSQL available locally.

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

## Environment variables

- `DATABASE_URL`: PostgreSQL connection string used by Flask.
  - Example (Docker Compose): `postgresql://notes:notes@db:5432/notes`
  - Example (local host): `postgresql://notes:notes@localhost:5432/notes`

If `DATABASE_URL` is not set, the app uses a default local Postgres URL.

## Run tests

```bash
pytest
```

Tests are also run automatically in GitHub Actions CI.

## CI/CD flow

- **Push / Pull Request** -> GitHub Actions CI runs tests.
- **Merge/Push to `main`** -> GitHub Actions CD deploys to Hetzner VPS over SSH.

## Repository structure

- `app/` - Flask app factory and routes
- `templates/` - Jinja HTML templates
- `static/` - CSS
- `tests/` - pytest tests (including PostgreSQL integration test)
- `.github/workflows/ci.yml` - CI workflow
- `.github/workflows/deploy.yml` - CD workflow
- `Dockerfile` - app image build
- `docker-compose.yml` - app + PostgreSQL services
- `run.py` - local entry point

## Known limitations / next steps

- Uses Flask development server (not a production WSGI server yet)
- No HTTPS/domain setup yet
- No database migrations yet
- No authentication/authorization yet
