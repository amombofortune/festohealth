import React from "react";
import "./appointment.scss";
import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";
import AppointmentTable from "./AppointmentTable";

function Appointment() {
  return (
    <div className="appointment">
      <SideBar />
      <div className="appointmentContainer">
        <Navbar />
        <div classname="appointmentTable">
          <AppointmentTable />
        </div>
      </div>
    </div>
  );
}

export default Appointment;
