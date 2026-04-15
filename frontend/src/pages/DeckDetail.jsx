import { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { getCards, createCard, deleteCard } from '../api/index';
import FlashCard from '../components/FlashCard';

function DeckDetail() {
    const { id } = useParams();
    const navigate = useNavigate();
    const [cards, setCards] = useState([]);
    const [question, setQuestion] = useState('');
    const [answer, setAnswer] = useState('');

    useEffect(() => {
        getCards(id).then(res => setCards(res.data));
    }, [id]);

    const handleAddCard = () => {
        if (!question || !answer) return;
        createCard(id, { question, answer })
            .then(res => {
                setCards([...cards, res.data]);
                setQuestion('');
                setAnswer('');
            });
    };

    const handleDelete = (cardId) => {
        deleteCard(id, cardId)
            .then(() => setCards(cards.filter(c => c.id !== cardId)));
    };

    return (
        <div className="container">
            <button className="btn-secondary" onClick={() => navigate('/')}>← Back</button>
            <h1>Cards</h1>

            <div className="form">
                <input
                    value={question}
                    onChange={e => setQuestion(e.target.value)}
                    placeholder="Question"
                />
                <input
                    value={answer}
                    onChange={e => setAnswer(e.target.value)}
                    placeholder="Answer"
                />
                <button className="btn-primary" onClick={handleAddCard}>Add Card</button>
            </div>

            {cards.map(card => (
                <FlashCard 
                    key={card.id} 
                    card={card} 
                    onDelete={handleDelete} 
                />
            ))}

            {cards.length > 0 && (
                <button className="btn-primary" onClick={() => navigate(`/quiz/${id}`)}>Start Quiz</button>
            )}
        </div>
    );
}

export default DeckDetail;