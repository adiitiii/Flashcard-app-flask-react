import { useState, useEffect } from 'react';
import { getDecks, createDeck, deleteDeck } from '../api/index';
import { useNavigate } from 'react-router-dom';
import DeckCard from '../components/DeckCard';

function Home() {
    const [decks, setDecks] = useState([]);
    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');
    const navigate = useNavigate();

    useEffect(() => {
        getDecks().then(res => setDecks(res.data));
    }, []);

    const handleCreate = () => {
        if (!title) return;
        createDeck({ title, description })
            .then(res => {
                setDecks([...decks, res.data]);
                setTitle('');
                setDescription('');
            });
    };

    const handleDeleteDeck = (deckId) => {
        deleteDeck(deckId)
            .then(() => setDecks(decks.filter(deck => deck.id !== deckId)));
    };

    return (
    <div className="container">
        <h1>My Flashcard Decks</h1>

        <div className="form">
            <input
                value={title}
                onChange={e => setTitle(e.target.value)}
                placeholder="Deck title"
            />
            <input
                value={description}
                onChange={e => setDescription(e.target.value)}
                placeholder="Description"
            />
            <button className="btn-primary" onClick={handleCreate}>Create Deck</button>
        </div>

        {decks.map(deck => (
            <DeckCard 
                key={deck.id} 
                deck={deck} 
                onNavigate={(id) => navigate(`/decks/${id}`)} 
                onDelete={handleDeleteDeck} 
            />
        ))}
    </div>
);
}

export default Home;