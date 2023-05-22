import React from "react";
import Box from "@mui/material/Box";
import Modal from "@mui/material/Modal";
import "./Doctor.scss";
import DoctorForm from "./DoctorForm";
import DoctorTable from "./DoctorTable";
import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";

function Doctor() {
  //Modal
  const [open, setOpen] = React.useState(false);
  const handleClose = () => setOpen(false);

  return (
    <div className="doctor">
      <SideBar />
      <div className="doctorContainer">
        <Navbar />
        <div>
          <div>
            <Modal open={open} onClose={handleClose}>
              <Box className="box">
                <DoctorForm />
              </Box>
            </Modal>
          </div>
          <div>
            <DoctorTable />
          </div>
        </div>
      </div>
    </div>
  );
}

export default Doctor;
