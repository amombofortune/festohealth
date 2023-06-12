import React, { useContext } from "react";
import "./sidebar.scss";
import SpaceDashboardIcon from "@mui/icons-material/SpaceDashboard";
import PeopleOutlineIcon from "@mui/icons-material/PeopleOutline";
import PersonIcon from "@mui/icons-material/Person";
import Person3Icon from "@mui/icons-material/Person3";
import InventoryIcon from "@mui/icons-material/Inventory";
import MedicationIcon from "@mui/icons-material/Medication";
import VaccinesIcon from "@mui/icons-material/Vaccines";
import ConstructionIcon from "@mui/icons-material/Construction";
import HowToRegIcon from "@mui/icons-material/HowToReg";
import TaskIcon from "@mui/icons-material/Task";
import LogoutIcon from "@mui/icons-material/Logout";
import { Link } from "react-router-dom";
import UserContext from "../../contexts/UserContext";

const SideBar = () => {
  const { userData } = useContext(UserContext);

  // Access user data - bring it back to get the null error
  //const { user_type } = userData;

  // Access user data
  const user_type = userData?.user_type;

  const renderPatientSidebar = () => {
    return (
      <React.Fragment>
        {/* Render patient-specific sidebar options */}
        <p className="title">MAIN</p>
        <Link to="/" style={{ textDecoration: "none" }}>
          <li>
            <SpaceDashboardIcon className="icon" />
            <span>Dashboard</span>
          </li>
        </Link>

        <p className="title">USERS</p>
        <Link to="/doctor_one" style={{ textDecoration: "none" }}>
          <li>
            <PeopleOutlineIcon className="icon" />
            <span>Doctors</span>
          </li>
        </Link>
        <p className="title">OPERATIONS</p>
        <Link to="/appointment" style={{ textDecoration: "none" }}>
          <li>
            <InventoryIcon className="icon" />
            <span>Appointments</span>
          </li>
        </Link>
        <Link to="/admission" style={{ textDecoration: "none" }}>
          <li>
            <ConstructionIcon className="icon" />
            <span>Admissions</span>
          </li>
        </Link>
        <Link to="/referral" style={{ textDecoration: "none" }}>
          <li>
            <ConstructionIcon className="icon" />
            <span>Referrals</span>
          </li>
        </Link>
        <Link to="/prescription" style={{ textDecoration: "none" }}>
          <li>
            <ConstructionIcon className="icon" />
            <span>Prescription</span>
          </li>
        </Link>
        <Link to="/diagnosis" style={{ textDecoration: "none" }}>
          <li>
            <ConstructionIcon className="icon" />
            <span>Diagnosis</span>
          </li>
        </Link>
        <Link to="/lab_test" style={{ textDecoration: "none" }}>
          <li>
            <MedicationIcon className="icon" />
            <span>Laboratory</span>
          </li>
        </Link>
        <p className="title">THIRD PARTIES</p>
        <Link to="/insurance_provider_one" style={{ textDecoration: "none" }}>
          <li>
            <HowToRegIcon className="icon" />
            <span>Insurance Providers</span>
          </li>
        </Link>
        <Link to="/hospital_one" style={{ textDecoration: "none" }}>
          <li>
            <TaskIcon className="icon" />
            <span>Hospitals</span>
          </li>
        </Link>
        <li>
          <TaskIcon className="icon" />
          <span>Pharmacies</span>
        </li>
        <p className="title">USER ACCOUNT</p>
        <Link to="/products" style={{ textDecoration: "none" }}>
          <li>
            <InventoryIcon className="icon" />
            <span>Products</span>
          </li>
        </Link>
        <li>
          <LogoutIcon className="icon" />
          <span>Log Out</span>
        </li>
      </React.Fragment>
    );
  };

  const renderDoctorSidebar = () => {
    return (
      <React.Fragment>
        {/* Render doctor-specific sidebar options */}
        <p className="title">MAIN</p>
        <Link to="/" style={{ textDecoration: "none" }}>
          <li>
            <SpaceDashboardIcon className="icon" />
            <span>Dashboard</span>
          </li>
        </Link>

        <p className="title">USERS</p>
        <Link to="/doctor_one" style={{ textDecoration: "none" }}>
          <li>
            <PeopleOutlineIcon className="icon" />
            <span>Doctors</span>
          </li>
        </Link>

        <Link to="/patient" style={{ textDecoration: "none" }}>
          <li>
            <PersonIcon className="icon" />
            <span>Patients</span>
          </li>
        </Link>
        <Link to="/nurse" style={{ textDecoration: "none" }}>
          <li>
            <Person3Icon className="icon" />
            <span>Nurses</span>
          </li>
        </Link>
        <Link to="/availability" style={{ textDecoration: "none" }}>
          <li>
            <InventoryIcon className="icon" />
            <span>Appointments</span>
          </li>
        </Link>
      </React.Fragment>
    );
  };

  const renderDefaultSidebar = () => {
    return (
      <React.Fragment>
        {/* Render default sidebar options */}
        <p className="title">MAIN</p>
        <Link to="/" style={{ textDecoration: "none" }}>
          <li>
            <SpaceDashboardIcon className="icon" />
            <span>Dashboard</span>
          </li>
        </Link>

        <p className="title">USERS</p>
        <Link to="/doctor_one" style={{ textDecoration: "none" }}>
          <li>
            <PeopleOutlineIcon className="icon" />
            <span>Doctors</span>
          </li>
        </Link>

        <Link to="/patient" style={{ textDecoration: "none" }}>
          <li>
            <PersonIcon className="icon" />
            <span>Patients</span>
          </li>
        </Link>
        <Link to="/nurse" style={{ textDecoration: "none" }}>
          <li>
            <Person3Icon className="icon" />
            <span>Nurses</span>
          </li>
        </Link>
        <p className="title">OPERATIONS</p>
        <Link to="/appointment" style={{ textDecoration: "none" }}>
          <li>
            <InventoryIcon className="icon" />
            <span>Appointments</span>
          </li>
        </Link>
        <Link to="/admission" style={{ textDecoration: "none" }}>
          <li>
            <ConstructionIcon className="icon" />
            <span>Admissions</span>
          </li>
        </Link>
        <Link to="/referral" style={{ textDecoration: "none" }}>
          <li>
            <ConstructionIcon className="icon" />
            <span>Referrals</span>
          </li>
        </Link>
        <Link to="/prescription" style={{ textDecoration: "none" }}>
          <li>
            <ConstructionIcon className="icon" />
            <span>Prescription</span>
          </li>
        </Link>
        <Link to="/diagnosis" style={{ textDecoration: "none" }}>
          <li>
            <ConstructionIcon className="icon" />
            <span>Diagnosis</span>
          </li>
        </Link>
        <Link to="/lab_test" style={{ textDecoration: "none" }}>
          <li>
            <MedicationIcon className="icon" />
            <span>Laboratory</span>
          </li>
        </Link>
        <Link to="/medical_device" style={{ textDecoration: "none" }}>
          <li>
            <VaccinesIcon className="icon" />
            <span>Medical Devices</span>
          </li>
        </Link>
        <p className="title">THIRD PARTIES</p>
        <Link to="/insurance_provider_one" style={{ textDecoration: "none" }}>
          <li>
            <HowToRegIcon className="icon" />
            <span>Insurance Providers</span>
          </li>
        </Link>
        <Link to="/hospital_one" style={{ textDecoration: "none" }}>
          <li>
            <TaskIcon className="icon" />
            <span>Hospitals</span>
          </li>
        </Link>
        <li>
          <TaskIcon className="icon" />
          <span>Pharmacies</span>
        </li>
        <p className="title">USER ACCOUNT</p>
        <Link to="/products" style={{ textDecoration: "none" }}>
          <li>
            <InventoryIcon className="icon" />
            <span>Products</span>
          </li>
        </Link>
        <li>
          <LogoutIcon className="icon" />
          <span>Log Out</span>
        </li>
      </React.Fragment>
    );
  };

  const renderSidebarContent = () => {
    switch (user_type) {
      case "patient":
        return renderPatientSidebar();
      case "doctor":
        return renderDoctorSidebar();
      default:
        return renderDefaultSidebar();
    }
  };

  return (
    <div className="sidebar">
      <div className="top">
        <Link to="/" style={{ textDecoration: "none" }}>
          <span className="logo">festohealth</span>
        </Link>
      </div>
      <hr />
      <div className="center">
        <ul>
          {/* Render sidebar content based on user role */}
          {renderSidebarContent()}

          {/* ... */}
        </ul>
      </div>
      <div className="bottom">
        <div className="colorOption"></div>
        <div className="colorOption"></div>
      </div>
    </div>
  );
};

export default SideBar;
