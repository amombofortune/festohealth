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

const WardEdit = ({ selectedRow }) => {
  const { name, type, capacity, location, hospital_id } = selectedRow;

  const [nameValue, setName] = useState(name);
  const [typeValue, setType] = useState(type);
  const [capacityValue, setCapacity] = useState(capacity);
  const [locationValue, setLocation] = useState(location);
  const [hospitalID, setHospitalID] = useState(hospital_id);

  //Update record
  const handleUpdate = async () => {
    const appointmentData = {
      name: nameValue,
      type: typeValue,
      capacity: capacityValue,
      location: locationValue,
      hospital_id: hospitalID,
    };

    try {
      const res = await axios.put(
        `http://127.0.0.1:8000/ward/${selectedRow.id}`,
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
          Are you sure you want to update ward?
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Edit out this form and we will update ward information.
        </Typography>
        <form onSubmit={handleUpdate} style={{ marginTop: "10px" }}>
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Name"
                placeholder="Enter Name"
                variant="outlined"
                type="text"
                value={nameValue}
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
                value={typeValue}
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
                value={capacityValue}
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
                value={locationValue}
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
                value={hospitalID}
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
                Update
              </Button>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default WardEdit;
