"""Routes blueprint."""

from flask import Blueprint, redirect, render_template, request, url_for

bp = Blueprint("main", __name__)

# In-memory storage for this process only (cleared when the server restarts).
_notes: list[str] = []


def reset_notes() -> None:
    """Clear stored notes (used by the test suite)."""
    _notes.clear()


@bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("note", "").strip()
        if text:
            _notes.append(text)
        return redirect(url_for("main.index"))

    # Newest notes first for the "Recent notes" list.
    return render_template("index.html", notes=list(reversed(_notes)))
