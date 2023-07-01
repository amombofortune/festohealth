import React, { useContext, useState } from "react";
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
  const [showDoctorSubMenu, setShowDoctorSubMenu] = useState(false);
  const [showPatientSubMenu, setShowPatientSubMenu] = useState(false);
  const [showNurseSubMenu, setShowNurseSubMenu] = useState(false);
  const [showAppointmentSubMenu, setShowAppointmentSubMenu] = useState(false);
  const [showAdmissionSubMenu, setShowAdmissionSubMenu] = useState(false);
  const [showReferralSubMenu, setShowReferralSubMenu] = useState(false);
  const [showPrescriptionSubMenu, setShowPrescriptionSubMenu] = useState(false);
  const [showDiagnosisSubMenu, setShowDiagnosisSubMenu] = useState(false);
  const [showLaboratorySubMenu, setShowLaboratorySubMenu] = useState(false);

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
        <Link
          style={{ textDecoration: "none" }}
          onClick={() => setShowDoctorSubMenu(!showDoctorSubMenu)}
        >
          <li>
            <PeopleOutlineIcon className="icon" />
            <span>Doctors</span>
          </li>
        </Link>
        {showDoctorSubMenu && (
          <ul className="submenu">
            <li>
              <Link to="/doctor_one" style={{ textDecoration: "none" }}>
                <PeopleOutlineIcon className="icon" />
                <span>View Doctors</span>
              </Link>
            </li>
            <li>
              <Link to="/doctor_two" style={{ textDecoration: "none" }}>
                <PeopleOutlineIcon className="icon" />
                <span>Doctor 2</span>
              </Link>
            </li>
          </ul>
        )}
        <p className="title">OPERATIONS</p>
        <Link
          style={{ textDecoration: "none" }}
          onClick={() => setShowAppointmentSubMenu(!showAppointmentSubMenu)}
        >
          <li>
            <InventoryIcon className="icon" />
            <span>Appointments</span>
          </li>
        </Link>
        {showAppointmentSubMenu && (
          <ul className="submenu">
            <li>
              <Link to="/appointment" style={{ textDecoration: "none" }}>
                <InventoryIcon className="icon" />
                <span>View Appointments</span>
              </Link>
            </li>
            <li>
              <Link to="/appointment" style={{ textDecoration: "none" }}>
                <InventoryIcon className="icon" />
                <span>Book Appointment</span>
              </Link>
            </li>
          </ul>
        )}
        <Link
          style={{ textDecoration: "none" }}
          onClick={() => setShowAdmissionSubMenu(!showAdmissionSubMenu)}
        >
          <li>
            <ConstructionIcon className="icon" />
            <span>Admissions</span>
          </li>
        </Link>
        {showAdmissionSubMenu && (
          <ul className="submenu">
            <li>
              <Link to="/admission" style={{ textDecoration: "none" }}>
                <PeopleOutlineIcon className="icon" />
                <span>Admission 1</span>
              </Link>
            </li>
            <li>
              <Link to="/admission" style={{ textDecoration: "none" }}>
                <PeopleOutlineIcon className="icon" />
                <span>Admission 2</span>
              </Link>
            </li>
          </ul>
        )}
        <Link
          style={{ textDecoration: "none" }}
          onClick={() => setShowReferralSubMenu(!showReferralSubMenu)}
        >
          <li>
            <ConstructionIcon className="icon" />
            <span>Referrals</span>
          </li>
        </Link>
        {showReferralSubMenu && (
          <ul className="submenu">
            <li>
              <Link to="/referral" style={{ textDecoration: "none" }}>
                <PeopleOutlineIcon className="icon" />
                <span>Referral 1</span>
              </Link>
            </li>
            <li>
              <Link to="/referral" style={{ textDecoration: "none" }}>
                <PeopleOutlineIcon className="icon" />
                <span>Referral 2</span>
              </Link>
            </li>
          </ul>
        )}
        <Link
          style={{ textDecoration: "none" }}
          onClick={() => setShowPrescriptionSubMenu(!showPrescriptionSubMenu)}
        >
          <li>
            <ConstructionIcon className="icon" />
            <span>Prescription</span>
          </li>
        </Link>
        {showPrescriptionSubMenu && (
          <ul className="submenu">
            <li>
              <Link to="/prescription" style={{ textDecoration: "none" }}>
                <PeopleOutlineIcon className="icon" />
                <span>Prescription 1</span>
              </Link>
            </li>
            <li>
              <Link to="/prescription" style={{ textDecoration: "none" }}>
                <PeopleOutlineIcon className="icon" />
                <span>Prescription 2</span>
              </Link>
            </li>
          </ul>
        )}
        <Link
          style={{ textDecoration: "none" }}
          onClick={() => setShowDiagnosisSubMenu(!showDiagnosisSubMenu)}
        >
          <li>
            <ConstructionIcon className="icon" />
            <span>Diagnosis</span>
          </li>
        </Link>
        {showDiagnosisSubMenu && (
          <ul className="submenu">
            <li>
              <Link to="/diagnosis" style={{ textDecoration: "none" }}>
                <PeopleOutlineIcon className="icon" />
                <span>Diagnosis 1</span>
              </Link>
            </li>
            <li>
              <Link to="/diagnosis" style={{ textDecoration: "none" }}>
                <PeopleOutlineIcon className="icon" />
                <span>Diagnosis 2</span>
              </Link>
            </li>
          </ul>
        )}
        <Link
          style={{ textDecoration: "none" }}
          onClick={() => setShowLaboratorySubMenu(!showLaboratorySubMenu)}
        >
          <li>
            <MedicationIcon className="icon" />
            <span>Laboratory</span>
          </li>
        </Link>
        {showLaboratorySubMenu && (
          <ul className="submenu">
            <li>
              <Link to="/lab_test" style={{ textDecoration: "none" }}>
                <PeopleOutlineIcon className="icon" />
                <span>Laboratory 1</span>
              </Link>
            </li>
            <li>
              <Link to="/lab_test" style={{ textDecoration: "none" }}>
                <PeopleOutlineIcon className="icon" />
                <span>Laboratory 2</span>
              </Link>
            </li>
          </ul>
        )}
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
        <Link
          style={{ textDecoration: "none" }}
          onClick={() => setShowDoctorSubMenu(!showDoctorSubMenu)}
        >
          <li>
            <PeopleOutlineIcon className="icon" />
            <span>Doctors</span>
          </li>
        </Link>
        {showDoctorSubMenu && (
          <ul className="submenu">
            <li>
              <Link to="/doctor_one" style={{ textDecoration: "none" }}>
                <PeopleOutlineIcon className="icon" />
                <span>View Doctors</span>
              </Link>
            </li>
            <li>
              <Link to="/doctor_two" style={{ textDecoration: "none" }}>
                <PeopleOutlineIcon className="icon" />
                <span>Manage Doctors</span>
              </Link>
            </li>
          </ul>
        )}
        <Link
          style={{ textDecoration: "none" }}
          onClick={() => setShowPatientSubMenu(!showPatientSubMenu)}
        >
          <li>
            <PeopleOutlineIcon className="icon" />
            <span>Patients</span>
          </li>
        </Link>
        {showPatientSubMenu && (
          <ul className="submenu">
            <li>
              <Link to="/patient" style={{ textDecoration: "none" }}>
                <PeopleOutlineIcon className="icon" />
                <span>View Patients</span>
              </Link>
            </li>
            <li>
              <Link to="/patient" style={{ textDecoration: "none" }}>
                <PeopleOutlineIcon className="icon" />
                <span>Manage Patients</span>
              </Link>
            </li>
          </ul>
        )}
        <Link
          style={{ textDecoration: "none" }}
          onClick={() => setShowNurseSubMenu(!showNurseSubMenu)}
        >
          <li>
            <PeopleOutlineIcon className="icon" />
            <span>Nurse</span>
          </li>
        </Link>
        {showNurseSubMenu && (
          <ul className="submenu">
            <li>
              <Link to="/nurse" style={{ textDecoration: "none" }}>
                <PeopleOutlineIcon className="icon" />
                <span>View Nurses</span>
              </Link>
            </li>
            <li>
              <Link to="/nurse" style={{ textDecoration: "none" }}>
                <PeopleOutlineIcon className="icon" />
                <span>Manage Nurses</span>
              </Link>
            </li>
          </ul>
        )}
        <p className="title">OPERATIONS</p>
        <Link
          style={{ textDecoration: "none" }}
          onClick={() => setShowAppointmentSubMenu(!showAppointmentSubMenu)}
        >
          <li>
            <PeopleOutlineIcon className="icon" />
            <span>Appointments</span>
          </li>
        </Link>
        {showAppointmentSubMenu && (
          <ul className="submenu">
            <li>
              <Link to="/nurse" style={{ textDecoration: "none" }}>
                <InventoryIcon className="icon" />
                <span>View Appointments</span>
              </Link>
            </li>
            <li>
              <Link to="/nurse" style={{ textDecoration: "none" }}>
                <InventoryIcon className="icon" />
                <span>Manage Appointments</span>
              </Link>
            </li>
          </ul>
        )}
        <Link
          style={{ textDecoration: "none" }}
          onClick={() => setShowAdmissionSubMenu(!showAdmissionSubMenu)}
        >
          <li>
            <PeopleOutlineIcon className="icon" />
            <span>Admissions</span>
          </li>
        </Link>
        {showAdmissionSubMenu && (
          <ul className="submenu">
            <li>
              <Link to="/admission" style={{ textDecoration: "none" }}>
                <PeopleOutlineIcon className="icon" />
                <span>View Admissions</span>
              </Link>
            </li>
            <li>
              <Link to="/nurse" style={{ textDecoration: "none" }}>
                <PeopleOutlineIcon className="icon" />
                <span>Manage Admissions</span>
              </Link>
            </li>
          </ul>
        )}
        <Link
          style={{ textDecoration: "none" }}
          onClick={() => setShowReferralSubMenu(!showReferralSubMenu)}
        >
          <li>
            <PeopleOutlineIcon className="icon" />
            <span>Referrals</span>
          </li>
        </Link>
        {showReferralSubMenu && (
          <ul className="submenu">
            <li>
              <Link to="/referrals" style={{ textDecoration: "none" }}>
                <PeopleOutlineIcon className="icon" />
                <span>View Referrals</span>
              </Link>
            </li>
            <li>
              <Link to="/nurse" style={{ textDecoration: "none" }}>
                <PeopleOutlineIcon className="icon" />
                <span>Manage Referrals</span>
              </Link>
            </li>
          </ul>
        )}
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
        <Link to="/medication" style={{ textDecoration: "none" }}>
          <li>
            <ConstructionIcon className="icon" />
            <span>Medication</span>
          </li>
        </Link>
        <Link
          style={{ textDecoration: "none" }}
          onClick={() => setShowLaboratorySubMenu(!showLaboratorySubMenu)}
        >
          <li>
            <PeopleOutlineIcon className="icon" />
            <span>Laboratory</span>
          </li>
        </Link>
        {showLaboratorySubMenu && (
          <ul className="submenu">
            <li>
              <Link to="/lab_test" style={{ textDecoration: "none" }}>
                <PeopleOutlineIcon className="icon" />
                <span>Lab Tests</span>
              </Link>
            </li>
            <li>
              <Link to="/lab_results" style={{ textDecoration: "none" }}>
                <PeopleOutlineIcon className="icon" />
                <span>Lab Results</span>
              </Link>
            </li>
          </ul>
        )}
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
