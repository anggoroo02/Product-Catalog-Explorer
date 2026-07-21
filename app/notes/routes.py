from flask import render_template

from flask_login import login_required

from app.notes import notes_bp


@notes_bp.route("")
@login_required
def index():

    return render_template(
        "notes/index.html"
    )