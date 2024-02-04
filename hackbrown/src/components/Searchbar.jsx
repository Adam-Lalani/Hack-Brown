import React from "react";
import magnifyingImage from "../assets/mangifyingglass.png";

const Searchbar = () => {
  return (
    // <div className="flex flex-grow w-full bg-white relative rounded items-center justify-center">
    //   <div className="flex items-center absolute ">
    //     <img src={magnifyingImage} alt="Magnifying Glass" className="w-6 h-6" />
    //     <textarea
    //       placeholder="Enter here"
    //       className="flex flex-grow h-18 w-full rounded-lg resize-none outline-none p-4 pl-12" // Add pl-12 for left padding
    //     />
    //   </div>
    // </div>
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