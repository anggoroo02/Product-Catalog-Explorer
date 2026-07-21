from app.extensions import db
from app.models import Note

def get_user_notes(user_id):

    return (
        Note.query
        .filter_by(user_id=user_id)
        .order_by(Note.updated_at.desc())
        .all()
    )

def get_product_notes(user_id, product_id):

    return (
        Note.query
        .filter_by(
            user_id=user_id,
            product_id=product_id
        )
        .order_by(Note.updated_at.desc())
        .all()
    )

def get_note(user_id, note_id):

    return Note.query.filter_by(
        id=note_id,
        user_id=user_id
    ).first()

def create_note(
    user_id,
    product_id,
    title,
    content
):

    note = Note(
        user_id=user_id,
        product_id=product_id,
        title=title,
        content=content
    )

    db.session.add(note)
    db.session.commit()

    return note

def update_note(
    user_id,
    note_id,
    title,
    content
):

    note = get_note(
        user_id,
        note_id
    )

    if note is None:
        return None

    note.title = title
    note.content = content

    db.session.commit()

    return note

def delete_note(
    user_id,
    note_id
):

    note = get_note(
        user_id,
        note_id
    )

    if note is None:
        return False

    db.session.delete(note)
    db.session.commit()

    return True