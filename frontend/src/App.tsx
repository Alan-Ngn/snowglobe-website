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
import Home from './components/Home/Home';

const App: FC = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
      </Routes>
    </Router>
  );
};

export default App;
