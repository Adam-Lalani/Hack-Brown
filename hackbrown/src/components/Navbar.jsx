import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav className="text-white text-xl p-4">
      <ul className="flex justify-between items-center">
        <li>
          <Link to="/">Home</Link>
        </li>
        <div className="ml-auto flex space-x-10">
          <li>
            <Link to="/about">About</Link>
          </li>
          <li>
            <Link to="/feedback">Feedback</Link>
          </li>
        </div>
      </ul>
    </nav>
  );
};

export default Navbar;
