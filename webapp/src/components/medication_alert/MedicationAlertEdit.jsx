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

const MedicationAlertEdit = ({ selectedRow }) => {
  const {
    patient_id,
    medication_id,
    dosage,
    frequency,
    alert_date,
    alert_text,
    status,
  } = selectedRow;

  const [patientID, setPatientID] = useState(patient_id);
  const [medicationID, setMedicationID] = useState(medication_id);
  const [dosageValue, setDosage] = useState(dosage);
  const [frequencyValue, setFrequency] = useState(frequency);
  const [alertDate, setAlertDate] = useState(alert_date);
  const [alertText, setAlertText] = useState(alert_text);
  const [statusValue, setStatus] = useState(status);

  //Update record
  const handleUpdate = async () => {
    const appointmentData = {
      patient_id: patientID,
      medication_id: medicationID,
      dosage: dosageValue,
      frequency: frequencyValue,
      alert_date: alertDate,
      alert_text: alertText,
      status: statusValue,
    };

    try {
      const res = await axios.put(
        `http://127.0.0.1:8000/medical_alert/${selectedRow.id}`,
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
          Are you sure you want to update medical alert?
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Edit out this form and we will update medical alert.
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
                label="Medication ID"
                placeholder="Enter Medication ID"
                variant="outlined"
                type="number"
                value={medicationID}
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
                value={dosageValue}
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
                value={frequencyValue}
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
                value={alertDate}
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
                value={alertText}
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
                value={statusValue}
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
                Update
              </Button>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default MedicationAlertEdit;
