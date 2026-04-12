import { BrowserRouter, Routes, Route } from "react-router-dom"
import InstructionsView from "./views/instructions/instructionsView"
import MainFlowView from './views/mainFlow/mainFlowView'
import ChooseBookView from "./views/chooseBook/chooseBookView"
import SelectedBookView from "./views/selectedBook/selectedBookView"
import ConfigurePlaylistView from "./views/configurePlaylist/configurePlaylistView"
import ShowPlaylistView from "./views/showPlaylist/showPlaylistView"
import './App.css'

function App() {
  return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<MainFlowView />} />
                <Route path="/instructions" element={<InstructionsView />} />
                <Route path="/flow/choose-book" element={<ChooseBookView />} />
                <Route path="/flow/book/:mode/:book_id" element={<SelectedBookView />} />
                <Route path="/flow/book/:mode/:book_id/create-playlist" element={<ConfigurePlaylistView />} />
                <Route path="/flow/book/:mode/:book_id/show-playlist/:n_tracks" element={<ShowPlaylistView />} />
                <Route path="*" element={<h1>Not found!</h1>} />
            </Routes>
        </BrowserRouter>
    );
}

export default App
