from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route('/random', methods=['GET', 'POST'])
def get_random_cafe():
    """return a random café from the café database"""
    with app.app_context():
        result = db.session.execute(db.select(Cafe).order_by(Cafe.id))
        all_cafes = result.scalars().fetchall()
        chosen_cafe = random.choice(all_cafes)

        x = {
            'id': chosen_cafe.id,
            'name': chosen_cafe.name,
            'map_url': chosen_cafe.map_url,
            'img_url': chosen_cafe.img_url,
            'location': chosen_cafe.location,
            'seats': chosen_cafe.seats,
            'has_toilet': chosen_cafe.has_toilet,
            'has_wifi': chosen_cafe.has_wifi,
            'has_sockets': chosen_cafe.has_sockets,
            'can_take_calls': chosen_cafe.can_take_calls,
            'coffee_price': chosen_cafe.coffee_price
        }
    return jsonify(cafe=x), 200


@app.route('/all')
def get_all_cafes():
    """return all available café from the café database"""
    with app.app_context():
        result = db.session.execute(db.select(Cafe).order_by(Cafe.id))
        cafes = result.scalars().fetchall()

        all_cafes = [{
            'id': cafe.id,
            'name': cafe.name,
            'map_url': cafe.map_url,
            'img_url': cafe.img_url,
            'location': cafe.location,
            'seats': cafe.seats,
            'has_toilet': cafe.has_toilet,
            'has_wifi': cafe.has_wifi,
            'has_sockets': cafe.has_sockets,
            'can_take_calls': cafe.can_take_calls,
            'coffee_price': cafe.coffee_price
        } for cafe in cafes]

        return jsonify(cafes=all_cafes), 200


@app.route('/search')
def search():
    """given a location parameter during call, searches the database for a café/cafés with
    location that matches the given location"""
    loc = request.args.get('loc').title()

    # querying the database for café/cafés with the location same as loc
    result = db.session.execute(db.select(Cafe).where(Cafe.location == loc)).scalars()
    searched_cafes = result.fetchall()

    if not searched_cafes:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404

    cafes = [{
        'id': cafe.id,
        'name': cafe.name,
        'map_url': cafe.map_url,
        'img_url': cafe.img_url,
        'location': cafe.location,
        'seats': cafe.seats,
        'has_toilet': cafe.has_toilet,
        'has_wifi': cafe.has_wifi,
        'has_sockets': cafe.has_sockets,
        'can_take_calls': cafe.can_take_calls,
        'coffee_price': cafe.coffee_price
    } for cafe in searched_cafes]
    return jsonify(cafes=cafes), 200


# HTTP POST - Create Record
@app.route('/add', methods=['POST'])
def add():
    """create and add a café to the database"""
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."}), 200


# HTTP PUT/PATCH - Update Record
@app.route('/update-price/<int:cafe_id>', methods=['PATCH'])
def update_price(cafe_id):
    """update an already existing cafe's price"""
    cafe = db.session.get(Cafe, cafe_id)
    if cafe:
        cafe.coffee_price = request.args.get('new_price')
        db.session.commit()
        return jsonify(response={"success": "Price successfully Updated"}), 200
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database"}), 404


# HTTP DELETE - Delete Record
@app.route('/report-closed/<int:cafe_id>', methods=['DELETE'])
def delete_cafe(cafe_id):
    """deletes a cafe"""
    if request.args.get('api_key') == 'TopSecretAPIKey':
        cafe_to_delete = db.session.get(Cafe, cafe_id)
        if cafe_to_delete:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(response={"success": "Cafe successfully deleted"}), 200
        else:
            return jsonify(error={"Not Found": "Sorry, a cafe with that id was not found in the database"}), 404
    else:
        return jsonify({"error": "Sorry, that's not allowed. Make sure you have the correct api key"}), 403


if __name__ == '__main__':
    app.run(debug=True)
