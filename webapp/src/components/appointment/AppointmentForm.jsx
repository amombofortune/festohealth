import {
  Button,
  CardContent,
  Grid,
  TextField,
  Typography,
} from "@mui/material";
import React, { useState, useEffect, useContext } from "react";
import axios from "axios";
import MenuItem from "@mui/material/MenuItem";
import "./appointment.scss";
import UserContext from "../../contexts/UserContext";

const AppointmentForm = (props) => {
  const [patient_id, setPatientID] = useState("");
  const [doctor_id, setDoctorID] = useState(props.doctor_id);
  const [type, setAppointmentType] = useState("");
  const [date, setAppointmentDate] = useState("");
  const [description, setDescription] = useState("");
  const [status, setStatus] = useState("");
  const [selectedStartTime, setSelectedStartTime] = useState(null);
  const [selectedEndTime, setSelectedEndTime] = useState(null);
  const [appointmentTypeDB, setAppointmentTypeDB] = useState([]);

  const { userData } = useContext(UserContext);

  useEffect(() => {
    if (userData && userData.user_id) {
      // Access user data and set initial values
      const { user_id } = userData;
      setPatientID(user_id);
      // Set other initial values...
    }
  }, [userData]);

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
        type,
        date,
        start_time: selectedStartTime, // Use selected start time
        end_time: selectedEndTime, // Use selected end time
        description,
        status,
      };

      await axios.post("http://127.0.0.1:8000/appointment", data, {
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

  //Fetch appointment type
  useEffect(() => {
    const fetchData = async () => {
      try {
        const access_token = document.cookie.replace(
          /(?:(?:^|.*;\s*)access_token\s*=\s*([^;]*).*$)|^.*$/,
          "$1"
        );

        const response = await axios.get(
          "http://127.0.0.1:8000/appointment_type",
          {
            withCredentials: true, // Enable sending cookies with the request
            headers: {
              Authorization: `Bearer ${access_token}`, // Include the access token as a request header
            },
          }
        );

        console.log(
          "Fetching reaction type from database successful!!!",
          response.data
        );
        setAppointmentTypeDB(response.data);
      } catch (error) {
        console.error("Failed to fetch reaction type data:", error);
        // Handle error fetching admission data
      }
    };

    fetchData();
  }, []);

  const generateTimeSlots = (start, end, interval) => {
    const startTime = new Date(`01/01/2023 ${start}`);
    const endTime = new Date(`01/01/2023 ${end}`);

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

  // Set the interval value according to your requirements
  const interval = 60; //60 minutes
  // Define the available time slots
  const availableTimeSlots = generateTimeSlots(
    "08:00 AM",
    "05:00 PM",
    interval
  );

  function chunkArray(array, chunkSize) {
    const chunks = [];
    for (let i = 0; i < array.length; i += chunkSize) {
      chunks.push(array.slice(i, i + chunkSize));
    }
    return chunks;
  }

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
                value={userData.user_id}
                onChange={(event) => {
                  setPatientID(event.target.value);
                }}
                fullWidth
                required
                disabled
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
                disabled
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                id="appointment_type"
                select
                label="Select Appointment Type"
                value={type}
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
                value={date}
                onChange={(event) => {
                  setAppointmentDate(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <h5 style={{ fontSize: "16px", marginTop: "8px" }}>
              Available Time Slots
            </h5>
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
                Book Appointment
              </Button>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default AppointmentForm;
