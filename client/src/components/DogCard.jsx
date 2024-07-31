import React from 'react'
import {  useNavigate } from 'react-router-dom'

const DogCard = ({ dog,deleteDog }) => { 
    const navigate = useNavigate()

    function handleDelete() {
        fetch('http://localhost:5555/dogs/' + dog.id, { method: "DELETE" })
        deleteDog(dog.id)
        alert("We will email you shortly on information about picking up your dog :)")
      }

    function handleEdit() 
    {
    navigate(`/dogs/${dog.id}/edit`) //Review
      }
    

  return (
    <div>
    <br></br>
      <img src= {dog.image} alt="Dog image did not load"/> 
      <p>Name: {dog.name}</p>
      <p>Breed: {dog.breed}</p>
      <p>Current Owner: {dog.owner.name}</p>
      <p>Current Location: {dog.adoption_location.name}</p>
      <button onClick={handleDelete}>Adopt Dog</button>
      <br></br>
      <br></br>
      <button onClick={handleEdit}>Edit Dog</button>

    </div>
  )
}

export default DogCard