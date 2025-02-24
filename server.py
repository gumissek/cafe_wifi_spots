import os
from flask import Flask, render_template, request, url_for
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Boolean, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from werkzeug.utils import redirect
from flask_ckeditor import CKEditor

from forms import AddCafeForm, EditCafeForm , CommentForm

# todo zmienic wszystko na zmienne srodowiskowe
FLASK_KEY = 's123312344adasda'
DATABASE_URI = ''

app = Flask(__name__)
app.config['SECRET_KEY'] = FLASK_KEY
bootstrap = Bootstrap5(app)
ckeditor=CKEditor(app)



# BAZA DANYCH
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///cafe.db')
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# TABELE
class Cafe(db.Model):
    __tablename__ = 'cafes'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    has_sockets: Mapped[str] = mapped_column(String(250), nullable=False)
    has_wifi: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[str] = mapped_column(String(250), nullable=False)
    can_take_calls: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=False)

    comments = relationship('Comment', back_populates='cafe')


class Comment(db.Model):
    __tablename__ = 'comments'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)

    cafe = relationship('Cafe', back_populates='comments')
    cafe_id: Mapped[int] = mapped_column(Integer, db.ForeignKey('cafes.id'))

with app.app_context():
    db.create_all()


@app.route('/', methods=['POST', 'GET'])
def home():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    if all_cafes:
        return render_template('index.html', all_cafes=all_cafes)
    else:
        return render_template('blad.html')


@app.route('/cafe/<int:cafe_id>', methods=['POST', 'GET'])
def show_cafe(cafe_id):
    commentform=CommentForm()
    requested_cafe = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
    return render_template('show_cafe.html', cafe=requested_cafe,comment_form=commentform)


@app.route('/addcafe', methods=['POST', 'GET'])
def add_cafe():
    add_form = AddCafeForm()
    if add_form.validate_on_submit():
        cafe_name = request.form['name']
        cafe_map_url = request.form['map_url']
        cafe_img_url = request.form['img_url']
        cafe_location = request.form['location']
        cafe_has_sockets = request.form['has_sockets']
        cafe_has_wifi = request.form['has_wifi']
        cafe_has_toilet = request.form['has_toilet']
        cafe_can_take_calls = request.form['can_take_calls']
        cafe_seats = request.form['seats']
        cafe_coffe_price = request.form['coffee_price']
        new_cafe = Cafe(name=cafe_name,
                        map_url=cafe_map_url,
                        img_url=cafe_img_url,
                        location=cafe_location,
                        has_sockets=cafe_has_sockets,
                        has_wifi=cafe_has_wifi,
                        has_toilet=cafe_has_toilet,
                        can_take_calls=cafe_can_take_calls,
                        seats=cafe_seats,
                        coffee_price=cafe_coffe_price)
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_cafe.html', form=add_form)


@app.route('/edit/<int:cafe_id>', methods=['POST', 'GET'])
def edit_cafe(cafe_id):

    requested_cafe = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
    editform = EditCafeForm(map_url=requested_cafe.map_url, img_url=requested_cafe.img_url,
                            location=requested_cafe.location, has_sockets=requested_cafe.has_sockets,
                            has_wifi=requested_cafe.has_wifi, has_toilet=requested_cafe.has_toilet,
                            can_take_calls=requested_cafe.can_take_calls, seats=requested_cafe.seats,
                            coffee_price=requested_cafe.coffee_price)
    if editform.validate_on_submit():
        requested_cafe.map_url = request.form['map_url']
        requested_cafe.img_url = request.form['img_url']
        requested_cafe.location = request.form['location']
        requested_cafe.has_sockets = request.form['has_sockets']
        requested_cafe.has_wifi = request.form['has_wifi']
        requested_cafe.has_toilet = request.form['has_toilet']
        requested_cafe.can_take_calls = request.form['can_take_calls']
        requested_cafe.seats = request.form['seats']
        requested_cafe.coffee_price = request.form['coffee_price']
        db.session.commit()
        return redirect(url_for('show_cafe',cafe_id=cafe_id))
    return render_template('edit_cafe.html', form=editform, cafe=requested_cafe)


if __name__ == '__main__':
    app.run(debug=True, port=5001)

# TODO zrobic strone flask ok
# TODO zrobic zmienne srodowiskowe
# TODO zrobic zrobic tabele i poloczanie z baza danych ok
# TODO zrobic strone glowna ktora wyswietla wszystkie rzeczy z bazy danych ok
# todo zrobic formularz do dodawania kawiarni ok
# todo zrobic formularz edytowania kawiarni ok
# todo zrobic
# todo zrobic funkcjonalosc ktora dodaje punkty
# TODO zrobic api tak zeby kazdy mogl modyfikowac ta liste i dokumentacje do tego
