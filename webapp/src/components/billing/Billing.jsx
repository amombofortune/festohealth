import React from "react";

import "./billing.scss";

import BillingTable from "./BillingTable";
import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";

function Billing() {
  return (
    <div className="billing">
      <SideBar />
      <div className="billingContainer">
        <Navbar />
        <div classname="appointmentTable">
          <BillingTable />
        </div>
      </div>
    </div>
  );
}

export default Billing;
