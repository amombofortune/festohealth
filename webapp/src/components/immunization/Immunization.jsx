import React from "react";
import "./Immunization.scss";
import ImmunizationTable from "./ImmunizationTable";
import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";

function Immunization() {
  return (
    <div className="immunization">
      <SideBar />
      <div className="immunizationContainer">
        <Navbar />
        <div>
          <ImmunizationTable />
        </div>
      </div>
    </div>
  );
}

export default Immunization;
