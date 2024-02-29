// import React from 'react';
// import { Route, Routes } from "react-router-dom";
// import logo from './logo.svg';
// import './App.css';
// import Home from './components/Home/Home';
// function App() {
//   return (
//     <div className="App">
//       <Route path="/" element={<Home />} />
//     </div>
//   );
// }

// export default App;
import React, { FC } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import WeatherList from './components/WeatherList/WeatherList';
import WeatherItem from './components/WeatherItem/WeatherItem';

const App: FC = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<WeatherList />} />
        <Route path="/:weatherId" element={<WeatherItem/>} />
      </Routes>
    </Router>
  );
};

export default App;
