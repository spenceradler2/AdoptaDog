import { useEffect, useState, useContext } from 'react'
import { useFormik } from 'formik'
import * as yup from 'yup'
import { DogContext } from '../DogContext'

const DogForm = () => {

  const { addDog } = useContext(DogContext)

  const initialValues = {
    name: "",
    breed: "",
    image:"",
    owner_name: "",
    adoption_location_name: "",
  }

  const validationSchema = yup.object({
    name: yup.string().required(),
    breed: yup.string().required(),
    image: yup.string().required(),
    owner_name: yup.string().required(),
    adoption_location_name: yup.string().required()
  })


  const formik = useFormik({
    initialValues,
    validationSchema,
    validateOnChange: false,
    onSubmit: function(values) {
      addDog({
        ...values
      })
    }
  })

  return (
    <div>
      <h2>Add a dog below:</h2>
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
        <div>
            <label htmlFor="owner_name">Current Owner(If there is no current owner. Type None): </label>
            <input type="text" name="owner_name" id="owner_name" value={ formik.values.owner_name } onChange={ formik.handleChange } />
            { formik.errors.owner_name ? <p style={{ color: "red"}}>{ formik.errors.owner_name}</p> : null } 
        </div><br />
        <div>
            <label htmlFor="adoption_location_name">Current Location (If the location is unknown. Type Unknown): </label>
            <input type="text" name="adoption_location_name" id="adoption_location_name" value={ formik.values.adoption_location_name } onChange={ formik.handleChange } />
            { formik.errors.adoption_location_name ? <p style={{ color: "red"}}>{ formik.errors.adoption_location_name}</p> : null } 
        </div><br />
        
        <input type="submit" value="Add a Dog" />
      </form>
    </div>
  )
}

export default DogForm