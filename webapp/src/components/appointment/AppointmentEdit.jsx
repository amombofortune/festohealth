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
    type,
    date,
    start_time,
    end_time,
    description,
    status,
  } = selectedRow;

  const [patientID, setPatientID] = useState(patient_id);
  const [doctorID, setDoctorID] = useState(doctor_id);
  const [appointmentType, setAppointmentType] = useState(type);
  const [appointmentDate, setAppointmentDate] = useState(date);
  const [startTime, setStartTime] = useState(start_time);
  const [endTime, setEndTime] = useState(end_time);
  const [descriptionValue, setDescriptionValue] = useState(description);
  const [statusValue, setStatusValue] = useState(status);
  const [appointmentTypeDB, setAppointmentTypeDB] = useState([]);

  const [selectedStartTime, setSelectedStartTime] = useState(null);
  const [selectedEndTime, setSelectedEndTime] = useState(null);

  const generateTimeSlots = (start, end, interval) => {
    const startTime = new Date(`01/01/2023  08:00 AM`);
    const endTime = new Date(`01/01/2023  05:00 PM`);

    const timeSlots = [];
    let currentTime = startTime;

    while (currentTime <= endTime) {
      const startTimeString = currentTime.toLocaleTimeString("en-US", {
        hour: "numeric",
        minute: "numeric",
        hour12: true,
      });
      currentTime.setMinutes(currentTime.getMinutes() + interval);
      const endTimeString = currentTime.toLocaleTimeString("en-US", {
        hour: "numeric",
        minute: "numeric",
        hour12: true,
      });

      const timeSlot = `${startTimeString} - ${endTimeString}`;
      timeSlots.push(timeSlot);
    }

    return timeSlots;
  };

  useEffect(() => {
    setStartTime(start_time);
    setEndTime(end_time);
    setSelectedStartTime(start_time);
    setSelectedEndTime(end_time);
  }, [start_time, end_time]);

  const interval = 60;
  const availableTimeSlots = generateTimeSlots(start_time, end_time, interval);

  function chunkArray(array, chunkSize) {
    const chunks = [];
    for (let i = 0; i < array.length; i += chunkSize) {
      chunks.push(array.slice(i, i + chunkSize));
    }
    return chunks;
  }

  //Update record
  const handleUpdate = async () => {
    const appointmentData = {
      patient_id: patientID,
      doctor_id: doctorID,
      type: appointmentType,
      date: appointmentDate,
      start_time: selectedStartTime || startTime,
      end_time: selectedEndTime || endTime,
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
                type="text"
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
            <h5>Available Time Slots</h5>
            <Grid xs={12} item>
              <div style={{ display: "flex", flexDirection: "column" }}>
                {chunkArray(availableTimeSlots, 2).map((row, rowIndex) => (
                  <div key={rowIndex} style={{ display: "flex" }}>
                    {row.map((time) => {
                      const [startTime, endTime] = time.split(" - ");
                      const isSelected =
                        startTime === selectedStartTime &&
                        endTime === selectedEndTime;

                      return (
                        <div
                          key={time}
                          style={{
                            border: isSelected
                              ? "2px solid #6439ff"
                              : "1px solid gray",
                            borderRadius: "10px",
                            padding: "5px",
                            margin: "5px",
                            flex: 1,
                            display: "flex",
                            justifyContent: "center",
                            alignItems: "center",
                            cursor: "pointer",
                            color: isSelected ? "#6439ff" : "#2C2C2C",
                          }}
                          onClick={() => {
                            if (isSelected) {
                              // Deselect if already selected
                              setSelectedStartTime(null);
                              setSelectedEndTime(null);
                            } else {
                              // Select the time slot
                              setSelectedStartTime(startTime);
                              setSelectedEndTime(endTime);
                            }
                          }}
                        >
                          {time}
                        </div>
                      );
                    })}
                  </div>
                ))}
              </div>
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
