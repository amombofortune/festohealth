import {
  Button,
  CardContent,
  Grid,
  TextField,
  Typography,
} from "@mui/material";
import React, { useState } from "react";
import axios from "axios";
import "./VitalSign.scss";

const VitalSignForm = () => {
  const [patient_id, setPatientID] = useState("");
  const [doctor_id, setDoctorID] = useState("");
  const [heart_rate, setHeartRate] = useState("");
  const [blood_pressure_systolic, setBloodPressureSystolic] = useState("");
  const [blood_pressure_diastolic, setBloodPressureDiastolic] = useState("");
  const [respiratory_rate, setRespiratoryRate] = useState("");
  const [temperature, setTemperature] = useState("");
  const [height, setHeight] = useState("");
  const [weight, setWeight] = useState("");
  const [oxygen_saturation, setOxygenSaturation] = useState("");
  const [recorded_at, setRecordedAt] = useState("");

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
        doctor_id,
        heart_rate,
        blood_pressure_systolic,
        blood_pressure_diastolic,
        respiratory_rate,
        temperature,
        height,
        weight,
        oxygen_saturation,
        recorded_at,
      };

      await axios.post("http://127.0.0.1:8000/vital_sign", data, {
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
          Vital Sign Form
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
                label="Doctor ID"
                placeholder="Enter Doctor ID"
                variant="outlined"
                type="text"
                value={doctor_id}
                onChange={(event) => {
                  setDoctorID(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                label="Heart Rate"
                placeholder="Enter Heart Rate"
                variant="outlined"
                type="number"
                value={heart_rate}
                onChange={(event) => {
                  setHeartRate(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Blood Pressure Systolic"
                placeholder="Enter Blood Pressure Systolic"
                variant="outlined"
                type="number"
                value={blood_pressure_systolic}
                onChange={(event) => {
                  setBloodPressureSystolic(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Blood Pressure Dyastolic"
                placeholder="Enter Blood Pressure Dyastolic"
                variant="outlined"
                type="number"
                value={blood_pressure_diastolic}
                onChange={(event) => {
                  setBloodPressureDiastolic(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Respiratory Rate"
                helperText="Enter Respiratory Rate"
                variant="outlined"
                type="number"
                value={respiratory_rate}
                onChange={(event) => {
                  setRespiratoryRate(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>

            <Grid xs={12} sm={6} item>
              <TextField
                label="Temperature"
                helperText="Enter Temperature"
                variant="outlined"
                type="number"
                value={temperature}
                onChange={(event) => {
                  setTemperature(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Height"
                helperText="Enter Height"
                variant="outlined"
                type="number"
                value={height}
                onChange={(event) => {
                  setHeight(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Weight"
                helperText="Enter Weight"
                variant="outlined"
                type="number"
                value={weight}
                onChange={(event) => {
                  setWeight(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Oxygen Saturation"
                helperText="Enter Oxygen Saturation"
                variant="outlined"
                type="number"
                value={oxygen_saturation}
                onChange={(event) => {
                  setOxygenSaturation(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Recorded At"
                helperText="Enter Recorded At"
                variant="outlined"
                type="date"
                value={recorded_at}
                onChange={(event) => {
                  setRecordedAt(event.target.value);
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

export default VitalSignForm;
