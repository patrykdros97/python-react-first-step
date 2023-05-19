import './App.css';
import axios from 'axios';
import { useState, useEffect} from 'react';

function App() {
  const [people, setPeople] = useState([]);

  useEffect(() => {
    axios.get('/api').then(res => setPeople(res.data));
  }, []);

  const listItems = people.map((p, index) =>  
    <li key={index}>{p.id} {p.name} {p.age}</li>
  );

  return (  
    <div>  
        <h2>List of peoples</h2>  
            <ul>{listItems}</ul>  
    </div>  
  );
}

export default App;
