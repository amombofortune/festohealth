import React from "react";
import "./Vaccination.scss";

import VaccinationTable from "./VaccinationTable";
import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";

function Vaccination() {
  return (
    <div className="vaccination">
      <SideBar />
      <div className="vaccinationContainer">
        <Navbar />
        <div>
          <VaccinationTable />
        </div>
      </div>
    </div>
  );
}

export default Vaccination;
