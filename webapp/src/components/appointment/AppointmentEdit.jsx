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

const AppointmentEdit = ({ selectedRow }) => {
  const {
    patient_id,
    doctor_id,
    appointment_type,
    appointment_date,
    appointment_start_time,
    appointment_end_time,
    description,
    status,
  } = selectedRow;

  const [patientID, setPatientID] = useState(patient_id);
  const [doctorID, setDoctorID] = useState(doctor_id);
  const [appointmentType, setAppointmentType] = useState(appointment_type);
  const [appointmentDate, setAppointmentDate] = useState(appointment_date);
  const [appointmentStartTime, setAppointmentStartTime] = useState(
    appointment_start_time
  );
  const [appointmentEndTime, setAppointmentEndTime] =
    useState(appointment_end_time);
  const [descriptionValue, setDescriptionValue] = useState(description);
  const [statusValue, setStatusValue] = useState(status);
  const [appointmentTypeDB, setAppointmentTypeDB] = useState([]);

  //Update record
  const handleUpdate = async () => {
    const appointmentData = {
      patient_id: patientID,
      doctor_id: doctorID,
      appointment_type: appointmentType,
      appointment_date: appointmentDate,
      appointment_start_time: appointmentStartTime,
      appointment_end_time: appointmentEndTime,
      description: descriptionValue,
      status: statusValue,
    };

    try {
      const res = await axios.put(
        `http://127.0.0.1:8000/appointment/${selectedRow.id}`,
        appointmentData
      );
      console.log("Updated!!", res);
      window.location.reload(true);
    } catch (err) {
      console.log(err);
    }
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
          Are you sure you want to update appointment?
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Edit out this form and we will update your appointment.
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
                id="appointmentType"
                select
                label="Select Appointment Type"
                value={appointmentType}
                //defaultValue="In-person"
                //helperText="Please select appointment type"
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
                //label="Appointment Date"
                helperText="Enter Appointment Date"
                variant="outlined"
                type="date"
                value={appointmentDate}
                onChange={(event) => {
                  setAppointmentDate(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                //label="Start Time"
                helperText="Enter Appointment Start Time"
                variant="outlined"
                type="time"
                value={appointmentStartTime}
                onChange={(event) => {
                  setAppointmentStartTime(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                //label="End Time"
                helperText="Enter Appointment End Time"
                variant="outlined"
                type="time"
                value={appointmentEndTime}
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
                value={descriptionValue}
                onChange={(event) => {
                  setDescriptionValue(event.target.value);
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
                value={statusValue}
                onChange={(event) => {
                  setStatusValue(event.target.value);
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

export default AppointmentEdit;
