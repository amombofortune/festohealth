import React from "react";
import "./PatientConsent.scss";
import PatientConsentTable from "./PatientConsentTable";
import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";

function PatientConsent() {
  return (
    <div className="patientConsent">
      <SideBar />
      <div className="patientConsentContainer">
        <Navbar />
        <div>
          <PatientConsentTable />
        </div>
      </div>
    </div>
  );
}

export default PatientConsent;
