from flask_wtf import FlaskForm
from flask_ckeditor import CKEditorField
from wtforms.fields.choices import SelectField
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import StringField, URLField, SubmitField
from wtforms.validators import DataRequired, URL


class AddCafeForm(FlaskForm):
    name = StringField(label='Cafe name:', validators=[DataRequired(message='This field should contain email.')])
    map_url = URLField(label='Google map link:',
                       validators=[DataRequired(message='This field should contain a link to Google Maps.'), URL()])
    img_url = URLField(label='Image of cafe:',
                       validators=[DataRequired(message='This field should contain a link to the image of the cafe.'),
                                   URL()])
    location = StringField(label='Adress:', validators=[DataRequired(message='This field should contain an address.')])
    has_sockets = SelectField(label='How many sockets:',
                              choices=[('✘', '✘'), ('🔌', '🔌'), ('🔌🔌', '🔌🔌'), ('🔌🔌🔌', '🔌🔌🔌'), ('🔌🔌🔌🔌', '🔌🔌🔌🔌'),
                                       ('🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌')])
    has_wifi = SelectField(label='How strong WiFi-connection:',
                           choices=[('✘', '✘'), ('🛜', '🛜'), ('🛜🛜', '🛜🛜'), ('🛜🛜🛜', '🛜🛜🛜'), ('🛜🛜🛜🛜', '🛜🛜🛜🛜'),
                                    ('🛜🛜🛜🛜🛜', '🛜🛜🛜🛜🛜')])
    has_toilet = SelectField(label='If cafe has toilet:', choices=[('YES', 'YES'), ('NO', 'NO')],
                             validators=[DataRequired()])
    can_take_calls = SelectField(label='If cafe takes calls:', choices=[('YES', 'YES'), ('NO', 'NO')],
                                 validators=[DataRequired()])
    seats = SelectField(label='How many seats:',
                        choices=[('✘', '✘'), ('🪑', '🪑'), ('🪑🪑', '🪑🪑'), ('🪑🪑🪑', '🪑🪑🪑'), ('🪑🪑🪑🪑', '🪑🪑🪑🪑'),
                                 ('🪑🪑🪑🪑🪑', '🪑🪑🪑🪑🪑')])

    coffee_price = IntegerField(label='Coffee price:', validators=[DataRequired()])
    submit_button = SubmitField(label='Add cafe!')


class EditCafeForm(FlaskForm):
    map_url = URLField(label='Google map`s link:',
                       validators=[DataRequired(message='This field should contain a link to Google Maps.')])
    img_url = URLField(label='Image of cafe',
                       validators=[DataRequired(message='This field should contain a link to the image of the cafe.')])
    location = StringField(label='Adress:', validators=[DataRequired(message='This field should contain an address.')])
    has_sockets = SelectField(label='How many sockets:',
                              choices=[('✘', '✘'), ('🔌', '🔌'), ('🔌🔌', '🔌🔌'), ('🔌🔌🔌', '🔌🔌🔌'), ('🔌🔌🔌🔌', '🔌🔌🔌🔌'),
                                       ('🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌')])
    has_wifi = SelectField(label='How strong WiFi-connection:',
                           choices=[('✘', '✘'), ('🛜', '🛜'), ('🛜🛜', '🛜🛜'), ('🛜🛜🛜', '🛜🛜🛜'), ('🛜🛜🛜🛜', '🛜🛜🛜🛜'),
                                    ('🛜🛜🛜🛜🛜', '🛜🛜🛜🛜🛜')])
    has_toilet = SelectField(label='If cafe has toilet:', choices=[('YES', 'YES'), ('NO', 'NO')],
                             validators=[DataRequired()])
    can_take_calls = SelectField(label='If cafe takes calls:', choices=[('YES', 'YES'), ('NO', 'NO')],
                                 validators=[DataRequired()])
    seats = SelectField(label='How many seats:',
                        choices=[('✘', '✘'), ('🪑', '🪑'), ('🪑🪑', '🪑🪑'), ('🪑🪑🪑', '🪑🪑🪑'), ('🪑🪑🪑🪑', '🪑🪑🪑🪑'),
                                 ('🪑🪑🪑🪑🪑', '🪑🪑🪑🪑🪑')])

    coffee_price = StringField(label='Coffee price:', validators=[DataRequired()])
    submit_button = SubmitField(label='Edit cafe!')


class CommentForm(FlaskForm):
    autor = StringField(label='Author:', validators=[DataRequired()])
    text = CKEditorField(label='Comment:', validators=[DataRequired()])
    submit = SubmitField(label='Add comment!')
