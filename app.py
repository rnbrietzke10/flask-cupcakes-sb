"""Flask app for Cupcakes"""
import os
from flask import Flask, request, render_template, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = os.urandom(24)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def index_page():
    return render_template("index.html")


@app.route('/api/cupcakes')
def get_all_cupcakes():
    cupcakes =[ cupcake.serialize() for cupcake in Cupcake.query.all()]

    return jsonify(cupcakes=cupcakes)


@app.route('/api/cupcakes/<int:id>')
def get_cupcake(id):
    """Returns JSON for specified cupcake """
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake():
    """Creates new instance of Cupcake, saves it to the database and returns JSON of the created cupcake"""
    img = request.json.get("image", "https://tinyurl.com/demo-cupcake")
    new_cupcake = Cupcake(flavor=request.json["flavor"], size= request.json["size"], rating=request.json["rating"], image=img)
    db.session.add(new_cupcake)
    db.session.commit()
    response_json = jsonify(cupcake=new_cupcake.serialize())

    return (response_json, 201)


@app.route('/api/cupcakes/<int:id>', methods=["PATCH"])
def update_cupcake(id):
    """Updates the specified cupcake instance and returns JSON with the newly updated cupcake info"""
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json.get("flavor", cupcake.flavor)
    cupcake.size = request.json.get("size", cupcake.size)
    cupcake.rating = request.json.get("rating", cupcake.rating)
    cupcake.image = request.json.get("image", cupcake.image)

    db.session.commit()

    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes/<int:id>', methods=["DELETE"])
def delete_cupcake(id):
    """Deletes specified cupcake"""
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="Deleted")
