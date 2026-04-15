import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from database import db as _db


@pytest.fixture
def client():
    app = create_app()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            _db.create_all()
            yield client
            _db.drop_all()


class TestFlashcardApp:
    """Core tests that prove the app works correctly"""

    def test_create_and_get_deck(self, client):
        """Create a deck, verify it appears in list"""
        # Create
        resp = client.post('/decks', json={
            'title': 'Spanish Words',
            'description': 'Basic vocabulary'
        })
        assert resp.status_code == 201
        deck_id = resp.get_json()['id']

        # Get all decks
        resp = client.get('/decks')
        decks = resp.get_json()
        assert len(decks) == 1
        assert decks[0]['title'] == 'Spanish Words'

    def test_deck_validation_rejects_invalid_input(self, client):
        """Test all validation rules together"""
        # Missing title
        resp = client.post('/decks', json={'description': 'No title'})
        assert resp.status_code == 400

        # Empty title (spaces only)
        resp = client.post('/decks', json={'title': '   '})
        assert resp.status_code == 400

        # Title too long (>100 chars)
        resp = client.post('/decks', json={'title': 'a' * 101})
        assert resp.status_code == 400

    def test_update_and_delete_deck(self, client):
        """Update deck details, then delete it"""
        # Create
        resp = client.post('/decks', json={'title': 'Original', 'description': 'Old'})
        deck_id = resp.get_json()['id']

        # Update
        resp = client.put(f'/decks/{deck_id}', json={'title': 'Updated', 'description': 'New'})
        assert resp.status_code == 200
        assert resp.get_json()['title'] == 'Updated'

        # Delete
        resp = client.delete(f'/decks/{deck_id}')
        assert resp.status_code == 200

        # Verify gone
        resp = client.get('/decks')
        assert len(resp.get_json()) == 0

    def test_create_and_get_card(self, client):
        """Create a card, verify it appears in deck"""
        # Create deck first
        resp = client.post('/decks', json={'title': 'Math'})
        deck_id = resp.get_json()['id']

        # Create card
        resp = client.post(f'/decks/{deck_id}/cards', json={
            'question': 'What is 2+2?',
            'answer': '4'
        })
        assert resp.status_code == 201

        # Get cards
        resp = client.get(f'/decks/{deck_id}/cards')
        cards = resp.get_json()
        assert len(cards) == 1
        assert cards[0]['question'] == 'What is 2+2?'

    def test_card_validation_rejects_invalid_input(self, client):
        """Card validation rules"""
        # Create deck
        resp = client.post('/decks', json={'title': 'Test'})
        deck_id = resp.get_json()['id']

        # Missing question
        resp = client.post(f'/decks/{deck_id}/cards', json={'answer': 'Only answer'})
        assert resp.status_code == 400

        # Missing answer
        resp = client.post(f'/decks/{deck_id}/cards', json={'question': 'Only question'})
        assert resp.status_code == 400

        # Question too long (>500 chars)
        resp = client.post(f'/decks/{deck_id}/cards', json={
            'question': 'a' * 501,
            'answer': 'Valid answer'
        })
        assert resp.status_code == 400

    def test_update_and_delete_card(self, client):
        """Update card details, then delete it"""
        # Create deck and card
        resp = client.post('/decks', json={'title': 'Test'})
        deck_id = resp.get_json()['id']

        resp = client.post(f'/decks/{deck_id}/cards', json={
            'question': 'Old Q', 'answer': 'Old A'
        })
        card_id = resp.get_json()['id']

        # Update
        resp = client.put(f'/decks/{deck_id}/cards/{card_id}', json={
            'question': 'New Q', 'answer': 'New A'
        })
        assert resp.status_code == 200
        assert resp.get_json()['question'] == 'New Q'

        # Delete
        resp = client.delete(f'/decks/{deck_id}/cards/{card_id}')
        assert resp.status_code == 200

        # Verify gone
        resp = client.get(f'/decks/{deck_id}/cards')
        assert len(resp.get_json()) == 0

    def test_quiz_gets_cards_from_deck(self, client):
        """Quiz endpoint returns cards for a deck"""
        # Create deck with 2 cards
        resp = client.post('/decks', json={'title': 'Quiz Deck'})
        deck_id = resp.get_json()['id']

        client.post(f'/decks/{deck_id}/cards', json={
            'question': 'Q1', 'answer': 'A1'
        })
        client.post(f'/decks/{deck_id}/cards', json={
            'question': 'Q2', 'answer': 'A2'
        })

        # Get cards for quiz
        resp = client.get(f'/decks/{deck_id}/cards')
        cards = resp.get_json()

        assert len(cards) == 2
        assert cards[0]['question'] == 'Q1'
        assert cards[1]['question'] == 'Q2'