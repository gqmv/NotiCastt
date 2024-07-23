import { Routes, Route, BrowserRouter, Outlet } from 'react-router-dom'

import Home from './pages/Home'
import PodCast from './pages/PodCast'
import Navbar from './components/Navbar'
import Footer from './components/Footer'

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
      </Routes>
      <Routes>
      <Route element={
        <>
        <Navbar /> 
        <Outlet /> 
        <Footer />
        </>
      }>
        <Route path="/podcast" element={<PodCast />} />
      </Route>
      </Routes>
    </BrowserRouter>
  )
}

export default App