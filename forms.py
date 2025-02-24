from flask_wtf import FlaskForm
from flask_ckeditor import CKEditorField
from wtforms.fields.choices import SelectField
from wtforms.fields.simple import StringField, URLField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class AddCafeForm(FlaskForm):
    name = StringField(label='Cafe name:', validators=[DataRequired(message='To pole powinno zawierac email.')])
    map_url = StringField(label='Google map`s link:',
                          validators=[DataRequired(message='To pole powinno zawierac, link do map googla')])
    img_url = StringField(label='Image of cafe',
                          validators=[DataRequired(message='To pole powinno zawierac link do obrazka kawiarni')])
    location = StringField(label='Adress:', validators=[DataRequired(message='To pole powinno zawierac adres')])
    has_sockets = SelectField(label='How many sockets:',
                              choices=[('X', 'X'), ('🔌', '🔌'), ('🔌🔌', '🔌🔌'), ('🔌🔌🔌', '🔌🔌🔌'), ('🔌🔌🔌🔌', '🔌🔌🔌🔌'),
                                       ('🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌')])
    has_wifi = SelectField(label='How strong WiFi-connection:',
                           choices=[('X', 'X'), ('🛜', '🛜'), ('🛜🛜', '🛜🛜'), ('🛜🛜🛜', '🛜🛜🛜'), ('🛜🛜🛜🛜', '🛜🛜🛜🛜'),
                                    ('🛜🛜🛜🛜🛜', '🛜🛜🛜🛜🛜')])
    has_toilet = SelectField(label='If cafe has toilet:', choices=[('YES', 'YES'), ('NO', 'NO')],
                             validators=[DataRequired()])
    can_take_calls = SelectField(label='If cafe takes calls:', choices=[('YES', 'YES'), ('NO', 'NO')],
                                 validators=[DataRequired()])
    seats = SelectField(label='How many seats:',
                        choices=[('X', 'X'), ('🪑', '🪑'), ('🪑🪑', '🪑🪑'), ('🪑🪑🪑', '🪑🪑🪑'), ('🪑🪑🪑🪑', '🪑🪑🪑🪑'),
                                 ('🪑🪑🪑🪑🪑', '🪑🪑🪑🪑🪑')])

    coffee_price = StringField(label='Coffee price:', validators=[DataRequired()])
    submit_button = SubmitField(label='Add cafe')


class EditCafeForm(FlaskForm):
    map_url = StringField(label='Google map`s link:',
                          validators=[DataRequired(message='To pole powinno zawierac, link do map googla')])
    img_url = StringField(label='Image of cafe',
                          validators=[DataRequired(message='To pole powinno zawierac link do obrazka kawiarni')])
    location = StringField(label='Adress:', validators=[DataRequired(message='To pole powinno zawierac adres')])
    has_sockets = SelectField(label='How many sockets:',
                              choices=[('X', 'X'), ('🔌', '🔌'), ('🔌🔌', '🔌🔌'), ('🔌🔌🔌', '🔌🔌🔌'), ('🔌🔌🔌🔌', '🔌🔌🔌🔌'),
                                       ('🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌')])
    has_wifi = SelectField(label='How strong WiFi-connection:',
                           choices=[('X', 'X'), ('🛜', '🛜'), ('🛜🛜', '🛜🛜'), ('🛜🛜🛜', '🛜🛜🛜'), ('🛜🛜🛜🛜', '🛜🛜🛜🛜'),
                                    ('🛜🛜🛜🛜🛜', '🛜🛜🛜🛜🛜')])
    has_toilet = SelectField(label='If cafe has toilet:', choices=[('YES', 'YES'), ('NO', 'NO')],
                             validators=[DataRequired()])
    can_take_calls = SelectField(label='If cafe takes calls:', choices=[('YES', 'YES'), ('NO', 'NO')],
                                 validators=[DataRequired()])
    seats = SelectField(label='How many seats:',
                        choices=[('X', 'X'), ('🪑', '🪑'), ('🪑🪑', '🪑🪑'), ('🪑🪑🪑', '🪑🪑🪑'), ('🪑🪑🪑🪑', '🪑🪑🪑🪑'),
                                 ('🪑🪑🪑🪑🪑', '🪑🪑🪑🪑🪑')])

    coffee_price = StringField(label='Coffee price:', validators=[DataRequired()])
    submit_button = SubmitField(label='Edit cafe')


class CommentForm(FlaskForm):
    autor = StringField(label='Podaj autora', validators=[DataRequired()])
    text = CKEditorField(label='Dodaj komentarz', validators=[DataRequired()])
    submit = SubmitField(label='Dodaj komentarz')
