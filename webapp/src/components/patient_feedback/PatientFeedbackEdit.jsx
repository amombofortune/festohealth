import {
  Button,
  CardContent,
  Grid,
  TextField,
  Typography,
} from "@mui/material";
import React, { useState } from "react";
import axios from "axios";

import "./PatientFeedback.scss";

const PatientFeedbackEdit = ({ selectedRow }) => {
  const { patient_id, doctor_id, date, text, rating } = selectedRow;

  const [patientID, setPatientID] = useState(patient_id);
  const [doctorID, setDoctorID] = useState(doctor_id);
  const [dateValue, setDate] = useState(date);
  const [textValue, setText] = useState(text);
  const [ratingValue, setRating] = useState(rating);

  //Update record
  const handleUpdate = async () => {
    const appointmentData = {
      patient_id: patientID,
      doctor_id: doctorID,
      date: dateValue,
      text: textValue,
      rating: ratingValue,
    };

    try {
      const res = await axios.put(
        `http://127.0.0.1:8000/patient_feedback/${selectedRow.id}`,
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
          Are you sure you want to update patient feedback?
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Edit out this form and we will update patient feedback.
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
                type="number"
                value={doctorID}
                onChange={(event) => {
                  setDoctorID(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                //label="Consent Date"
                helperText="Enter  Date"
                variant="outlined"
                type="date"
                value={dateValue}
                onChange={(event) => {
                  setDate(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                label="Text"
                placeholder="Enter Text"
                variant="outlined"
                type="text"
                value={textValue}
                onChange={(event) => {
                  setText(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                label="Rating"
                placeholder="Enter Rating"
                variant="outlined"
                type="number"
                value={ratingValue}
                onChange={(event) => {
                  setRating(event.target.value);
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

export default PatientFeedbackEdit;
