import {
  Button,
  CardContent,
  Grid,
  TextField,
  Typography,
} from "@mui/material";
import React, { useState, useContext } from "react";
import { DoctorAvailabilityContext } from "../../contexts/DoctorAvailabilityContext";
import axios from "axios";
import "./appointment.scss";

const DoctorAvailabilityForm = () => {
  const [date, setDate] = useState("");
  const [selectedStartTimes, setSelectedStartTimes] = useState([]);
  const [selectedEndTimes, setSelectedEndTimes] = useState([]);

  const { setUnavailableTimeSlots } = useContext(DoctorAvailabilityContext);

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
        date,
        start_time: selectedStartTimes,
        end_time: selectedEndTimes,
      };

      await axios.post("http://127.0.0.1:8000/availability", data, {
        withCredentials: true,
        headers,
      });

      // Update the unavailable time slots
      setUnavailableTimeSlots([...selectedStartTimes, ...selectedEndTimes]);

      window.location.reload(true);
      console.log("Posting data to database successful!!!");
    } catch (error) {
      console.error("Failed to post data to the database:", error);
      // Handle error posting data
    }
  };

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

      const timeSlot = {
        startTime: startTimeString,
        endTime: endTimeString,
      };
      timeSlots.push(timeSlot);
    }

    return timeSlots;
  };

  const interval = 60; //60 minutes
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
            <h5 style={{ fontSize: "16px", marginTop: "8px" }}>Choose Date</h5>
            <Grid xs={12} item>
              <TextField
                helperText="Enter Date"
                variant="outlined"
                type="date"
                value={date}
                onChange={(event) => {
                  setDate(event.target.value);
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
                    {row.map((timeSlot) => {
                      const { startTime, endTime } = timeSlot;
                      const isSelected =
                        selectedStartTimes.includes(startTime) &&
                        selectedEndTimes.includes(endTime);

                      return (
                        <div
                          key={`${startTime}-${endTime}`}
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
                              setSelectedStartTimes(
                                selectedStartTimes.filter(
                                  (time) => time !== startTime
                                )
                              );
                              setSelectedEndTimes(
                                selectedEndTimes.filter(
                                  (time) => time !== endTime
                                )
                              );
                            } else {
                              setSelectedStartTimes([
                                ...selectedStartTimes,
                                startTime,
                              ]);
                              setSelectedEndTimes([
                                ...selectedEndTimes,
                                endTime,
                              ]);
                            }
                          }}
                        >
                          {`${startTime} - ${endTime}`}
                        </div>
                      );
                    })}
                  </div>
                ))}
              </div>
            </Grid>

            <Grid xs={12} item>
              <Button
                type="submit"
                variant="contained"
                color="primary"
                style={{ backgroundColor: "#6439ff" }}
                fullWidth
              >
                Update Availability
              </Button>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default DoctorAvailabilityForm;
