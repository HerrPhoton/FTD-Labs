import './App.css';
import { Routes, Route } from 'react-router-dom';
import ConclusionPanel from './components/ConclusionPanel';
import DescriptionPanel from './components/DescriptionPanel';
import IntroPanel from './components/IntroPanel';
import NavPanel from './components/NavPanel';


function App() 
{
  return (
    <div className="App">
        <NavPanel/>

        <Routes>
          <Route path="/" element={<IntroPanel />} />
          <Route path="/description" element={<DescriptionPanel />} />
          <Route path="/conclusion" element={<ConclusionPanel />} />
        </Routes>

    </div>
  );
}

export default App;
