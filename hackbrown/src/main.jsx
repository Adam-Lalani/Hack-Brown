import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx";
import About from "./pages/About";
import Feedback from "./pages/Feedback";
import Resultpage from "./pages/Resultpage.jsx";
import "./index.css";
import { createBrowserRouter, RouterProvider } from "react-router-dom";

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
  },
  {
    path: "/about",
    element: <About />,
  },
  {
    path: "/feedback",
    element: <Feedback />,
  },
  {
    path: "/resultpage/", // Route without dynamic parameter
    element: <Resultpage />,
  },
  {
    path: "/resultpage/:query",
    element: <Resultpage />,
  },
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);
