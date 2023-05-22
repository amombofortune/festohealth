import React from "react";
import Box from "@mui/material/Box";
import Modal from "@mui/material/Modal";
import "./VitalSign.scss";
import VitalSignTable from "./VitalSignTable";
import VitalSignForm from "./VitalSignForm";
import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";

function VitalSign() {
  //Modal
  const [open, setOpen] = React.useState(false);
  const handleClose = () => setOpen(false);

  return (
    <div className="vitalSign">
      <SideBar />
      <div className="vitalSignContainer">
        <Navbar />
        <div>
          <div>
            <Modal open={open} onClose={handleClose}>
              <Box className="box">
                <VitalSignForm />
              </Box>
            </Modal>
          </div>
          <div>
            <VitalSignTable />
          </div>
        </div>
      </div>
    </div>
  );
}

export default VitalSign;
