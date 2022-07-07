import './App.css';
import { useEffect, useState } from 'react'
import Prato from './components/prato.js'


function App() {
  const [pratos, setPratos] = useState( [] )


  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/imoveis/')
    .then(resposta => resposta.json())
    .then(dados => {
        setPratos(dados)
    })

}, [])

  return (
    <div className="App">
    {pratos.map(prato =>
    (<Prato
    key={prato.id}
    nome={prato.nome}
    descricao={prato.descricao}
    valor={prato.valor}
    />))}
    </div>
  );
}

export default App;
