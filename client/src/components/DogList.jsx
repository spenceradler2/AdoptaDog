import { useContext } from 'react'
import { DogContext } from '../DogContext'
import DogCard from './DogCard'

const DogList = () => {
  const { dogs,deleteDog } = useContext(DogContext)

  const dogCards = dogs.map(dog => <DogCard key={ dog.id } dog={dog} deleteDog={deleteDog}/>)

  return (
    <div className='allbutnavbarandcard'>
    <h2>Would you like to adopt one of the dogs below?</h2>

    <div className='row'>
      { dogCards }
    </div>
    </div>
  )
}

export default DogList