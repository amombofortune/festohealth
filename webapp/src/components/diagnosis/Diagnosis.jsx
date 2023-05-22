import React from "react";

import "./diagnosis.scss";
import DiagnosisTable from "./DiagnosisTable";
import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";

function Diagnosis() {
  return (
    <div className="diagnosis">
      <SideBar />
      <div className="diagnosisContainer">
        <Navbar />
        <div classname="appointmentTable">
          <DiagnosisTable />
        </div>
      </div>
    </div>
  );
}

export default Diagnosis;
