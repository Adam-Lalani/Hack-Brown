import React from "react";
import Navbar from "./components/Navbar";
import Searchbar from "./components/Searchbar";
import { Link } from "react-router-dom";

const App = () => {
  const containerStyle = {
    fontFamily: "'Inter', sans-serif", // Apply Inter font to the entire component
    backgroundImage: "url('src/assets/homepage-background.png')",
    backgroundSize: "100% 100%",
    backgroundRepeat: "no-repeat",
    height: "100vh", // Set the height to cover the entire viewport height"
    display: "flex",
    flexDirection: "column", // If you want to stack Navbar and content vertically
  };

  return (
    <div style={containerStyle} className="flex flex-col h-lvh">
      <Navbar />
      <div className="flex flex-row">
        <div className="w-1/2"></div>
        <div className="ml-6 flex flex-col flex-grow w-1/2 p-2 justify-center h-lvh space-y-8">
          <div className="flex flex-col mb-8">
            <h1 className="text-white text-6xl font-bold mb-4">
              Tomorrow@Brown
            </h1>
            <p className="text-white font-extralight text-3xl mr-32">
              <span className="text-3xl font-bold">Blast off!</span> Find events
              specific to your needs, or go{" "}
              <span className="italic">rogue</span> and venture out to the
              unknown!
            </p>
          </div>
          <Searchbar />
          <p className="text-white text-lg font-extralight mr-36">
            Learn more about events at Brown by searching for tags such as
            non-professional, academic, artistic, etc. Or click{" "}
            <span className="underline cursor-pointer">here</span> for random
            fun...
          </p>
        </div>
      </div>
    </div>
  );
};

export default App;