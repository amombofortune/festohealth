import React from "react";

import "./MedicalDevice.scss";
import MedicalDeviceTable from "./MedicalDeviceTable";
import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";

function MedicalDevice() {
  return (
    <div className="medicalDevice">
      <SideBar />
      <div className="medicalDeviceContainer">
        <Navbar />
        <div classname="appointmentTable">
          <MedicalDeviceTable />
        </div>
      </div>
    </div>
  );
}

export default MedicalDevice;
