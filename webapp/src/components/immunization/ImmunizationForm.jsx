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

const ImmunizationForm = () => {
  const [patient_id, setPatientID] = useState("");
  const [vaccine_name, setVaccineName] = useState("");
  const [dose_number, setDoseNumber] = useState("");
  const [date_given, setDateGiven] = useState("");
  const [administering_provider, setAdministeringProvider] = useState("");
  const [expiration_date, setExpirationDate] = useState("");

  //Post data to database
  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const access_token = document.cookie.replace(
        /(?:(?:^|.*;\s*)access_token\s*=\s*([^;]*).*$)|^.*$/,
        "$1"
      );

      const headers = {
        Authorization: `Bearer ${access_token}`,
        "Content-Type": "application/json",
      };

      const data = {
        patient_id,
        vaccine_name,
        dose_number,
        date_given,
        administering_provider,
        expiration_date,
      };

      await axios.post("http://127.0.0.1:8000/immunization", data, {
        withCredentials: true, // Enable sending cookies with the request
        headers,
      });

      window.location.reload(true);
      console.log("Posting data to database successful!!!");
    } catch (error) {
      console.error("Failed to post data to the database:", error);
      // Handle error posting data
    }
  };

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Immunization Form
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Fill out the form to add immunization details of patients.
        </Typography>
        <form onSubmit={handleSubmit} className="admission_form">
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Patient ID"
                placeholder="Enter Patient ID"
                variant="outlined"
                type="text"
                value={patient_id}
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
                value={vaccine_name}
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
                value={dose_number}
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
                value={date_given}
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
                value={administering_provider}
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
                value={expiration_date}
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
                Submit
              </Button>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default ImmunizationForm;
