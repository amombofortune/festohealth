import React from "react";

import "./AdverseReactionType.scss";
import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";
import AdverseReactionTypeTable from "./AdverseReactionTypeTable";

function AdverseReactionType() {
  return (
    <div className="adverseReactionType">
      <SideBar />
      <div className="adverseReactionContainer">
        <Navbar />
        <div>
          <AdverseReactionTypeTable />
        </div>
      </div>
    </div>
  );
}

export default AdverseReactionType;
