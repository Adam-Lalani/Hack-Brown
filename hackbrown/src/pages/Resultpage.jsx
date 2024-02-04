import React from "react";
import { useState, useEffect } from "react";
import Result from "../components/Result.jsx";
import Searchbar from "../components/Searchbar.jsx";
import Navbar from "../components/Navbar.jsx";


const Resultpage = () => {
  const [searchResults, setSearchResults] = useState([]);

  const containerStyle = {
    fontFamily: "'Inter', sans-serif",
    backgroundImage: "url('src/assets/result-background.png')",
    backgroundSize: "100% 100%",
    backgroundRepeat: "no-repeat",
    height: "100vh",
    display: "flex",
    flexDirection: "column",
  };
  return (
    <div style={containerStyle} className="flex flex-col h-lvh">
      <Navbar />
      <Searchbar />
      <div className="flex-col space-y-8 w-full">
        {searchResults.map((result) => (
          <Result key={result.id} data={result} />
        ))}
      </div>
    </div>
  );
};

export default Resultpage;
