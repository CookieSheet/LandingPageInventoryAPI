from flask import Blueprint, request, jsonify
from space_inventory.helpers import token_required
from space_inventory.models import db, User, Ship, ship_schema, ships_schema

api = Blueprint('api', __name__, url_prefix = '/api')

@api.route('/getdata')
@token_required
def getdata(current_user_token):
    return {'some': 'value'}

# Create Ship Endpoint
@api.route('/ships', methods = ['POST'])
@token_required
def create_ship(current_user_token):
    name = request.json['name']
    description = request.json['description']
    classification = request.json['classification']
    size = request.json['size']
    range = request.json['range']
    max_speed = request.json['max_speed']
    weapons = request.json['weapons']
    shield = request.json['shield']
    engine = request.json['engine']
    travel = request.json['travel']
    user_token = current_user_token.token

    print(f"BIG TESTER: {current_user_token.token}")

    ship = Ship(name, description, classification, size, range, max_speed, weapons, shield, engine, travel, user_token = user_token)

    db.session.add(ship)
    db.session.commit()

    response = ship_schema.dump(ship)
    return jsonify(response)

# Retrieve all Ship Endpoints
@api.route('/ships', methods = ['GET'])
@token_required
def get_ships(current_user_token):
    owner = current_user_token.token
    ships = Ship.query.filter_by(user_token = owner).all()
    response = ships_schema.dump(ships)
    return jsonify(response)


# Retrieve One Ship Endpoint
@api.route('/ships/<id>', methods = ['GET'])
@token_required
def get_ship(current_user_token, id):
    owner = current_user_token.token
    if owner == current_user_token.token:
        ship = Ship.query.get(id)
        response = ship_schema.dump(ship)
        return jsonify(response)
    else:
        return jsonify({'message': 'Valid Token Required'}), 401

# Update Ship Endpoint
@api.route('/ships/<id>', methods = ['POST', 'PUT'])
@token_required
def update_ship(current_user_token, id):
    ship = Ship.query.get(id) # grab ship instance

    ship.name = request.json['name']
    ship.description = request.json['description']
    ship.classification = request.json['classification']
    ship.size = request.json['size']
    ship.range = request.json['range']
    ship.max_speed = request.json['max_speed']
    ship.weapons = request.json['weapons']
    ship.shield = request.json['shield']
    ship.engine = request.json['engine']
    ship.travel = request.json['travel']
    ship.user_token = current_user_token.token

    db.session.commit()
    response = ship_schema.dump(ship)
    return jsonify(response)


# Delet ship endpoijnt
@api.route('/ships/<id>', methods = ['DELETE'])
@token_required
def delete_ship(current_user_token, id):
    ship = Ship.query.get(id)
    db.session.delete(ship)
    db.session.commit()
    response = ship_schema.dump(ship)
    return jsonify(response)

