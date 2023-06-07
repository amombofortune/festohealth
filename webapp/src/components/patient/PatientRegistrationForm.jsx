import React from "react";

import "./Patient.scss";

import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";
import PatientMultiStepForm from "./PatientMultiStepForm";

function PatientRegistrationForm() {
  return (
    <div className="patient">
      <SideBar />
      <div className="patientContainer">
        <Navbar />
        <div style={{ marginTop: "50px" }}>
          <PatientMultiStepForm />
        </div>
      </div>
    </div>
  );
}

export default PatientRegistrationForm;
