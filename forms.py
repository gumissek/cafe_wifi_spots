from flask_wtf import FlaskForm
from flask_ckeditor import CKEditorField
from wtforms.fields.simple import StringField, URLField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class AddCafeForm(FlaskForm):
    name = StringField(label='Cafe name:',validators=[DataRequired(message='To pole powinno zawierac email.')])
    map_url = StringField(label='Google map`s link:',validators=[DataRequired(message='To pole powinno zawierac, link do map googla')])
    img_url = StringField(label='Image of cafe',validators=[DataRequired(message='To pole powinno zawierac link do obrazka kawiarni')])
    location = StringField(label='Adress:',validators=[DataRequired(message='To pole powinno zawierac adres')])
    has_sockets = StringField(label='If cafe has sockets:',validators=[DataRequired()])
    has_wifi = StringField(label='If cafe has wifi:',validators=[DataRequired()])
    has_toilet = StringField(label='If cafe has toilet:',validators=[DataRequired()])
    can_take_calls = StringField(label='If cafe takes calls:',validators=[DataRequired()])
    seats = StringField(label='Seats:',validators=[DataRequired()])
    coffee_price = StringField(label='Coffee price:',validators=[DataRequired()])
    submit_button = SubmitField(label='Add cafe')

class EditCafeForm(FlaskForm):
    map_url = StringField(label='New Google map`s link:',
                          validators=[DataRequired(message='To pole powinno zawierac, link do map googla')])
    img_url = StringField(label='New Image of cafe',
                          validators=[DataRequired(message='To pole powinno zawierac link do obrazka kawiarni')])
    location = StringField(label='New Adress:', validators=[DataRequired(message='To pole powinno zawierac adres')])
    has_sockets = StringField(label='New If cafe has sockets:', validators=[DataRequired()])
    has_wifi = StringField(label='New If cafe has wifi:', validators=[DataRequired()])
    has_toilet = StringField(label='New If cafe has toilet:', validators=[DataRequired()])
    can_take_calls = StringField(label='New If cafe takes calls:', validators=[DataRequired()])
    seats = StringField(label='New Seats:', validators=[DataRequired()])
    coffee_price = StringField(label='New Coffee price:', validators=[DataRequired()])
    submit_button = SubmitField(label='Edit cafe')

class CommentForm(FlaskForm):
    autor = StringField(label='Podaj autora',validators=[DataRequired()])
    text= CKEditorField(label='Dodaj komentarz',validators=[DataRequired()])
    submit = SubmitField(label='Dodaj komentarz')