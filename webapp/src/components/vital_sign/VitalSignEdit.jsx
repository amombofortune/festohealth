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

const VitalSignEdit = ({ selectedRow }) => {
  const {
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
  } = selectedRow;

  const [patientID, setPatientID] = useState(patient_id);
  const [doctorID, setDoctorID] = useState(doctor_id);
  const [heartRate, setHeartRate] = useState(heart_rate);
  const [bloodPressureSystolic, setBloodPressureSystolic] = useState(
    blood_pressure_systolic
  );
  const [bloodPressureDiastolic, setBloodPressureDiastolic] = useState(
    blood_pressure_diastolic
  );
  const [respiratoryRate, setRespiratoryRate] = useState(respiratory_rate);
  const [temperatureValue, setTemperature] = useState(temperature);
  const [heightValue, setHeight] = useState(height);
  const [weightValue, setWeight] = useState(weight);
  const [oxygenSaturation, setOxygenSaturation] = useState(oxygen_saturation);
  const [recordedAt, setRecordedAt] = useState(recorded_at);

  //Update record
  const handleUpdate = async () => {
    const appointmentData = {
      patient_id: patientID,
      doctor_id: doctorID,
      heart_rate: heartRate,
      blood_pressure_systolic: bloodPressureSystolic,
      blood_pressure_diastolic: bloodPressureDiastolic,
      respiratory_rate: respiratoryRate,
      temperature: temperatureValue,
      height: heightValue,
      weight: weightValue,
      oxygen_saturation: oxygenSaturation,
      recorded_at: recordedAt,
    };

    try {
      const res = await axios.put(
        `http://127.0.0.1:8000/vital_sign/${selectedRow.id}`,
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
          Are you sure you want to update vital sign?
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Edit out this form and we will update vital sign.
        </Typography>
        <form onSubmit={handleUpdate} style={{ marginTop: "10px" }}>
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Patient ID"
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
            <Grid xs={12} sm={6} item>
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
                required
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                label="Heart Rate"
                placeholder="Enter Heart Rate"
                variant="outlined"
                type="number"
                value={heartRate}
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
                value={bloodPressureSystolic}
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
                value={bloodPressureDiastolic}
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
                value={respiratoryRate}
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
                value={temperatureValue}
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
                value={heightValue}
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
                value={weightValue}
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
                value={oxygenSaturation}
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
                value={recordedAt}
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
                Update
              </Button>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default VitalSignEdit;
