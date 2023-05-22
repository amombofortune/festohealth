import React from "react";
import "./nurse.scss";
import SideBar from "../../components/sidebar/SideBar";
import Navbar from "../../components/navbar/Navbar";
import NurseTable from "./NurseTable";

const Nurse = () => {
  return (
    <div className="nurse">
      <SideBar />
      <div className="nurseContainer">
        <Navbar />
        <div classname="appointmentTable">
          <NurseTable />
        </div>
      </div>
    </div>
  );
};

export default Nurse;
