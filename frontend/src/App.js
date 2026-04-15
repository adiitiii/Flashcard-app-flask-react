import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import DeckDetail from './pages/DeckDetail';
import QuizPage from './pages/QuizPage';
import './App.css';

function App() {
    return (
        <BrowserRouter>
        <Routes>
            <Route path='/' element={<Home />} />
            <Route path='/decks/:id' element={<DeckDetail />} />
            <Route path='/quiz/:id' element={<QuizPage />} />
        </Routes>
        </BrowserRouter>
    );
}

export default App;

