import React from "react";

import "./LabTest.scss";
import LabTestTable from "./LabTestTable";
import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";

function LabTest() {
  return (
    <div className="labTest">
      <SideBar />
      <div className="labTestContainer">
        <Navbar />
        <div classname="appointmentTable">
          <LabTestTable />
        </div>
      </div>
    </div>
  );
}

export default LabTest;
