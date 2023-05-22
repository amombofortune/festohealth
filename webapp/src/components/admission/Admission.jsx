import React from "react";

import "./admission.scss";

import AdmissionTable from "./AdmissionTable";
import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";

function Admission() {
  return (
    <div className="admission">
      <SideBar />
      <div className="admissionContainer">
        <Navbar />
        <div classname="appointmentTable">
          <AdmissionTable />
        </div>
      </div>
    </div>
  );
}

export default Admission;
