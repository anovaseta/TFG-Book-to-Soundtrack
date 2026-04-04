import { BrowserRouter, Routes, Route } from "react-router-dom"
import TestPageView from './views/testPage/testPageView'
import MainFlowView from './views/mainFlow/mainFlowView'
import ChooseBookView from "./views/chooseBook/chooseBookView"
import SelectedBookView from "./views/selectedBook/selectedBookView"

function App() {
  return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<h1>Home</h1>} />
                <Route path="/test" element={<TestPageView />} />
                <Route path="/flow" element={<MainFlowView />} />
                <Route path="/flow/choose-book" element={<ChooseBookView />} />
                <Route path="/flow/book/:book_id" element={<SelectedBookView />} />
                <Route path="/flow/book/:book_id/create-playlist" element={<p>In progress...</p>} />
                <Route path="*" element={<h1>Not found</h1>} />
            </Routes>
        </BrowserRouter>
    );
}

export default App
