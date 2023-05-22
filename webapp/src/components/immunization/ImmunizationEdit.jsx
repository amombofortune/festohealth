import {
  Button,
  CardContent,
  Grid,
  TextField,
  Typography,
} from "@mui/material";
import React, { useState } from "react";
import axios from "axios";

import "./Immunization.scss";

const ImmunizationEdit = ({ selectedRow }) => {
  const {
    patient_id,
    vaccine_name,
    dose_number,
    date_given,
    administering_provider,
    expiration_date,
  } = selectedRow;

  const [patientID, setPatientID] = useState(patient_id);
  const [vaccineName, setVaccineName] = useState(vaccine_name);
  const [doseNumber, setDoseNumber] = useState(dose_number);
  const [dateGiven, setDateGiven] = useState(date_given);
  const [administeringProvider, setAdministeringProvider] = useState(
    administering_provider
  );
  const [expirationDate, setExpirationDate] = useState(expiration_date);

  //Update record
  const handleUpdate = async () => {
    const appointmentData = {
      patient_id: patientID,
      vaccine_name: vaccineName,
      dose_number: doseNumber,
      date_given: dateGiven,
      administering_provider: administeringProvider,
      expiration_date: expirationDate,
    };

    try {
      const res = await axios.put(
        `http://127.0.0.1:8000/immunization/${selectedRow.id}`,
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
          Are you sure you want to update immunization?
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Edit out this form and we will update immunization.
        </Typography>
        <form onSubmit={handleUpdate} style={{ marginTop: "10px" }}>
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Patient ID"
                placeholder="Enter Patient ID"
                variant="outlined"
                type="text"
                value={patientID}
                onChange={(event) => {
                  setPatientID(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Vaccine Name"
                placeholder="Vaccine Name"
                variant="outlined"
                type="text"
                value={vaccineName}
                onChange={(event) => {
                  setVaccineName(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>

            <Grid xs={12} sm={6} item>
              <TextField
                label="Dose Number"
                placeholder="Enter Dose Number"
                variant="outlined"
                type="text"
                value={doseNumber}
                onChange={(event) => {
                  setDoseNumber(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                //label="Date Given"
                helperText="Enter Date Given"
                variant="outlined"
                type="date"
                value={dateGiven}
                onChange={(event) => {
                  setDateGiven(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Administering Provider"
                placeholder="Enter Administering Provider"
                variant="outlined"
                type="text"
                value={administeringProvider}
                onChange={(event) => {
                  setAdministeringProvider(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                //label="Expiration Date"
                helperText="Enter Expiration Date"
                variant="outlined"
                type="date"
                value={expirationDate}
                onChange={(event) => {
                  setExpirationDate(event.target.value);
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

export default ImmunizationEdit;
