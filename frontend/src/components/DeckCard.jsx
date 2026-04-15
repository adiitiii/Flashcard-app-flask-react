function DeckCard({ deck, onNavigate, onDelete }) {
    return (
        <div className="deck-card">
            <div onClick={() => onNavigate(deck.id)} style={{ cursor: 'pointer' }}>
                <h3>{deck.title}</h3>
                <p>{deck.description}</p>
            </div>
            <button className="btn-danger" onClick={(e) => {
                e.stopPropagation();
                onDelete(deck.id);
            }}>
                Delete
            </button>
        </div>
    );
}

export default DeckCard;
