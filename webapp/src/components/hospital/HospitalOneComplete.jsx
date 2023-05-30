import React from "react";
import "./Hospital.scss";
import SideBar from "../../components/sidebar/SideBar";
import Navbar from "../../components/navbar/Navbar";

import HospitalOne from "./HospitalOne";

const HospitalOneComplete = () => {
  return (
    <div className="list">
      <SideBar />
      <div className="listContainer">
        <Navbar />
        <div className="appointmentTable">
          <HospitalOne />
        </div>
      </div>
    </div>
  );
};

export default HospitalOneComplete;
