import { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { getCards } from '../api/index';

function QuizPage() {
    const { id } = useParams();
    const navigate = useNavigate();
    const [cards, setCards] = useState([]);
    const [current, setCurrent] = useState(0);
    const [showAnswer, setShowAnswer] = useState(false);
    const [score, setScore] = useState(0);
    const [finished, setFinished] = useState(false);

    useEffect(() => {
        getCards(id).then(res => setCards(res.data));
    }, [id]);

    const handleAnswer = (correct) => {
        if (correct) setScore(score + 1);
        if (current + 1 >= cards.length) {
            setFinished(true);
        } else {
            setCurrent(current + 1);
            setShowAnswer(false);
        }
    };

    if (finished) {
        return (
            <div className="container">
                <div className="score-box">
                    <h1>{score} / {cards.length}</h1>
                    <p>Quiz Complete!</p>
                    <button className="btn-primary" onClick={() => navigate(`/decks/${id}`)}>Back to Deck</button>
                </div>
            </div>
        );
    }

    if (cards.length === 0) return <p>Loading...</p>;

    return (
        <div className="container">
            <div className="quiz-box">
                <p>Question {current + 1} of {cards.length}</p>
                <h3>{cards[current].question}</h3>

                {!showAnswer ? (
                    <button className="btn-secondary" onClick={() => setShowAnswer(true)}>Show Answer</button>
                ) : (
                    <div>
                        <p className="quiz-answer">{cards[current].answer}</p>
                        <div className="quiz-buttons">
                            <button className="btn-success" onClick={() => handleAnswer(true)}>✓ Got it right</button>
                            <button className="btn-danger" onClick={() => handleAnswer(false)}>✗ Got it wrong</button>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
}

export default QuizPage;