import {
  Button,
  CardContent,
  Grid,
  TextField,
  Typography,
} from "@mui/material";
import React, { useState } from "react";
import axios from "axios";

import "./Department.scss";

const DepartmentEdit = ({ selectedRow }) => {
  const { name, description, hospital, head_doctor } = selectedRow;

  const [nameValue, setName] = useState(name);
  const [descriptionValue, setDescription] = useState(description);
  const [hospitalValue, setHospital] = useState(hospital);
  const [headDoctor, setHeadDoctor] = useState(head_doctor);

  //Update record
  const handleUpdate = async () => {
    const appointmentData = {
      name: nameValue,
      description: descriptionValue,
      hospital: hospitalValue,
      head_doctor: headDoctor,
    };

    try {
      const res = await axios.put(
        `http://127.0.0.1:8000/department/${selectedRow.id}`,
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
          Are you sure you want to update department?
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Edit out this form and we will update department.
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
                label="description"
                placeholder="Enter Description"
                variant="outlined"
                type="text"
                value={descriptionValue}
                onChange={(event) => {
                  setDescription(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="hospital"
                placeholder="Enter Hospital"
                variant="outlined"
                type="text"
                value={hospitalValue}
                onChange={(event) => {
                  setHospital(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="head doctor"
                placeholder="Enter Head Doctor"
                variant="outlined"
                type="text"
                value={headDoctor}
                onChange={(event) => {
                  setHeadDoctor(event.target.value);
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

export default DepartmentEdit;
