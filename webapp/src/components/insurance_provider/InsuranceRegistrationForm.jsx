import React from "react";

import "./InsuranceProvider.scss";

import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";
import InsuranceMultiStepForm from "./InsuranceMultiStepForm";

function InsuranceRegistrationForm() {
  return (
    <div className="patient">
      <SideBar />
      <div className="patientContainer">
        <Navbar />
        <div style={{ marginTop: "50px" }}>
          <InsuranceMultiStepForm />
        </div>
      </div>
    </div>
  );
}

export default InsuranceRegistrationForm;
