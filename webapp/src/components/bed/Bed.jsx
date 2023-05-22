import React from "react";

import "./Bed.scss";

import BedTable from "./BedTable";
import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";

function Bed() {
  return (
    <div className="bed">
      <SideBar />
      <div className="bedContainer">
        <Navbar />
        <div>
          <BedTable />
        </div>
      </div>
    </div>
  );
}

export default Bed;
