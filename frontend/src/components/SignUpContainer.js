import React from 'react'
import { Link } from 'react-router-dom'
import './SignUpContainer.css'



function LoginContainer(props) {
    return (
   
         
    <div className='container'>
     <div className='grid-container'>
        <div className='colonne-1'> 
         <Link to='/'> <i className='fa fa-house'></i></Link>
        </div>
        <div className='colonne-2'> 
          <h2> Inscrivez-vous et trouvez votre bonheur !</h2> 
          <button className='btn--login' onClick={() => props.onFormSwitch('register')}>se connecter avec google</button>
          <Link to="/Login" className='lien'>je possède un compte</Link>
         
        </div>
     </div>
   </div>
 )

 
}

export default LoginContainer