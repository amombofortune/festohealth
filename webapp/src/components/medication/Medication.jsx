import React from "react";

import "./Medication.scss";

import MedicationTable from "./MedicationTable";
import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";

function Medication() {
  return (
    <div className="medication">
      <SideBar />
      <div className="medicationContainer">
        <Navbar />
        <div>
          <MedicationTable />
        </div>
      </div>
    </div>
  );
}

export default Medication;
