from flask import Flask, jsonify
from flask_cors import CORS
from database import db
from routes.decks import decks_bp
from routes.cards import cards_bp
import logging


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flashcards.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    CORS(app)

    app.register_blueprint(decks_bp)
    app.register_blueprint(cards_bp)

    # Global error handler for 404
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Resource not found'}), 404

    # Global error handler for 500
    @app.errorhandler(500)
    def internal_error(error):
        logging.error(f"Internal server error: {str(error)}")
        return jsonify({'error': 'Internal server error'}), 500

    with app.app_context():
        db.create_all()

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)