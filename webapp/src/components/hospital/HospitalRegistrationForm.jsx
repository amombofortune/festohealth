import React from "react";

import "./Hospital.scss";

import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";
import HospitalMultiStepForm from "./HospitalMultiStepForm";

function HospitalRegistrationForm() {
  return (
    <div className="doctor">
      <SideBar />
      <div className="doctorContainer">
        <Navbar />
        <div style={{ marginTop: "50px" }}>
          <HospitalMultiStepForm />
        </div>
      </div>
    </div>
  );
}

export default HospitalRegistrationForm;
