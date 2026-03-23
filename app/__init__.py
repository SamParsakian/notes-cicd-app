"""Application factory for notes-cicd-app."""

import os
from pathlib import Path

from flask import Flask


def create_app(test_config=None):
    """Create and configure the Flask application."""
    base_dir = Path(__file__).resolve().parent.parent
    app = Flask(
        __name__,
        template_folder=str(base_dir / "templates"),
        static_folder=str(base_dir / "static"),
    )
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE_URL=os.getenv(
            "DATABASE_URL",
            "postgresql://notes:notes@localhost:5432/notes",
        ),
    )
    if test_config is not None:
        app.config.from_mapping(test_config)

    from app.routes import bp

    app.register_blueprint(bp)

    return app
