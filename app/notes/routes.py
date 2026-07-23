from flask import (
    flash,
    redirect,
    render_template,
    url_for
)

from flask_login import current_user, login_required

from app.notes import notes_bp
from app.notes.forms import CreateNoteForm, NoteForm
from app.services import product_service
from app.services.note_service import (
    create_note,
    delete_note,
    get_note,
    get_user_notes,
    update_note
)


def _get_product_titles(notes):
    product_titles = {}

    for note in notes:
        if note.product_id in product_titles:
            continue

        product = product_service.get_product_by_id(
            note.product_id
        )

        product_titles[note.product_id] = (
            product["title"]
            if product is not None
            else "Produk tidak tersedia"
        )

    return product_titles


@notes_bp.route("")
@login_required
def index():
    form = CreateNoteForm()
    notes = get_user_notes(current_user.id)
    product_titles = _get_product_titles(notes)

    return render_template(
        "notes/index.html",
        form=form,
        notes=notes,
        product_titles=product_titles
    )


@notes_bp.route("/add", methods=["POST"])
@login_required
def add():
    form = CreateNoteForm()

    if form.validate_on_submit():
        create_note(
            current_user.id,
            form.product_id.data,
            form.title.data,
            form.content.data
        )

        flash("Note berhasil ditambahkan.", "success")
        return redirect(
            url_for(
                "products.detail",
                product_id=form.product_id.data
            )
        )

    flash("Data note tidak valid.", "danger")
    notes = get_user_notes(current_user.id)
    product_titles = _get_product_titles(notes)

    return render_template(
        "notes/index.html",
        form=form,
        notes=notes,
        product_titles=product_titles
    )


@notes_bp.route("/<int:note_id>/edit", methods=["GET", "POST"])
@login_required
def edit(note_id):
    note = get_note(current_user.id, note_id)

    if note is None:
        flash("Note tidak ditemukan.", "danger")
        return redirect(url_for("notes.index"))

    form = NoteForm(obj=note)

    if form.validate_on_submit():
        updated_note = update_note(
            current_user.id,
            note_id,
            form.title.data,
            form.content.data
        )

        if updated_note is None:
            flash("Note tidak ditemukan.", "danger")
            return redirect(url_for("notes.index"))
        else:
            flash("Note berhasil diperbarui.", "success")

        return redirect(
            url_for(
                "products.detail",
                product_id=note.product_id
            )
        )

    return render_template(
        "notes/edit.html",
        form=form,
        note=note,
        product_title=_get_product_titles([note])[note.product_id]
    )


@notes_bp.route("/<int:note_id>/delete", methods=["POST"])
@login_required
def delete(note_id):
    note = get_note(current_user.id, note_id)

    if note is None:
        flash("Note tidak ditemukan.", "danger")
        return redirect(url_for("notes.index"))

    success = delete_note(current_user.id, note_id)

    if success:
        flash("Note berhasil dihapus.", "success")
    else:
        flash("Note tidak ditemukan.", "danger")

    return redirect(
        url_for(
            "products.detail",
            product_id=note.product_id
        )
    )
