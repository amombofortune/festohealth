import React from "react";
import "./PatientVisit.scss";

import PatientVisitTable from "./PatientVisitTable";
import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";

function PatientVisit() {
  return (
    <div className="patientVisit">
      <SideBar />
      <div className="patientVisitContainer">
        <Navbar />
        <div>
          <PatientVisitTable />
        </div>
      </div>
    </div>
  );
}

export default PatientVisit;
