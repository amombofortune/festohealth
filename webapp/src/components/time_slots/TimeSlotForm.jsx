import {
  Button,
  CardContent,
  Grid,
  TextField,
  Typography,
} from "@mui/material";
import React, { useState } from "react";
import axios from "axios";
import "./timeslot.scss";

const TimeSlotForm = () => {
  const [doctor_id, setDoctorID] = useState("");
  const [date, setDate] = useState("");
  const [start_time, setStartTime] = useState("08:00 AM");
  const [end_time, setEndTime] = useState("05:00 PM");
  const [availability, setAvailability] = useState("");
  const [selectedStartTime, setSelectedStartTime] = useState(null);
  const [selectedEndTime, setSelectedEndTime] = useState(null);

  //Post data to database
  const handleSubmit = async (e) => {
    e.preventDefault();

    setStartTime(start_time);
    setEndTime(end_time);

    console.log("Doctor ID:", doctor_id);
    console.log("Date:", date);
    console.log("Start Time:", start_time);
    console.log("End Time:", end_time);
    console.log("Is Available:", availability);

    await axios
      .post("http://127.0.0.1:8000/time_slot", {
        doctor_id,
        date,
        start_time: selectedStartTime,
        end_time: selectedEndTime,
        availability,
      })
      .then((res) => {
        window.location.reload(true);
        console.log("Posting data to database successful!!!", res);
      })
      .catch((err) => console.log(err));
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

      const timeSlot = `${startTimeString} - ${endTimeString}`;
      timeSlots.push(timeSlot);
    }

    return timeSlots;
  };

  // Set the interval value according to your requirements
  const interval = 60; //60 minutes
  // Define the available time slots
  const availableTimeSlots = generateTimeSlots(start_time, end_time, interval);

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
          Time Slot Form
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Fill out the form to record time slot.
        </Typography>
        <form onSubmit={handleSubmit} className="admission_form">
          <Grid container spacing={1}>
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
                helperText="Enter  Date"
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
                helperText="Enter Availability"
                variant="outlined"
                type="text"
                value={availability}
                onChange={(event) => {
                  setAvailability(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>

            <Grid xs={12} item>
              <Button
                style={{ backgroundColor: "#6439ff" }}
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

export default TimeSlotForm;
