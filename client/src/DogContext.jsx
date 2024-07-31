import { useEffect, createContext, useState } from "react";
import { useNavigate } from "react-router-dom";

const DogContext = createContext({})

function DogProvider({ children }) {
  const [dogs, setDogs] = useState([])

  const navigate = useNavigate()

  useEffect(() => {
    fetch("http://localhost:5555/dogs")
      .then((resp) => resp.json())
      .then(data => {setDogs(data)})
    }, [])

  function addDog(addDog) {
    const resp = fetch("http://localhost:5555/dogs", {
      method: "POST",
      headers: 
      {
        "Accept": "application/json",
        "Content-Type": "application/json"
      },
      body: JSON.stringify(addDog)
    })
    .then((resp) => resp.json())
    .then(dog => {setDogs([...dogs, dog])})
    navigate("/dogs")
  }
  
  function deleteDog(id) {
    const filteredDogs = dogs.filter(dog => dog.id !== id)
    setDogs(filteredDogs)
  }

  function updateDog(updatedDog) {
    const updatedDogs = dogs.map(dog => {
      if(dog.id === updatedDog.id) {
        return updatedDog
      } else {
        return dog
      }
    })
    setDogs(updatedDogs)
  }

  return <DogContext.Provider value={{ dogs, addDog,deleteDog, updateDog }}>{ children }</DogContext.Provider>
}

export { DogContext, DogProvider }