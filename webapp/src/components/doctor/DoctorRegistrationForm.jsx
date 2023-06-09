import React from "react";

import "./Doctor.scss";

import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";
import DoctorMultiStepForm from "./DoctorMultiStepForm";

function DoctorRegistrationForm() {
  return (
    <div className="doctor">
      <SideBar />
      <div className="doctorContainer">
        <Navbar />
        <div style={{ marginTop: "50px" }}>
          <DoctorMultiStepForm />
        </div>
      </div>
    </div>
  );
}

export default DoctorRegistrationForm;
