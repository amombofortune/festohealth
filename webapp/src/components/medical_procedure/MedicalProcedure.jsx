import React from "react";

import "./MedicalProcedure.scss";

import MedicalProcedureTable from "./MedicalProcedureTable";
import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";

function MedicalProcedure() {
  return (
    <div className="medicalProcedure">
      <SideBar />
      <div className="medicalProcedureContainer">
        <Navbar />

        <div>
          <MedicalProcedureTable />
        </div>
      </div>
    </div>
  );
}

export default MedicalProcedure;
