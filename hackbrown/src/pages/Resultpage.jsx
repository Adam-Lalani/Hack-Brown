import React from "react";
import Result from "../components/Result.jsx";
import Searchbar from "../components/Searchbar.jsx";
import Navbar from "../components/Navbar.jsx";
import { useLocation } from "react-router-dom";

const Resultpage = () => {
  const location = useLocation();
  const searchResults = location.state?.results || [];

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
      <div className="flex-col space-y-8 w-full">
        {searchResults.map((result, index) => (
          <Result key={index} data={result} />
        ))}
      </div>
    </div>
  );
};

export default Resultpage;
