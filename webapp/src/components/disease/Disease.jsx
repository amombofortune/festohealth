import React from "react";
import "./Disease.scss";
import DiseaseTable from "./DiseaseTable";
import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";

function Diagnosis() {
  return (
    <div className="disease">
      <SideBar />
      <div className="diseaseContainer">
        <Navbar />
        <div>
          <DiseaseTable />
        </div>
      </div>
    </div>
  );
}

export default Diagnosis;
