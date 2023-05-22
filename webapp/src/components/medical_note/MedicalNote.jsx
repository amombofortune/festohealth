import React from "react";
import "./MedicalNote.scss";

import MedicalNoteTable from "./MedicalNoteTable";
import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";

function MedicalNote() {
  return (
    <div className="medicalNote">
      <SideBar />
      <div className="medicalNoteContainer">
        <Navbar />
        <div>
          <MedicalNoteTable />
        </div>
      </div>
    </div>
  );
}

export default MedicalNote;
