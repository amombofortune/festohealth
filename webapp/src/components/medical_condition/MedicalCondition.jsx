import React from "react";
import Box from "@mui/material/Box";
import Modal from "@mui/material/Modal";
import "./MedicalCondition.scss";
import MedicalConditionTable from "./MedicalConditionTable";
import MedicalConditionForm from "./MedicalConditionForm";
import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";

function MedicalCondition() {
  //Modal
  const [open, setOpen] = React.useState(false);
  const handleClose = () => setOpen(false);

  return (
    <div className="medicalCondition">
      <SideBar />
      <div className="medicalConditionContainer">
        <Navbar />
        <div>
          <div>
            <Modal open={open} onClose={handleClose}>
              <Box className="box">
                <MedicalConditionForm />
              </Box>
            </Modal>
          </div>
          <div>
            <MedicalConditionTable />
          </div>
        </div>
      </div>
    </div>
  );
}

export default MedicalCondition;
