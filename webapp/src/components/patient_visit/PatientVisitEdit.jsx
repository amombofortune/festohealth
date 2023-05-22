import {
  Button,
  CardContent,
  Grid,
  TextField,
  Typography,
} from "@mui/material";
import React, { useState, useEffect } from "react";
import axios from "axios";
import MenuItem from "@mui/material/MenuItem";

import "./PatientVisit.scss";

const PatientVisitEdit = ({ selectedRow }) => {
  const {
    patient_id,
    doctor_id,
    appointment_id,
    visit_date,
    chief_complaint,
    diagnosis_id,
    notes,
  } = selectedRow;

  const [patientID, setPatientID] = useState(patient_id);
  const [doctorID, setDoctorID] = useState(doctor_id);
  const [appointmentID, setAppointmentID] = useState(appointment_id);
  const [visitDate, setVisitDate] = useState(visit_date);
  const [chiefComplaint, setChiefComplaint] = useState(chief_complaint);
  const [diagnosisID, setDiagnosisID] = useState(diagnosis_id);
  const [notesValue, setNotes] = useState(notes);

  const [appointmentIDDB, setAppointmentIDDB] = useState([]);

  //Update record
  const handleUpdate = async () => {
    const appointmentData = {
      patient_id: patientID,
      doctor_id: doctorID,
      appointment_id: appointmentID,
      visit_date: visitDate,
      chief_complaint: chiefComplaint,
      diagnosis_id: diagnosisID,
      notes: notesValue,
    };

    try {
      const res = await axios.put(
        `http://127.0.0.1:8000/patient_feedback/${selectedRow.id}`,
        appointmentData
      );
      console.log("Updated!!", res);
      window.location.reload(true);
    } catch (err) {
      console.log(err);
    }
  };

  //Fetch appointment
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/appointment")
      .then((res) => {
        console.log(
          "Fetching appointment from database successful!!!",
          res.data
        );
        setAppointmentIDDB(res.data);
      })
      .catch((err) => console.log(err));
  }, []);

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Are you sure you want to update patient feedback?
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Edit out this form and we will update patient feedback.
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
                type="number"
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
                id="appointment_id"
                select
                label="Select Appointment ID"
                value={appointmentID}
                //defaultValue="In-person"
                //helperText="Please select appointment type"
                onChange={(event) => {
                  setAppointmentID(event.target.value);
                }}
                fullWidth
              >
                {appointmentIDDB.map((item) => (
                  <MenuItem key={item.id} value={item.patient_id}>
                    {item.patient_id}
                  </MenuItem>
                ))}
              </TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                //label="Appointment Date"
                helperText="Enter Visit Date"
                variant="outlined"
                type="date"
                value={visitDate}
                onChange={(event) => {
                  setVisitDate(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Chief Complaint"
                placeholder="Enter Chief Complaint"
                variant="outlined"
                type="text"
                value={chiefComplaint}
                onChange={(event) => {
                  setChiefComplaint(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Diagnosis ID"
                helperText="Enter Diagnosis ID"
                variant="outlined"
                type="number"
                value={diagnosisID}
                onChange={(event) => {
                  setDiagnosisID(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                label="Notes"
                placeholder="Enter Notes"
                variant="outlined"
                type="text"
                value={notesValue}
                onChange={(event) => {
                  setNotes(event.target.value);
                }}
                multiline
                rows={4}
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

export default PatientVisitEdit;
