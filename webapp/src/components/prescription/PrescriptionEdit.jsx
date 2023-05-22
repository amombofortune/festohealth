import {
  Button,
  CardContent,
  Grid,
  TextField,
  Typography,
} from "@mui/material";
import React, { useState } from "react";
import axios from "axios";

import "./Prescription.scss";

const PrescriptionEdit = ({ selectedRow }) => {
  const { doctor_id, patient_id, medication, dosage, instructions } =
    selectedRow;

  const [doctorID, setDoctorID] = useState(doctor_id);
  const [patientID, setPatientID] = useState(patient_id);
  const [medicationValue, setMedication] = useState(medication);
  const [dosageValue, setDosage] = useState(dosage);
  const [instructionsValue, setInstructions] = useState(instructions);

  //Update record
  const handleUpdate = async () => {
    const appointmentData = {
      doctor_id: doctorID,
      patient_id: patientID,
      medication: medicationValue,
      dosage: dosageValue,
      instructions: instructionsValue,
    };

    try {
      const res = await axios.put(
        `http://127.0.0.1:8000/prescription/${selectedRow.id}`,
        appointmentData
      );
      console.log("Updated!!", res);
      window.location.reload(true);
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Are you sure you want to update prescription information?
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Edit out this form and we will update prescription information.
        </Typography>
        <form onSubmit={handleUpdate} style={{ marginTop: "10px" }}>
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Doctor ID"
                placeholder="Enter Doctor ID"
                variant="outlined"
                type="number"
                value={doctorID}
                onChange={(event) => {
                  setDoctorID(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Patient ID"
                placeholder="Enter Patient ID"
                variant="outlined"
                type="number"
                value={patientID}
                onChange={(event) => {
                  setPatientID(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                label="Medication"
                placeholder="Enter Medication"
                variant="outlined"
                type="text"
                value={medicationValue}
                onChange={(event) => {
                  setMedication(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Dosage"
                placeholder="Enter Dosage"
                variant="outlined"
                type="text"
                value={dosageValue}
                onChange={(event) => {
                  setDosage(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Instructions"
                helperText="Enter Instructions"
                variant="outlined"
                type="text"
                value={instructionsValue}
                onChange={(event) => {
                  setInstructions(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>

            <Grid xs={12} item>
              <Button
                type="submit"
                variant="contained"
                color="primary"
                fullWidth
              >
                Update
              </Button>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default PrescriptionEdit;
