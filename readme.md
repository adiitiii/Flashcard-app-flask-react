# Flashcard App

## Overview

A full-stack Flashcard Application that allows users to create decks, add cards, and take quizzes to test their knowledge.

---

## Features

* Create, update, and delete flashcard decks
* Add, update, and delete cards within a deck
* Interactive quiz mode to test knowledge
* Score tracking for quiz performance

---

## Tech Stack

* **Backend:** Flask, SQLAlchemy
* **Frontend:** React, Axios
* **Database:** SQLite

---

## Key Technical Decisions

To align with the project goals of simplicity, maintainability, and interface safety, the following technical decisions were made during development:

* **Database (SQLite):** Chosen for its simplicity and self-containment. It requires zero configuration, which allows for instant local setup without relying on external containers or services.
* **Clear Interface Boundaries:** The frontend React application and backend Flask API operate completely independently. This strict decoupling enforces clear system boundaries, increasing the system's change resilience.
* **API Route Validation:** Data validation occurs strictly at the API boundaries. The backend enforces constraints (e.g., verifying required fields and type safety) and explicitly throws `400 Bad Request` before invalid state can ever reach the database or core logic.
* **Basic State Management:** Rather than introducing complex state management libraries (like Redux), state is kept localized to the components that require it. This aligns with the "simplicity over cleverness" mandate.
* **Flask Blueprints:** Application routes are partitioned using Blueprints to prevent having a single monolithic file for routes, making it easy to logically organize features (e.g., mapping to `/decks` and `/cards`).

---

## Project Structure

```
flashcard-app/
│
├── backend/
│   ├── routes/
│   ├── models.py
│   ├── database.py
│   └── app.py
│
├── frontend/
│   ├── src/
│   └── public/
│
├── tests/
│   └── test_api.py
│
├── README.md
└── claude.md
```

---

## How to Run the Project

### 1. Backend Setup

```
cd backend
pip install -r requirements.txt
python app.py
```

Backend will run on:

```
http://127.0.0.1:5000
```

---

### 2. Frontend Setup

```
cd frontend
npm install
npm start
```

Frontend will run on:

```
http://localhost:3000
Note: If port 3000 is already in use, React will automatically start on the next available port (e.g., 3001).
```
---
## API Endpoints

### Decks

* `GET /decks` → Get all decks
* `POST /decks` → Create a new deck
* `PUT /decks/<id>` → Update a deck
* `DELETE /decks/<id>` → Delete a deck

### Cards

* `GET /decks/<deck_id>/cards` → Get cards of a deck
* `POST /decks/<deck_id>/cards` → Create a card
* `PUT /decks/<deck_id>/cards/<card_id>` → Update a card
* `DELETE /decks/<deck_id>/cards/<card_id>` → Delete a card

---

## Running Tests

```
pip install pytest
pytest
```

---

## Future Improvements

* User authentication
* Better UI/UX enhancements
* Search and filter decks
* Progress tracking

---

## Notes

This project demonstrates full-stack development with API integration, state management, and basic automated testing.
