import React from "react";

import "./adverseReaction.scss";
import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";
import AdverseReactionTable from "./AdverseReactionTable";

function AdverseReaction() {
  return (
    <div className="adverseReaction">
      <SideBar />
      <div className="adverseReactionContainer">
        <Navbar />
        <div classname="appointmentTable">
          <AdverseReactionTable />
        </div>
      </div>
    </div>
  );
}

export default AdverseReaction;
