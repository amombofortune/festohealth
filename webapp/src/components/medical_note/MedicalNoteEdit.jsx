import {
  Button,
  CardContent,
  Grid,
  TextField,
  Typography,
} from "@mui/material";
import React, { useState } from "react";
import axios from "axios";

import "./MedicalNote.scss";

const MedicalNoteEdit = ({ selectedRow }) => {
  const { patient_id, doctor_id, date, content } = selectedRow;

  const [patientID, setPatientID] = useState(patient_id);
  const [doctorID, setDoctorID] = useState(doctor_id);
  const [dateValue, setDate] = useState(date);
  const [contentValue, setContent] = useState(content);

  //Update record
  const handleUpdate = async () => {
    const appointmentData = {
      patient_id: patientID,
      doctor_id: doctorID,
      date: dateValue,
      content: contentValue,
    };

    try {
      const res = await axios.put(
        `http://127.0.0.1:8000/medical_note/${selectedRow.id}`,
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
          Are you sure you want to update medical note?
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Edit out this form and we will update medical note.
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
                label="Content"
                helperText="Enter Content"
                variant="outlined"
                type="text"
                value={contentValue}
                onChange={(event) => {
                  setContent(event.target.value);
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

export default MedicalNoteEdit;
