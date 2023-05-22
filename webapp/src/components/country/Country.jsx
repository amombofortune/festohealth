import React from "react";
import "./Country.scss";

import CountryTable from "./CountryTable";
import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";

function Country() {
  return (
    <div className="country">
      <SideBar />
      <div className="countryContainer">
        <Navbar />
        <div>
          <CountryTable />
        </div>
      </div>
    </div>
  );
}

export default Country;
