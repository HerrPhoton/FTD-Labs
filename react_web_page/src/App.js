import './App.css';
import { Routes, Route, Navigate } from 'react-router-dom';
import ConclusionPanel from './components/ConclusionPanel';
import DescriptionPanel from './components/DescriptionPanel';
import IntroPanel from './components/IntroPanel';
import NavPanel from './components/NavPanel';
import PostsPanel from './components/PostsPanel';
import APIPanel from './components/APIPanel';
import InvertImgPanel from './components/InvertImgPanel';
import StatisticsPanel from './components/StatisticsPanel';

function App()
{
  return (
    <div className="app-container">
        <NavPanel/>

        <Routes>
          <Route path="/" element={<Navigate to="/intro" replace />} />
          <Route path="/intro" element={<IntroPanel />} />
          <Route path="/description" element={<DescriptionPanel />} />
          <Route path="/posts" element={<PostsPanel />} />
          <Route path="/conclusion" element={<ConclusionPanel />} />
          <Route path="/invert" element={<InvertImgPanel />} />
          <Route path="/api" element={<APIPanel />} />
          <Route path="/statistics" element={<StatisticsPanel />} />
        </Routes>

    </div>
  );
}

export default App;
