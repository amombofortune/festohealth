import React from "react";
import "./Doctor.scss";
import SideBar from "../../components/sidebar/SideBar";
import Navbar from "../../components/navbar/Navbar";

import DoctorOne from "./DoctorOne";

const Complete = () => {
  return (
    <div className="list">
      <SideBar />
      <div className="listContainer">
        <Navbar />
        <div className="appointmentTable">
          <DoctorOne />
        </div>
      </div>
    </div>
  );
};

export default Complete;
