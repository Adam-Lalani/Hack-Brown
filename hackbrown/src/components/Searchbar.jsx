import React from "react";
import magnifyingImage from "../assets/mangifyingglass.png";

const Searchbar = () => {
  return (
    <div className="flex w-4/5 bg-white rounded-lg h-20 p-4 items-center">
      <img src={magnifyingImage} alt="Magnifying Glass" className="w-6 h-6" />
      <textarea 
        placeholder="Enter here"
        className="flex w-full resize-none outline-none text-lg h-full px-4 py-2.5 items-center"
      />
    </div>
  );
};

export default Searchbar;
