import React from "react";
import "./InsuranceProvider.scss";
import SideBar from "../../components/sidebar/SideBar";
import Navbar from "../../components/navbar/Navbar";

import InsuranceProviderOne from "./InsuranceProviderOne";

const InsuranceProviderComplete = () => {
  return (
    <div className="list">
      <SideBar />
      <div className="listContainer">
        <Navbar />
        <div className="appointmentTable">
          <InsuranceProviderOne />
        </div>
      </div>
    </div>
  );
};

export default InsuranceProviderComplete;
