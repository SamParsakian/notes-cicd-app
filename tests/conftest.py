"""Shared pytest fixtures for the Flask app."""

import pytest

from app import create_app
from app.routes import reset_notes


@pytest.fixture(autouse=True)
def _empty_notes():
    """Start each test with an empty in-memory note list."""
    reset_notes()
    yield


@pytest.fixture()
def flask_app():
    return create_app({"TESTING": True})


@pytest.fixture()
def client(flask_app):
    return flask_app.test_client()
