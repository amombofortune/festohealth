import React from "react";
import "./complete.scss";
import SideBar from "../../components/sidebar/SideBar";
import Navbar from "../../components/navbar/Navbar";

import Trial from "./Trial";

const Complete = () => {
  return (
    <div className="list">
      <SideBar />
      <div className="listContainer">
        <Navbar />
        <div className="appointmentTable">
          <Trial />
        </div>
      </div>
    </div>
  );
};

export default Complete;
