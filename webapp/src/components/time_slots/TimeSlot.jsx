import React from "react";
import "./timeslot.scss";

import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";
import TimeSlotForm from "./TimeSlotForm";

function TimeSlot() {
  return (
    <div className="timeSlot">
      <SideBar />
      <div className="timeSlotContainer">
        <Navbar />
        <div>
          <TimeSlotForm />
        </div>
      </div>
    </div>
  );
}

export default TimeSlot;
