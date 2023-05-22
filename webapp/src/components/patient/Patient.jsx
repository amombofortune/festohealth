import React from "react";

import "./Patient.scss";

import PatientTable from "./PatientTable";
import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";

function Patient() {
  return (
    <div className="patient">
      <SideBar />
      <div className="patientContainer">
        <Navbar />
        <div classname="appointmentTable">
          <PatientTable />
        </div>
      </div>
    </div>
  );
}

export default Patient;
