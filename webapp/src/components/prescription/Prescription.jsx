import React from "react";
import "./Prescription.scss";
import PrescriptionTable from "./PrescriptionTable";
import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";

function Prescription() {
  return (
    <div className="prescription">
      <SideBar />
      <div className="prescriptionContainer">
        <Navbar />
        <div>
          <PrescriptionTable />
        </div>
      </div>
    </div>
  );
}

export default Prescription;
