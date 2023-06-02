import {
  Button,
  CardContent,
  Grid,
  TextField,
  Typography,
} from "@mui/material";
import React, { useState } from "react";
import axios from "axios";
import "./Vaccination.scss";

const VaccinationForm = () => {
  const [patient_id, setPatientID] = useState("");
  const [vaccine_name, setVaccineName] = useState("");
  const [administered_by, setAdministeredBy] = useState("");
  const [administered_at, setAdministeredAt] = useState("");
  const [next_dose_due, setNextDoseDue] = useState("");

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
        administered_by,
        administered_at,
        next_dose_due,
      };

      await axios.post("http://127.0.0.1:8000/vaccination", data, {
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
          Vaccination Form
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Fill out the form to record vaccination.
        </Typography>
        <form onSubmit={handleSubmit} className="admission_form">
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Patient ID"
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
            <Grid xs={12} sm={6} item>
              <TextField
                label="Vaccine Name"
                placeholder="Enter Vaccine Name"
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
            <Grid xs={12} item>
              <TextField
                label="Administered By"
                placeholder="Enter Administered By"
                variant="outlined"
                type="text"
                value={administered_by}
                onChange={(event) => {
                  setAdministeredBy(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Administered At"
                placeholder="Enter Administered At"
                variant="outlined"
                type="date"
                value={administered_at}
                onChange={(event) => {
                  setAdministeredAt(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Next Dose Due"
                helperText="Enter Next Dose Due"
                variant="outlined"
                type="date"
                value={next_dose_due}
                onChange={(event) => {
                  setNextDoseDue(event.target.value);
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

export default VaccinationForm;
