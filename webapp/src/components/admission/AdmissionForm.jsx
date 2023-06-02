import {
  Button,
  CardContent,
  Grid,
  TextField,
  Typography,
} from "@mui/material";
import React, { useState } from "react";
import axios from "axios";
import "./admission.scss";

const AdmissionForm = () => {
  const [patient_id, setPatientID] = useState("");
  const [admission_date, setAdmissionDate] = useState("");
  const [admission_time, setAdmissionTime] = useState("");
  const [discharge_date, setDischargeDate] = useState("");
  const [discharge_time, setDischargeTime] = useState("");
  const [reason, setReason] = useState("");
  const [diagnosis, setDiagnosis] = useState("");
  const [treatment, setTreatment] = useState("");
  const [doctor_id, setDoctorID] = useState("");

  //post data to database
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
        admission_date,
        admission_time,
        discharge_date,
        discharge_time,
        reason,
        diagnosis,
        treatment,
        doctor_id,
      };

      await axios.post("http://127.0.0.1:8000/admission", data, {
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
          Patient Admission Form
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Fill out the form to admit patient.
        </Typography>
        <form onSubmit={handleSubmit} className="admission_form">
          <Grid container spacing={1}>
            <Grid xs={12} item>
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
                //label="Admission Date"
                helperText="Enter Admission Date"
                variant="outlined"
                type="date"
                value={admission_date}
                onChange={(event) => {
                  setAdmissionDate(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                //label="Admission Time"
                helperText="Enter Admission Time"
                variant="outlined"
                type="time"
                value={admission_time}
                onChange={(event) => {
                  setAdmissionTime(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                //label="Discharge Date"
                helperText="Enter Discharge Date"
                variant="outlined"
                type="date"
                value={discharge_date}
                onChange={(event) => {
                  setDischargeDate(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                //label="Discharge Time"
                helperText="Enter Discharge Time"
                variant="outlined"
                type="time"
                value={discharge_time}
                onChange={(event) => {
                  setDischargeTime(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                label="Reason"
                placeholder="Enter Reason"
                variant="outlined"
                type="text"
                value={reason}
                onChange={(event) => {
                  setReason(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                label="Diagnosis"
                placeholder="Enter Diagnosis"
                variant="outlined"
                type="text"
                value={diagnosis}
                onChange={(event) => {
                  setDiagnosis(event.target.value);
                }}
                multiline
                rows={4}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                label="Treatment"
                placeholder="Enter Treatment"
                variant="outlined"
                type="text"
                value={treatment}
                onChange={(event) => {
                  setTreatment(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} item>
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

export default AdmissionForm;
