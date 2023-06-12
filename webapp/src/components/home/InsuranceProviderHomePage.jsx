import React from "react";
import "./home.scss";
import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";

function InsuranceProviderHomePage() {
  return (
    <div className="homepage">
      <SideBar />
      <div className="homepageContainer">
        <Navbar />
        <div classname="appointmentTable">InsuranceProviderHomePage</div>
      </div>
    </div>
  );
}

export default InsuranceProviderHomePage;
