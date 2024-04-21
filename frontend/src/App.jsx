import react from 'react'
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import Login from './pages/Login'
import Register from './pages/Register'
import NotFound from './pages/NotFound'
import Home from './pages/Home'
import ProtectedRoute
from './components/ProtectedRoute'

function Logout() {
  localStorage.clear()
  return <Navigate to="/login"/>
}
function RegisterAndLogout() {
  localStorage.clear()
  return <Register /> //remove and lingering access tokens when someone new registers
}
function App() {
//any route that we want to be protected we will wrap with a protected route aaround it
  return (
    <BrowserRouter>
      <Routes>
        <Route
        path="/"
        element={
          <ProtectedRoute>  
            <Home/>
          </ProtectedRoute>
        }
        />
        <Route path="/login" element={<Login/>}/>
        <Route path="/logout" element={<Logout/>}/>
        <Route path="/register" element={<RegisterAndLogout/>}/>
        <Route path="/*" element={<NotFound/>}/> 
      </Routes>
    </BrowserRouter>
  )
}

export default App
