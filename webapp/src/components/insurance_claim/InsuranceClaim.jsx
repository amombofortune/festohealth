import React from "react";

import "./InsuranceClaim.scss";
import InsuranceClaimTable from "./InsuranceClaimTable";
import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";

function InsuranceClaim() {
  return (
    <div className="insuranceClaim">
      <SideBar />
      <div className="insuranceClaimContainer">
        <Navbar />
        <div>
          <InsuranceClaimTable />
        </div>
      </div>
    </div>
  );
}

export default InsuranceClaim;
