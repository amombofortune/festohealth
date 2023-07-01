import React from "react";
import "./home.scss";
import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";

function HospitalHomePage() {
  return (
    <div className="homepage">
      <SideBar />
      <div className="homepageContainer">
        <Navbar />
        <div classname="appointmentTable">HospitalHomePage</div>
      </div>
    </div>
  );
}

export default HospitalHomePage;
