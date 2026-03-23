"""Shared pytest fixtures for the Flask app."""

import pytest

from app import create_app


@pytest.fixture()
def flask_application():
    return create_app({"TESTING": True})


@pytest.fixture()
def client(flask_application):
    return flask_application.test_client()
