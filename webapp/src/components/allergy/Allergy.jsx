import React from "react";

import "./Allergy.scss";
import AllergyTable from "./AllergyTable";
import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";

function Allergy() {
  return (
    <div className="allergy">
      <SideBar />
      <div className="allergyContainer">
        <Navbar />
        <div>
          <AllergyTable />
        </div>
      </div>
    </div>
  );
}

export default Allergy;
