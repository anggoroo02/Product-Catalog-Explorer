from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, NumberRange


class NoteForm(FlaskForm):
    title = StringField(
        "Judul",
        validators=[
            DataRequired(),
            Length(max=100)
        ]
    )

    content = TextAreaField(
        "Catatan",
        validators=[
            DataRequired()
        ]
    )

    submit = SubmitField("Simpan Note")


class CreateNoteForm(NoteForm):
    product_id = IntegerField(
        "Product ID",
        validators=[
            DataRequired(),
            NumberRange(min=1)
        ]
    )
