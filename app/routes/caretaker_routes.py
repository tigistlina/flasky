from flask import Blueprint, jsonify, abort, make_response, request
from app.models.caretaker import Caretaker
from app.models.cat import Cat
from app import db
from app.helpers import validate_model

caretaker_bp = Blueprint("caretaker_bp", __name__, url_prefix="/caretakers")

@caretaker_bp.route("", methods=["POST"])
def create_caretaker():
    request_body = request.get_json()
    try:
        new_caretaker = Caretaker.from_dict(request_body)

        db.session.add(new_caretaker)
        db.session.commit()
        return make_response(jsonify(f"Caretaker {new_caretaker.name} successfully created"), 201)
    except KeyError as e:
        abort(make_response({"message": f"missing required value: {e}"}, 400))

@caretaker_bp.route("", methods=["GET"])
def read_all_caretaker():
    caretakers = Caretaker.query.all()

    caretakers_response = [caretaker.to_dict() for caretaker in caretakers]

    return jsonify(caretakers_response)

# POST /caretakers/1/cats
@caretaker_bp.route("<caretaker_id>/cats", methods=["POST"])
def create_cat(caretaker_id):
    caretaker = validate_model(Caretaker, caretaker_id)
    request_body = request.get_json()
    try:
        new_cat = Cat.from_dict(request_body)
        new_cat.caretaker = caretaker

        db.session.add(new_cat)
        db.session.commit()

        return make_response(jsonify(f"Cat {new_cat.name} cared by {caretaker.name} successfully created"), 201)
    except KeyError as e:
        abort(make_response({"message": f"missing required value: {e}"}, 400))

# GET /caretakers/1/cats
@caretaker_bp.route("<caretaker_id>/cats", methods=["GET"])
def read_cats(caretaker_id):
    caretaker = validate_model(Caretaker, caretaker_id)

    cats_response = []
    for cat in caretaker.cats:
        cats_response.append(cat.to_dict())

    return(jsonify(cats_response))