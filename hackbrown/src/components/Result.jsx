import React from "react";

const Result = ({ data }) => {
  return (
    <div className="w-3/5 h-64 rounded-lg bg-white flex flex-col p-4 overflow-auto">
      <h1>{data.From}</h1>
      <h2>{data.Subject}</h2>
      <p>{data.Data}</p>
    </div>
  );
};

export default Result;
