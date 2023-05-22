import React from "react";
import "./Department.scss";
import DepartmentTable from "./DepartmentTable";
import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";

function Department() {
  return (
    <div className="department">
      <SideBar />
      <div className="departmentContainer">
        <Navbar />
        <div>
          <DepartmentTable />
        </div>
      </div>
    </div>
  );
}

export default Department;
