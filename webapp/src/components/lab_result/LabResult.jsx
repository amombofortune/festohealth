import React from "react";
import Box from "@mui/material/Box";
import Modal from "@mui/material/Modal";
import "./LabResult.scss";
import LabResultForm from "./LabResultForm";
import LabResultTable from "./LabResultTable";
import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";

function LabResult() {
  //Modal
  const [open, setOpen] = React.useState(false);
  const handleClose = () => setOpen(false);

  return (
    <div className="labResult">
      <SideBar />
      <div className="labResultContainer">
        <Navbar />
        <div>
          <div>
            <Modal open={open} onClose={handleClose}>
              <Box className="box">
                <LabResultForm />
              </Box>
            </Modal>
          </div>
          <div>
            <LabResultTable />
          </div>
        </div>
      </div>
    </div>
  );
}

export default LabResult;
