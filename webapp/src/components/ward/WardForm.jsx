import {
  Button,
  CardContent,
  Grid,
  TextField,
  Typography,
} from "@mui/material";
import React, { useState } from "react";
import axios from "axios";
import "./Ward.scss";

const WardForm = () => {
  const [name, setName] = useState("");
  const [type, setType] = useState("");
  const [capacity, setCapacity] = useState("");
  const [location, setLocation] = useState("");
  const [hospital_id, setHospitalID] = useState("");

  //Post data to database
  const handleSubmit = async (e) => {
    e.preventDefault();

    await axios
      .post("http://127.0.0.1:8000/ward", {
        name,
        type,
        capacity,
        location,
        hospital_id,
      })
      .then((res) => {
        window.location.reload(true);
        console.log("Posting data to database successful!!!", res);
      })
      .catch((err) => console.log(err));
  };

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Ward Form
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Fill out the form to record vaccination.
        </Typography>
        <form onSubmit={handleSubmit} className="admission_form">
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Name"
                placeholder="Enter Name"
                variant="outlined"
                type="text"
                value={name}
                onChange={(event) => {
                  setName(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Type"
                placeholder="Enter Type"
                variant="outlined"
                type="text"
                value={type}
                onChange={(event) => {
                  setType(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                label="Capacity"
                placeholder="Enter Capacity"
                variant="outlined"
                type="number"
                value={capacity}
                onChange={(event) => {
                  setCapacity(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Location"
                placeholder="Enter Location"
                variant="outlined"
                type="text"
                value={location}
                onChange={(event) => {
                  setLocation(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Hospital ID"
                placeholder="Enter Hospital ID"
                variant="outlined"
                type="number"
                value={hospital_id}
                onChange={(event) => {
                  setHospitalID(event.target.value);
                }}
                fullWidth
                required
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

export default WardForm;
