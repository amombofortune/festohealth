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

const DepartmentForm = () => {
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [hospital, setHospital] = useState("");
  const [head_doctor, setHeadDoctor] = useState("");

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
        name,
        description,
        hospital,
        head_doctor,
      };

      await axios.post("http://127.0.0.1:8000/department", data, {
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

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Chronic Condition Form
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Fill out the form to add a chronic condition.
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
                label="description"
                placeholder="Enter Description"
                variant="outlined"
                type="text"
                value={description}
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
                value={hospital}
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
                value={head_doctor}
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
                Submit
              </Button>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default DepartmentForm;
