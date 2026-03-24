"""Routes blueprint."""

import time

import psycopg
from flask import Blueprint, current_app, redirect, render_template, request, url_for

bp = Blueprint("main", __name__)

_db_initialized = False

_CREATE_NOTES_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS notes (
    id SERIAL PRIMARY KEY,
    body TEXT NOT NULL
);
"""


def _get_db_url() -> str:
    return current_app.config["DATABASE_URL"]


def _connect():
    # autocommit keeps setup (CREATE TABLE) simple for beginners.
    return psycopg.connect(_get_db_url(), autocommit=True)


def _ensure_db_initialized() -> bool:
    global _db_initialized
    if _db_initialized:
        return True

    # Keep tests beginner-friendly: if Postgres isn't running, the home page can still load.
    if current_app.config.get("TESTING"):
        return False

    attempts = int(current_app.config.get("DB_INIT_ATTEMPTS", 20))
    delay_seconds = float(current_app.config.get("DB_INIT_DELAY_SECONDS", 0.5))

    for _ in range(attempts):
        try:
            with _connect() as conn:
                with conn.cursor() as cur:
                    cur.execute(_CREATE_NOTES_TABLE_SQL)
            _db_initialized = True
            return True
        except psycopg.OperationalError:
            time.sleep(delay_seconds)

    return False


@bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if not current_app.config.get("TESTING"):
            text = request.form.get("note", "").strip()
            if text and _ensure_db_initialized():
                with _connect() as conn:
                    with conn.cursor() as cur:
                        cur.execute(
                            "INSERT INTO notes (body) VALUES (%s);",
                            (text,),
                        )
        return redirect(url_for("main.index"))

    # Newest notes first for the "Recent notes" list.
    if not _ensure_db_initialized():
        notes: list[str] = []
    else:
        with _connect() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT body FROM notes ORDER BY id DESC;")
                notes = [row[0] for row in cur.fetchall()]

    return render_template("index.html", notes=notes)


@bp.route("/delete/<int:note_index>", methods=["POST"])
def delete_note(note_index: int):
    if _ensure_db_initialized():
        with _connect() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id FROM notes ORDER BY id DESC;")
                note_ids = [row[0] for row in cur.fetchall()]
                if 0 <= note_index < len(note_ids):
                    cur.execute("DELETE FROM notes WHERE id = %s;", (note_ids[note_index],))

    return redirect(url_for("main.index"))
