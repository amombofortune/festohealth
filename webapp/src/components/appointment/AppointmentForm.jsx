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
import "./appointment.scss";

const AppointmentForm = () => {
  const [patient_id, setPatientID] = useState("");
  const [doctor_id, setDoctorID] = useState("");
  const [appointment_type, setAppointmentType] = useState("");
  const [appointment_date, setAppointmentDate] = useState("");
  const [appointment_start_time, setAppointmentStartTime] = useState("");
  const [appointment_end_time, setAppointmentEndTime] = useState("");
  const [description, setDescription] = useState("");
  const [status, setStatus] = useState("");

  const [appointmentTypeDB, setAppointmentTypeDB] = useState([]);

  //Post data to database
  const handleSubmit = async (e) => {
    e.preventDefault();

    await axios
      .post("http://127.0.0.1:8000/appointment", {
        patient_id,
        doctor_id,
        appointment_type,
        appointment_date,
        appointment_start_time,
        appointment_end_time,
        description,
        status,
      })
      .then((res) => {
        window.location.reload(true);
        console.log("Posting data to database successful!!!", res);
      })
      .catch((err) => console.log(err));
  };

  //Fetch appointment type
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/appointment_type")
      .then((res) => {
        console.log(
          "Fetching appointment type from database successful!!!",
          res.data
        );
        setAppointmentTypeDB(res.data);
      })
      .catch((err) => console.log(err));
  }, []);

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Appointment Booking Form
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Fill out the form to book an appointment with one of our specialists.
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
                id="appointment_type"
                select
                label="Select Appointment Type"
                value={appointment_type}
                onChange={(event) => {
                  setAppointmentType(event.target.value);
                }}
                fullWidth
              >
                {appointmentTypeDB.map((item) => (
                  <MenuItem key={item.id} value={item.name}>
                    {item.name}
                  </MenuItem>
                ))}
              </TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                helperText="Enter Appointment Date"
                variant="outlined"
                type="date"
                value={appointment_date}
                onChange={(event) => {
                  setAppointmentDate(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                helperText="Enter Appointment Start Time"
                variant="outlined"
                type="time"
                value={appointment_start_time}
                onChange={(event) => {
                  setAppointmentStartTime(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                helperText="Enter Appointment End Time"
                variant="outlined"
                type="time"
                value={appointment_end_time}
                onChange={(event) => {
                  setAppointmentEndTime(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                label="Description"
                placeholder="Enter Description"
                variant="outlined"
                type="text"
                value={description}
                onChange={(event) => {
                  setDescription(event.target.value);
                }}
                multiline
                rows={4}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                label="Status"
                placeholder="Enter Status"
                variant="outlined"
                type="text"
                value={status}
                onChange={(event) => {
                  setStatus(event.target.value);
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
                Submit
              </Button>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default AppointmentForm;
