from flask import Blueprint, jsonify, request
from database import db
from models import Card, Deck

cards_bp = Blueprint('cards', __name__)

#GET ALL CARDS
@cards_bp.route('/decks/<int:deck_id>/cards', methods=['GET'])
def get_cards(deck_id):
    cards = Card.query.filter_by(deck_id=deck_id).all()
    return jsonify([card.to_dict() for card in cards])

#CREATE A NEW CARD
@cards_bp.route('/decks/<int:deck_id>/cards', methods=['POST'])
def create_card(deck_id):
    # Check if deck exists
    deck = Deck.query.get(deck_id)
    if not deck:
        return jsonify({'error': 'Deck not found'}), 404

    data = request.get_json()

    # Simple validation - just check they exist
    if not data.get('question') or not data.get('answer'):
        return jsonify({'error': 'Question and answer are required'}), 400

    new_card = Card(
        question=data['question'],
        answer=data['answer'],
        deck_id=deck_id
    )

    db.session.add(new_card)
    db.session.commit()

    return jsonify(new_card.to_dict()), 201

#DELETES A CARD
@cards_bp.route('/decks/<int:deck_id>/cards/<int:card_id>', methods=['DELETE'])
def delete_card(deck_id, card_id):
    card = Card.query.get(card_id)

    if not card:
        return jsonify({'error': 'Card not found'}), 404

    # Verify card belongs to this deck
    if card.deck_id != deck_id:
        return jsonify({'error': 'Card not found in this deck'}), 404

    db.session.delete(card)
    db.session.commit()

    return jsonify({'message': 'Card deleted successfully'}), 200

#UPDATE A CARD
@cards_bp.route('/decks/<int:deck_id>/cards/<int:card_id>', methods=['PUT'])
def update_card(deck_id, card_id):
    card = Card.query.get(card_id)

    if not card:
        return jsonify({'error': 'Card not found'}), 404

    if card.deck_id != deck_id:
        return jsonify({'error': 'Card not found in this deck'}), 404

    data = request.get_json()

    # Simple update - only update what's provided
    if 'question' in data:
        card.question = data['question']
    if 'answer' in data:
        card.answer = data['answer']

    db.session.commit()

    return jsonify(card.to_dict()), 200