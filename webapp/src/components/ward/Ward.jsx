import React from "react";
import "./Ward.scss";

import WardTable from "./WardTable";
import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";

function Ward() {
  return (
    <div className="ward">
      <SideBar />
      <div className="wardContainer">
        <Navbar />
        <div>
          <WardTable />
        </div>
      </div>
    </div>
  );
}

export default Ward;
