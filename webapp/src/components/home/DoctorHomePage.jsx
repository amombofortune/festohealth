import React from "react";
import "./home.scss";
import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";

function DoctorHomePage() {
  return (
    <div className="homepage">
      <SideBar />
      <div className="homepageContainer">
        <Navbar />
        <div classname="appointmentTable">DoctorHomePage</div>
      </div>
    </div>
  );
}

export default DoctorHomePage;
