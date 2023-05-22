import {
  Button,
  CardContent,
  Grid,
  TextField,
  Typography,
} from "@mui/material";
import React, { useState } from "react";
import axios from "axios";
import "./MedicationAlert.scss";

const MedicationAlertForm = () => {
  const [patient_id, setPatientID] = useState("");
  const [medication_id, setMedicationID] = useState("");
  const [dosage, setDosage] = useState("");
  const [frequency, setFrequency] = useState("");
  const [alert_date, setAlertDate] = useState("");
  const [alert_text, setAlertText] = useState("");
  const [status, setStatus] = useState("");

  //Post data to database
  const handleSubmit = async (e) => {
    e.preventDefault();

    await axios
      .post("http://127.0.0.1:8000/medical_alert", {
        patient_id,
        medication_id,
        dosage,
        frequency,
        alert_date,
        alert_text,
        status,
      })
      .then((res) => {
        window.location.reload(true);
        console.log("Posting data to database successful!!!", res);
      })
      .catch((err) => console.log(err));
  };

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Medication Alert Form
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Fill out the form to administer medication to a patient.
        </Typography>
        <form onSubmit={handleSubmit} className="admission_form">
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <TextField
                label=" Patient ID"
                placeholder="Enter Patient ID"
                variant="outlined"
                type="number"
                value={patient_id}
                onChange={(event) => {
                  setPatientID(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                label="Medication ID"
                placeholder="Enter Medication ID"
                variant="outlined"
                type="number"
                value={medication_id}
                onChange={(event) => {
                  setMedicationID(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                label="Dosage"
                placeholder="Enter Dosage"
                variant="outlined"
                type="text"
                value={dosage}
                onChange={(event) => {
                  setDosage(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Frequency"
                placeholder="Enter Frequency"
                variant="outlined"
                type="frequency"
                value={frequency}
                onChange={(event) => {
                  setFrequency(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Alert Date"
                helperText="Enter Alert Date"
                variant="outlined"
                type="date"
                value={alert_date}
                onChange={(event) => {
                  setAlertDate(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Alert Text"
                helperText="Enter Alert Text"
                variant="outlined"
                type="text"
                value={alert_text}
                onChange={(event) => {
                  setAlertText(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Status"
                helperText="Enter Status"
                variant="outlined"
                type="text"
                value={status}
                onChange={(event) => {
                  setStatus(event.target.value);
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
                Submit
              </Button>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default MedicationAlertForm;
