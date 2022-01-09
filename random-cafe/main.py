from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import Random

app = Flask(__name__)


def dump_to_json(cafe):
    return jsonify(id=cafe.id,
                   name=cafe.name,
                   map_url=cafe.map_url,
                   img_url=cafe.img_url,
                   location=cafe.location,
                   seats=cafe.seats,
                   has_toilet=cafe.has_toilet,
                   has_wifi=cafe.has_wifi,
                   has_sockets=cafe.has_sockets,
                   can_tak_calls=cafe.can_take_calls,
                   coffee_price=cafe.coffee_price)


##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        # Method 1.
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

        # Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


def from_json(form_data):
    cafe = Cafe()
    cafe.name = form_data.get("name")
    cafe.map_url = form_data.get("map_url")
    cafe.img_url = form_data.get("img_url")
    cafe.location = form_data.get("location")
    cafe.seats = form_data.get("seats")
    cafe.has_toilet = bool(form_data.get("has_toilet"))
    cafe.has_wifi = bool(form_data.get("has_wifi"))
    cafe.has_sockets = bool(form_data.get("has_sockets"))
    cafe.can_take_calls = bool(form_data.get("can_take_calls"))
    cafe.coffee_price = form_data.get("coffee_price")

    return cafe


@app.route("/")
def home():
    return render_template("index.html")


@app.get('/random')
def random():
    random_id = Random().randint(1, 21)  # the id range of current records is [1, 21]
    cafe = Cafe.query.get(random_id)
    result = dump_to_json(cafe)
    return result


## HTTP GET - Read Record
@app.get('/all')
def get_all_cafes():
    all_cafes = Cafe.query.all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


@app.get('/search')
def search():
    location = request.args['loc']
    cafe = Cafe.query.filter_by(location=location).first()
    if cafe:
        return cafe.to_dict()

    return {
        "error": {
            "Note Found": "Sorry, we don't have a cafe at that location."
        }
    }


## HTTP POST - Create Record
@app.post('/cafe')
def add_cafe():
    print(request.form)
    cafe = from_json(request.form)
    db.session.add(cafe)
    db.session.commit()

    return {
        "response": {
            "success": "Successfully added the new cafe."
        }
    }


## HTTP PUT/PATCH - Update Record

@app.patch('/update-price/<int:cafe_id>')
def update_price(cafe_id):
    new_price = request.args.get('new_price')
    cafe = Cafe.query.get(cafe_id)
    if not cafe:
        return {"error": {
            "Not Found": f"Sorry a cafe with that id of {cafe_id} was not found in the database."
        }}, 404

    cafe.coffee_price = new_price
    db.session.commit()
    return {"success": "Successfully updated the price."}, 202


## HTTP DELETE - Delete Record
@app.delete('/report-closed/<int:cafe_id>')
def delete(cafe_id):
    api_key = request.args.get("api-key")
    if api_key != 'TopSecretAPIKey':
        return {"error": "Sorry, that's not allowed. Make sure you have the correct api_key"}, 404

    cafe = Cafe.query.get(cafe_id)
    if not cafe:
        return {"error": {
            "Not Found": f"Sorry a cafe with that id of {cafe_id} was not found in the database."
        }}, 404
    db.session.delete(cafe)
    db.session.commit()

    return {"success": "Successfully deleted the cafe from the database."}, 200

if __name__ == '__main__':
    app.run(debug=True)
