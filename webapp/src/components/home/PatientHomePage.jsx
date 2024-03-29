import React from "react";
import "./home.scss";
import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";

function PatientHomePage() {
  return (
    <div className="homepage">
      <SideBar />
      <div className="homepageContainer">
        <Navbar />
        <div className="appointmentTable">PatientHomePage</div>
      </div>
    </div>
  );
}

export default PatientHomePage;
