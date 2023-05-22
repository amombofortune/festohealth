import React from "react";
import "./Referral.scss";

import ReferralTable from "./ReferralTable";
import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";

function Referral() {
  return (
    <div className="referral">
      <SideBar />
      <div className="referralContainer">
        <Navbar />
        <div classname="appointmentTable">
          <ReferralTable />
        </div>
      </div>
    </div>
  );
}

export default Referral;
