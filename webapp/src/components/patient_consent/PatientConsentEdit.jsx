import {
  Button,
  CardContent,
  Grid,
  TextField,
  Typography,
} from "@mui/material";
import React, { useState } from "react";
import axios from "axios";

import "./PatientConsent.scss";

const PatientConsentEdit = ({ selectedRow }) => {
  const { patient_id, consent_type, consent_date, expiration_date } =
    selectedRow;

  const [patientID, setPatientID] = useState(patient_id);
  const [consentType, setConsentType] = useState(consent_type);
  const [consentDate, setConsentDate] = useState(consent_date);
  const [expirationDate, setExpirationDate] = useState(expiration_date);

  //Update record
  const handleUpdate = async () => {
    const appointmentData = {
      patient_id: patientID,
      consent_type: consentType,
      consent_date: consentDate,
      expiration_date: expirationDate,
    };

    try {
      const res = await axios.put(
        `http://127.0.0.1:8000/patient_consent/${selectedRow.id}`,
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
          Are you sure you want to update patient consent?
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Edit out this form and we will update patient consent.
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
                label="Consent Type"
                placeholder="Enter Consent Type"
                variant="outlined"
                type="text"
                value={consentType}
                onChange={(event) => {
                  setConsentType(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                helperText="Enter Consent Date"
                variant="outlined"
                type="date"
                value={consentDate}
                onChange={(event) => {
                  setConsentDate(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                helperText="Enter Expiration Date"
                variant="outlined"
                type="date"
                value={expirationDate}
                onChange={(event) => {
                  setExpirationDate(event.target.value);
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

export default PatientConsentEdit;
