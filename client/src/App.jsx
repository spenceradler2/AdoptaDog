import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Navbar from "./Navbar"
import Home from "./Home"
import DogList from "./components/DogList"
import DogForm from "./components/DogForm"
import { DogProvider } from "./DogContext"
import EditDogForm from "./components/EditDogForm";

function App() {

  return (
    <Router>
      <DogProvider>
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/dogs" element={<DogList />} />
          <Route path="/dogs/new" element={<DogForm />} />
          <Route path="/dogs/:id/edit" element={<EditDogForm />} />
        </Routes>
      </DogProvider> 
    </Router>
  )
}

export default App