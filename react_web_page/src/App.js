import './App.css';
import { Routes, Route } from 'react-router-dom';
import ConclusionPanel from './components/ConclusionPanel';
import DescriptionPanel from './components/DescriptionPanel';
import IntroPanel from './components/IntroPanel';
import NavPanel from './components/NavPanel';
import PostsPanel from './components/PostsPanel';
import APIPanel from './components/APIPanel';
import InvertImgPanel from './components/InvertImgPanel';

function App()
{
  return (
    <div className="app-container">
        <NavPanel/>

        <Routes>
          <Route path="/" element={<IntroPanel />} />
          <Route path="/description" element={<DescriptionPanel />} />
          <Route path="/posts" element={<PostsPanel />} />
          <Route path="/conclusion" element={<ConclusionPanel />} />
          <Route path="/invert" element={<InvertImgPanel />} />
          <Route path="/api" element={<APIPanel />} />
        </Routes>

    </div>
  );
}

export default App;
