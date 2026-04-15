import axios from 'axios'

const API = axios.create({
    baseURL: 'http://127.0.0.1:5000'
})

//Deck API Calls
export const getDecks = () => API.get('/decks');
export const createDeck = (data) => API.post('/decks', data);
export const deleteDeck = (id) => API.delete(`/decks/${id}`);
export const updateDeck = (id, data) => API.put(`/decks/${id}`, data);

//Card API Calls
export const getCards = (deckId) => API.get(`/decks/${deckId}/cards`);
export const createCard = (deckId, data) => API.post(`/decks/${deckId}/cards`, data);
export const deleteCard = (deckId, cardId) => API.delete(`/decks/${deckId}/cards/${cardId}`);
export const updateCard = (deckId, cardId, data) => API.put(`/decks/${deckId}/cards/${cardId}`, data);