import {
  Button,
  CardContent,
  Grid,
  TextField,
  Typography,
} from "@mui/material";
import React, { useState } from "react";
import axios from "axios";
import "./LabTest.scss";

const LabTestForm = () => {
  const [test_name, setTestName] = useState("");
  const [test_description, setTestDescription] = useState("");
  const [test_type, setTestType] = useState("");
  const [test_cost, setTestCost] = useState("");

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
        test_name,
        test_description,
        test_type,
        test_cost,
      };

      await axios.post("http://127.0.0.1:8000/lab_test", data, {
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
          Lab Test Form
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Fill out the form to add lab test information.
        </Typography>
        <form onSubmit={handleSubmit} className="admission_form">
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <TextField
                label=" Test Name"
                placeholder="Enter Test Name"
                variant="outlined"
                type="name"
                value={test_name}
                onChange={(event) => {
                  setTestName(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                label="Test Description"
                placeholder="Enter Test Description"
                variant="outlined"
                type="text"
                value={test_description}
                onChange={(event) => {
                  setTestDescription(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Test Type"
                placeholder="Enter Test Type"
                variant="outlined"
                type="text"
                value={test_type}
                onChange={(event) => {
                  setTestType(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Test Cost"
                placeholder="Enter Test Cost"
                variant="outlined"
                type="number"
                value={test_cost}
                onChange={(event) => {
                  setTestCost(event.target.value);
                }}
                fullWidth
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

export default LabTestForm;
