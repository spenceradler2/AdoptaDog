import React, { useEffect, useState } from 'react'
import {  useParams, useNavigate } from 'react-router-dom'
import { useFormik } from 'formik'
import * as yup from 'yup'
import { DogContext } from '../DogContext'
import { useContext } from 'react'



const EditDogForm = () => {
  const { id } = useParams()
  const { updateDog,dogs } = useContext(DogContext)
  const dog = dogs.find(dog => dog.id === parseInt(id))
  const navigate = useNavigate()

  const initialValues = {
    name: dog.name,
    breed: dog.breed,
    image:dog.image
  }
    
    function handleSubmit(values) {
        const resp = fetch("http://localhost:5555/dogs/" + id, {
          method: "PATCH",
          headers: 
          {
            "Accept": "application/json",
            "Content-Type": "application/json"
          },
          body: JSON.stringify(values)
        })
        .then((resp) => resp.json())
        .then(data => {updateDog(data)})
        navigate("/dogs")
      }

    const validationSchema = yup.object({
        name: yup.string().required(),
        breed: yup.string().required(),
        image: yup.string().required()
      })
    
    
    const formik = useFormik({
        initialValues,
        validationSchema,
        validateOnChange: false,
        onSubmit: handleSubmit
      })
    
    return (
        <div>
          <h2>Edit {dog.name}</h2>
          <form onSubmit={ formik.handleSubmit }>
            <div>
                <label htmlFor="name">Name: </label>
                <input type="text" name="name" id="name" value={ formik.values.name } onChange={ formik.handleChange } />
                { formik.errors.name ? <p style={{ color: "red"}}>{ formik.errors.name}</p> : null }
            </div><br />
            <div>
                <label htmlFor="breed">Breed: </label>
                <input type="text" name="breed" id="breed" value={ formik.values.breed } onChange={ formik.handleChange } />
                { formik.errors.breed ? <p style={{ color: "red"}}>{ formik.errors.breed}</p> : null }
            </div><br />
            <div>
                <label htmlFor="image">Image: </label>
                <input type="text" name="image" id="image" value={ formik.values.image } onChange={ formik.handleChange } />
                { formik.errors.image ? <p style={{ color: "red"}}>{ formik.errors.image}</p> : null } 
            </div><br />
                    
            <input type="submit" value="Update Dog" />
          </form>
        </div>
        ) 
      
}

export default EditDogForm