from flask import Blueprint, jsonify, request
from database import db
from models import Deck

decks_bp = Blueprint('decks', __name__)

#GET ALL DECKS
@decks_bp.route('/decks', methods=['GET'])
def get_decks():
    decks = Deck.query.all()
    return jsonify([deck.to_dict() for deck in decks])

#CREATE DECK
@decks_bp.route('/decks', methods=['POST'])
def create_deck():
    data = request.get_json()

    # Simple validation - just check title exists
    if not data.get('title'):
        return jsonify({'error': 'Title is required'}), 400

    new_deck = Deck(
        title=data['title'],
        description=data.get('description', '')
    )

    db.session.add(new_deck)
    db.session.commit()

    return jsonify(new_deck.to_dict()), 201

#DELETES A DECK
@decks_bp.route('/decks/<int:id>', methods=['DELETE'])
def delete_deck(id):
    deck = Deck.query.get(id)

    if not deck:
        return jsonify({'error': 'Deck not found'}), 404

    db.session.delete(deck)
    db.session.commit()

    return jsonify({'message': 'Deck deleted successfully'}), 200

#UPDATES A DECK
@decks_bp.route('/decks/<int:id>', methods=['PUT'])
def update_deck(id):
    deck = Deck.query.get(id)

    if not deck:
        return jsonify({'error': 'Deck not found'}), 404

    data = request.get_json()

    # Only update fields that are provided
    if 'title' in data:
        deck.title = data['title']
    if 'description' in data:
        deck.description = data['description']

    db.session.commit()

    return jsonify(deck.to_dict()), 200