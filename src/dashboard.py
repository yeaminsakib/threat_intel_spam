"""Flask dashboard entry point for the threat intel spam project."""
from __future__ import annotations

from pathlib import Path

try:
    from flask import Flask, jsonify
except ImportError:  # pragma: no cover - optional dependency for the scaffold
    Flask = None
    jsonify = None


BASE_DIR = Path(__file__).resolve().parents[1]


def create_app() -> Flask:
    """Create the Flask application."""

    if Flask is None:
        raise RuntimeError("Flask is not installed. Install requirements.txt first.")

    app = Flask(__name__)

    @app.get("/")
    def index() -> object:
        return jsonify(
            {
                "project": "threat_intel_spam",
                "status": "ok",
                "data_dir": str(BASE_DIR / "data"),
                "models_dir": str(BASE_DIR / "models"),
            }
        )

    return app


def main() -> None:
    """Run the development server."""

    app = create_app()
    app.run(debug=True)


if __name__ == "__main__":
    main()
