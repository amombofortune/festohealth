import React from "react";

import "./InsuranceProvider.scss";
import InsuranceProviderTable from "./InsuranceProviderTable";
import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";

function InsuranceProvider() {
  return (
    <div className="insuranceProvider">
      <SideBar />
      <div className="insuranceProviderContainer">
        <Navbar />
        <div classname="appointmentTable">
          <InsuranceProviderTable />
        </div>
      </div>
    </div>
  );
}

export default InsuranceProvider;
