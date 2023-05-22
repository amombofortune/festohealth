import React from "react";

import "./MedicationAlert.scss";

import MedicationAlertTable from "./MedicationAlertTable";
import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";

function MedicationAlert() {
  return (
    <div className="medicationAlert">
      <SideBar />
      <div className="medicationAlertContainer">
        <Navbar />
        <div>
          <MedicationAlertTable />
        </div>
      </div>
    </div>
  );
}

export default MedicationAlert;
