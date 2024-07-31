import { Link } from 'react-router-dom'


const Navbar = () => {
  return (
    <ul >
      {/* <h4>Navigation Bar</h4>   */}
      <li><Link to="/">Welcome Page</Link></li>
      <li><Link to="/dogs">Show all dogs</Link></li>
      <li><Link to="/dogs/new">Add a dog</Link></li>
    </ul>
  )
}

export default Navbar