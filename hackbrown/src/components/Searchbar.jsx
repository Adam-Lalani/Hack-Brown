import React, { useState, useCallback } from "react";
import magnifyingImage from "../assets/mangifyingglass.png";
import { useNavigate } from "react-router-dom";

const Searchbar = () => {
  const navigate = useNavigate();
  const [searchQuery, setSearchQuery] = useState("");

  const handleSearch = useCallback(() => {
    if (!searchQuery){
        navigate("/resultpage");
    }
    if (searchQuery.trim() !== "") {
      const queryValue = encodeURIComponent(searchQuery);
      navigate(`/resultpage/${queryValue}`);
    }
  }, [navigate, searchQuery]);

  const handleKeyDown = (event) => {
    if (event.key === "Enter") {
      handleSearch();
    }
  };

  return (
    <div className="flex w-4/5 bg-white rounded-lg h-20 p-4 items-center cursor-pointer">
      <img
        src={magnifyingImage}
        alt="Magnifying Glass"
        className="w-6 h-6"
        onClick={handleSearch}
      />

      <textarea
        placeholder="Enter here"
        className="flex w-full resize-none outline-none text-lg h-full px-4 py-2.5 items-center"
        value={searchQuery}
        onChange={(e) => setSearchQuery(e.target.value)}
        onKeyDown={handleKeyDown}
      />
    </div>
  );
};

export default Searchbar;
