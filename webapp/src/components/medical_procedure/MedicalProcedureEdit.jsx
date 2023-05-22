import {
  Button,
  CardContent,
  Grid,
  TextField,
  Typography,
} from "@mui/material";
import React, { useState } from "react";
import axios from "axios";

import "./MedicalProcedure.scss";

const MedicalProcedureEdit = ({ selectedRow }) => {
  const { patient_id, doctor_id, name, date, notes } = selectedRow;

  const [patientID, setPatientID] = useState(patient_id);
  const [doctorID, setDoctorID] = useState(doctor_id);
  const [nameValue, setName] = useState(name);
  const [dateValue, setDate] = useState(date);
  const [notesValue, setNotes] = useState(notes);

  //Update record
  const handleUpdate = async () => {
    const appointmentData = {
      patient_id: patientID,
      doctor_id: doctorID,
      name: nameValue,
      date: dateValue,
      notes: notesValue,
    };

    try {
      const res = await axios.put(
        `http://127.0.0.1:8000/medical_procedure/${selectedRow.id}`,
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
          Are you sure you want to update medical procedure?
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Edit out this form and we will update medical procedure.
        </Typography>
        <form onSubmit={handleUpdate} style={{ marginTop: "10px" }}>
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <TextField
                label=" Patient ID"
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
                label="Doctor ID"
                placeholder="Enter Doctor ID"
                variant="outlined"
                type="text"
                value={doctorID}
                onChange={(event) => {
                  setDoctorID(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                label="Name"
                placeholder="Enter Name"
                variant="outlined"
                type="text"
                value={nameValue}
                onChange={(event) => {
                  setName(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Date"
                placeholder="Enter Date"
                variant="outlined"
                type="date"
                value={dateValue}
                onChange={(event) => {
                  setDate(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Notes"
                helperText="Enter Notes"
                variant="outlined"
                type="text"
                value={notesValue}
                onChange={(event) => {
                  setNotes(event.target.value);
                }}
                fullWidth
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

export default MedicalProcedureEdit;
