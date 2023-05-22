import React from "react";
import "./PatientFeedback.scss";
import PatientFeedbackTable from "./PatientFeedbackTable";
import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";

function PatientFeedback() {
  return (
    <div className="patientFeedback">
      <SideBar />
      <div className="patientFeedbackContainer">
        <Navbar />
        <div>
          <PatientFeedbackTable />
        </div>
      </div>
    </div>
  );
}

export default PatientFeedback;
