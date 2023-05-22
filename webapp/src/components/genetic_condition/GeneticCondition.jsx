import React from "react";
import Box from "@mui/material/Box";
import Modal from "@mui/material/Modal";
import "./GeneticCondition.scss";
import GeneticConditionForm from "./GeneticConditionForm";
import GeneticConditionTable from "./GeneticConditionTable";
import SideBar from "../sidebar/SideBar";
import Navbar from "../navbar/Navbar";

function GeneticCondition() {
  //Modal
  const [open, setOpen] = React.useState(false);
  const handleClose = () => setOpen(false);

  return (
    <div className="geneticCondition">
      <SideBar />
      <div className="geneticConditionContainer">
        <Navbar />
        <div>
          <div>
            <Modal open={open} onClose={handleClose}>
              <Box className="box">
                <GeneticConditionForm />
              </Box>
            </Modal>
          </div>
          <div>
            <GeneticConditionTable />
          </div>
        </div>
      </div>
    </div>
  );
}

export default GeneticCondition;
