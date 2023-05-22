import React from "react";

import "./ChronicCondition.scss";

import ChronicConditionTable from "./ChronicConditionTable";
import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";

function ChronicCondition() {
  return (
    <div className="chronicCondition">
      <SideBar />
      <div className="chronicConditionContainer">
        <Navbar />
        <div>
          <ChronicConditionTable />
        </div>
      </div>
    </div>
  );
}

export default ChronicCondition;
