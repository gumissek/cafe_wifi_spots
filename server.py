import os

from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Boolean, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

# todo zmienic wszystko na zmienne srodowiskowe
FLASK_KEY = 's123312344adasda'
DATABASE_URI = ''

app = Flask(__name__)
app.config['SECRET_KEY'] = FLASK_KEY
bootstrap = Bootstrap5(app)


# BAZA DANYCH
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///cafe.db')
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# TABELE
class Cafe(db.Model):
    __tablename__ = 'cafes'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
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
    all_cafes=db.session.execute(db.select(Cafe)).scalars().all()
    if all_cafes:
        return render_template('index.html',all_cafes=all_cafes)
    else:
        return render_template('blad.html')


@app.route('/cafe/<int:cafe_id>',methods=['POST','GET'])
def show_cafe(cafe_id):
    requested_cafe=db.session.execute(db.select(Cafe).where(Cafe.id==cafe_id)).scalar()
    print(requested_cafe.id)
    print(requested_cafe.location)
    return render_template('show_cafe.html',cafe=requested_cafe)




if __name__ == '__main__':
    app.run(debug=True, port=5001)

# TODO zrobic strone flask ok
# TODO zrobic zmienne srodowiskowe
# TODO zrobic zrobic tabele i poloczanie z baza danych ok
# TODO zrobic strone glowna ktora wyswietla wszystkie rzeczy z bazy danych ok
# todo zrobic formularz do dodawania kawiarni
# todo zrobic
# todo zrobic funkcjonalosc ktora dodaje punkty
# TODO zrobic api tak zeby kazdy mogl modyfikowac ta liste i dokumentacje do tego
