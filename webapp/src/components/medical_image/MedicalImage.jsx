import React from "react";

import "./MedicalImage.scss";
import MedicalImageTable from "./MedicalImageTable";
import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";

function MedicalImage() {
  return (
    <div className="medicalImage">
      <SideBar />
      <div className="medicalImageContainer">
        <Navbar />
        <div>
          <MedicalImageTable />
        </div>
      </div>
    </div>
  );
}

export default MedicalImage;
