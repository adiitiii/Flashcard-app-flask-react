function FlashCard({ card, onDelete }) {
    return (
        <div className="card-item">
            <div>
                <p><strong>Q:</strong> {card.question}</p>
                <p><strong>A:</strong> {card.answer}</p>
            </div>
            <button className="btn-danger" onClick={() => onDelete(card.id)}>
                Delete
            </button>
        </div>
    );
}

export default FlashCard;
