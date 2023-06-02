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

const PatientVisitForm = () => {
  const [patient_id, setPatientID] = useState("");
  const [doctor_id, setDoctorID] = useState("");
  const [appointment_id, setAppointmentID] = useState("");
  const [visit_date, setVisitDate] = useState("");
  const [chief_complaint, setChiefComplaint] = useState("");
  const [diagnosis_id, setDiagnosisID] = useState("");
  const [notes, setNotes] = useState("");

  const [appointmentIDDB, setAppointmentIDDB] = useState([]);

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
        appointment_id,
        visit_date,
        chief_complaint,
        diagnosis_id,
        notes,
      };

      await axios.post("http://127.0.0.1:8000/patient_visit", data, {
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

  //Fetch appointment
  useEffect(() => {
    const fetchData = async () => {
      try {
        const access_token = document.cookie.replace(
          /(?:(?:^|.*;\s*)access_token\s*=\s*([^;]*).*$)|^.*$/,
          "$1"
        );

        const response = await axios.get("http://127.0.0.1:8000/appointment", {
          withCredentials: true, // Enable sending cookies with the request
          headers: {
            Authorization: `Bearer ${access_token}`, // Include the access token as a request header
          },
        });

        console.log(
          "Fetching appointment from database successful!!!",
          response.data
        );
        setAppointmentIDDB(response.data);
      } catch (error) {
        console.error("Failed to fetch country data:", error);
        // Handle error fetching admission data
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Patient Visit Form
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Fill out the form to record patient visit.
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
                type="number"
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
                id="appointment_id"
                select
                label="Select Appointment ID"
                value={appointment_id}
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
                value={visit_date}
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
                value={chief_complaint}
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
                value={diagnosis_id}
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
                value={notes}
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
                Submit
              </Button>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default PatientVisitForm;
