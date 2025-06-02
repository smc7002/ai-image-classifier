// frontend/src/pages/Home.jsx

import React, { useState, useEffect } from 'react';
import UploadArea from '../components/UploadArea';
import ResultBox from '../components/ResultBox';

const backgrounds = [
  '/bg1.jpg',
  '/bg2.jpg',
  '/bg3.jpg',
  //
];

const Home = () => {
  const [currentBg, setCurrentBg] = useState(0);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentBg((prev) => (prev + 1) % backgrounds.length);
    }, 5000); // 5sec
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="w-full h-screen relative overflow-hidden">
      {backgrounds.map((bg, index) => (
        <img
          key={index}
          src={bg}
          alt={`Background ${index}`}
          className={`absolute w-full h-full object-cover transition-opacity duration-1000 ${
            index === currentBg ? 'opacity-100' : 'opacity-0'
          }`}
        />
      ))}
      <div className="absolute w-full h-full bg-gradient-to-t from-black/70 via-black/40 to-transparent"></div>
      <div className="relative z-10 flex flex-col items-center justify-center h-full text-center">
        <h1 className="text-5xl font-bold text-white mb-4">StyleScope</h1>
        <p className="text-gray-300 mb-6">Show your outfit, we’ll tell your style.</p>
        <UploadArea setResult={setResult} setLoading={setLoading} />
        {result && <ResultBox result={result} />}
      </div>
    </div>
  );
};

export default Home;
