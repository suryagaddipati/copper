import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import Test from './Test'
import './index.css'

// Use Test component to debug syntax highlighting
const useTest = window.location.search.includes('test')

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    {useTest ? <Test /> : <App />}
  </React.StrictMode>,
)