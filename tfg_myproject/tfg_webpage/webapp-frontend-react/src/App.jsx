import { BrowserRouter, Routes, Route } from "react-router-dom"
import TestPageView from './views/testPage/testPageView'

function App() {
  return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<h1>Home</h1>} />
                <Route path="/test" element={<TestPageView />} />
                <Route path="*" element={<h1>You dummy dum dum</h1>} />
            </Routes>
        </BrowserRouter>
    );
}

export default App
