"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Account, People, Planet, Species, Vehicles, Favorites
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from argon2 import PasswordHasher


ph = PasswordHasher()
api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200


@api.route('/register', methods=['POST'])
def register():
    payload = request.get_json()
    print(ph.hash(payload['password']))

    user = User(
        email=payload['email'],
        password=ph.hash(payload['password']),
        is_active=True
    )

    db.session.add(user)
    db.session.commit()

    return "user registered", 200
# ____________________________________________________________________


@api.route('/login', methods=['POST'])
def login():
    payload = request.get_json()

    user = User.query.filter(User.email == payload['email']).first()
    if user is None:
        return 'failed-auth', 401
        # return 'user not found', 401
    # hash = ph.hash(payload['password'])
    # print(user.password)
    # print(hash)

    try:
        ph.verify(user.password, payload['password'])
        # ph.verify(user.password, ph.hash(payload['password']))

    except:
        # print(user.password)
        # print(hash)
        # return 'incorrect password', 401
        return 'failed-auth', 401

    token = create_access_token(identity=user.id)

    return jsonify({'token': token})

# ____________________________________________________________________


@ api.route('/accounts', methods=['GET'])
@ jwt_required()
def accounts():
    user_id = get_jwt_identity()

    user = User.query.get(user_id)
    accounts = Account.query.filter(Account.user_id == user_id).all()

    account_info = {
        "accounts": [x.serialize() for x in accounts],
        "user": user.serialize()
    }

    return jsonify(account_info)


@api.route('/account/<int:id>', methods=['DELETE'])
def del_account(id):
    account_data = Account.query.filter_by(id=id).delete()
    db.session.commit()

    return 'Account deleted', 204


# ____________________________________________________________________


@api.route('/people', methods=['GET'])
def people():

    people_data = People.query.all()

    response_body = [person.serialize() for person in people_data]

    return jsonify(response_body), 200


@api.route('/people/<int:id>', methods=['DELETE'])
def del_people(id):
    people_data = People.query.filter_by(id=id).delete()
    db.session.commit()

    return 'People deleted', 204

# ____________________________________________________________________


@api.route('/favorites', methods=['GET'])
def favorites():

    favorites_data = Favorites.query.all()
    response_body = [favorites.serialize() for favorite in favorites_data]
    return jsonify(response_body), 200


@api.route('/favorites/<int:id>', methods=['DELETE'])
def del_favorites(id):
    favorites_data = Favorites.query.filter_by(id=id).delete()
    db.session.commit()

    return 'Favorites deleted', 204

# ____________________________________________________________________


@api.route('/planet', methods=['GET'])
def planet():

    planet_data = Planet.query.all()

    response_body = [planet.serialize() for planet in planet_data]

    return jsonify(response_body), 200


@api.route('/planet/<int:id>', methods=['DELETE'])
def del_planet(id):
    planet_data = Planet.query.filter_by(id=id).delete()
    db.session.commit()

    return 'Planet deleted', 204

# ____________________________________________________________________


@api.route('/species', methods=['GET'])
def species():
    species_data = Species.query.all()
    response_body = [species.serialize() for species in species_data]
    return jsonify(response_body), 200


@api.route('/species/<int:id>', methods=['DELETE'])
def del_species(id):
    species_data = Species.query.filter_by(id=id).delete()
    db.session.commit()

    return 'Species deleted', 204


# ____________________________________________________________________


@api.route('/vehicles', methods=['GET'])
def vehicles():
    vehicles_data = Vehicles.query.all()
    response_body = [vehicles.serialize() for vehicles in vehicles_data]
    return jsonify(response_body), 200


@api.route('/vehicles/<int:id>', methods=['DELETE'])
def del_vehicles(id):
    vehicles_data = Vehicles.query.filter_by(id=id).delete()
    db.session.commit()

    return 'Vehicles deleted', 204
