"""PostgreSQL-backed integration test for notes flow."""

import os

import psycopg
import pytest

from app import create_app


@pytest.fixture()
def client_db():
    app = create_app({"TESTING": False})
    client = app.test_client()

    database_url = os.environ["DATABASE_URL"]
    with psycopg.connect(database_url, autocommit=True) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS notes (
                id SERIAL PRIMARY KEY,
                body TEXT NOT NULL
            );
            """
        )
        conn.execute("DELETE FROM notes;")

    yield client

    with psycopg.connect(database_url, autocommit=True) as conn:
        conn.execute("DELETE FROM notes;")


def test_create_and_delete_note_postgres_flow(client_db):
    add_response = client_db.post("/", data={"note": "integration test note"})
    assert add_response.status_code == 302

    page_after_add = client_db.get("/")
    assert b"integration test note" in page_after_add.data

    delete_response = client_db.post("/delete/0")
    assert delete_response.status_code == 302

    page_after_delete = client_db.get("/")
    assert b"integration test note" not in page_after_delete.data
