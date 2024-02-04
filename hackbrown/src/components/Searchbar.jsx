import React, { useState } from "react";
import magnifyingImage from "../assets/mangifyingglass.png";
import { fetchURL } from "../fetch";

const Searchbar = () => {
  const [inputValue, setInputValue] = useState("");

  const handleKeyDown = (event) => {
    if (event.key === "Enter") {
      fetchURL(inputValue);
      setInputValue("");
    }
  };


  const handleChange = (event) => {
    setInputValue(event.target.value);
  };

  return (
    <div className="flex w-4/5 bg-white rounded-lg h-20 p-4 items-center">
      <img src={magnifyingImage} alt="Magnifying Glass" className="w-6 h-6" />
      <textarea
        placeholder="Enter here"
        className="flex w-full resize-none outline-none text-lg h-full px-4 py-2.5 items-center"
        onKeyDown={handleKeyDown}
        onChange={handleChange}
        value={inputValue}
      />
    </div>
  );
};

export default Searchbar;
