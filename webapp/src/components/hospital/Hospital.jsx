import React from "react";
import "./Hospital.scss";
import HospitalTable from "./HospitalTable";
import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";

function Hospital() {
  return (
    <div className="hospital">
      <SideBar />
      <div className="hospitalContainer">
        <Navbar />
        <div classname="appointmentTable">
          <HospitalTable />
        </div>
      </div>
    </div>
  );
}

export default Hospital;
