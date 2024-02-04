import React from "react";
import Navbar from "../components/Navbar";
import logoImage from "../assets/brownlogo.png";

const About = () => {
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
        <div className="mx-20 flex flex-col flex-grow w-1/2 p-2 h-lvh space-y-8">
          <h1 className="text-white text-2xl">
            Hi! Our names are Nick Klatsky '25, Morgan Lo '25, Adam Lalani '26,
            and Christopher Chen '26. We are a group of{" "}
            <span className="italic">mostly</span> first time hackers!
          </h1>
          <h1 className="text-white text-lg">
            We decided to create Tomorrow@Brown in order to create a website for
            students at Brown University to easily access information about
            events here. Oftentimes, many events go unnoticed by students
            because information about the events were not communicated with
            them. Maybe they didn't sign up for the emailing list, or maybe they
            were too busy to see it. Whatever the case, this website has access
            to a database of club events and displays them to students based off
            of specific tags that they may input.
          </h1>
          <h1 className="text-white text-lg">
            Backend: This project uses python for backend development and relies on the
            NTLK, Scikit-learn, and the chatgpt API to compute a search
            algorithm.
          </h1>
          <h1 className="text-white text-lg">
            Frontend: This project was created with HTML/JS/React with the Tailwind CSS
            Framework. Initial designs for the general website layout were
            created in Figma.
          </h1>
        </div>
      </div>
    </div>
  );
};

export default About;
