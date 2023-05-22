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

const AdmissionEdit = ({ selectedRow }) => {
  const {
    patient_id,
    admission_date,
    admission_time,
    discharge_date,
    discharge_time,
    reason,
    diagnosis,
    treatment,
    doctor_id,
  } = selectedRow;

  const [patientID, setPatientID] = useState(patient_id);
  const [admissionDate, setAdmissionDate] = useState(admission_date);
  const [admissionTime, setAdmissionTime] = useState(admission_time);
  const [dischargeDate, setDischargeDate] = useState(discharge_date);
  const [dischargeTime, setDischargeTime] = useState(discharge_time);
  const [reasonValue, setReasonValue] = useState(reason);
  const [diagnosisValue, setDiagnosisValue] = useState(diagnosis);
  const [treatmentValue, setTreatmentValue] = useState(treatment);
  const [doctorID, setDoctorID] = useState(doctor_id);

  //Update record
  const handleUpdate = async () => {
    const appointmentData = {
      patient_id: patientID,
      admission_date: admissionDate,
      admission_time: admissionTime,
      discharge_date: dischargeDate,
      reason: reasonValue,
      diagnosis: diagnosisValue,
      treatment: treatmentValue,
      doctor_id: doctorID,
    };

    try {
      const res = await axios.put(
        `http://127.0.0.1:8000/admission/${selectedRow.id}`,
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
          Are you sure you want to update admissions?
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Edit out this form and we will update your admission.
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
                //label="Admission Date"
                helperText="Enter Admission Date"
                variant="outlined"
                type="date"
                value={admissionDate}
                onChange={(event) => {
                  setAdmissionDate(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                //label="Admission Date"
                helperText="Enter Admission Time"
                variant="outlined"
                type="time"
                value={admissionTime}
                onChange={(event) => {
                  setAdmissionTime(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                //label="Appointment Date"
                helperText="Enter Discharge Date"
                variant="outlined"
                type="date"
                value={dischargeDate}
                onChange={(event) => {
                  setDischargeDate(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                //label="Start Time"
                helperText="Enter Discharge Time"
                variant="outlined"
                type="time"
                value={dischargeTime}
                onChange={(event) => {
                  setDischargeTime(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="End Reason"
                placeholder="Enter Reason"
                variant="outlined"
                type="text"
                value={reasonValue}
                onChange={(event) => {
                  setReasonValue(event.target.value);
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
                value={diagnosisValue}
                onChange={(event) => {
                  setDiagnosisValue(event.target.value);
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
                value={treatmentValue}
                onChange={(event) => {
                  setTreatmentValue(event.target.value);
                }}
                fullWidth
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
              <Button
                type="submit"
                variant="contained"
                color="primary"
                style={{ backgroundColor: "#6439ff" }}
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

export default AdmissionEdit;
