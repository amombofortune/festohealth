import React from "react";

import "./profile.scss";

import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";
import ProfilePage from "./ProfilePage";

function Profile() {
  return (
    <div className="patient">
      <SideBar />
      <div className="patientContainer">
        <Navbar />
        <div style={{ marginTop: "20px" }}>
          <ProfilePage />
        </div>
      </div>
    </div>
  );
}

export default Profile;
