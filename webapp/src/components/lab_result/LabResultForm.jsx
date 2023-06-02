import {
  Button,
  CardContent,
  Grid,
  TextField,
  Typography,
} from "@mui/material";
import React, { useState } from "react";
import axios from "axios";
import "./LabResult.scss";

const LabResultForm = () => {
  const [patient_id, setPatientID] = useState("");
  const [lab_test_name, setLabTestName] = useState("");
  const [test_date, setTestDate] = useState("");
  const [test_result, setTestResult] = useState("");
  const [units, setUnits] = useState("");
  const [comments, setComments] = useState("");

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
        lab_test_name,
        test_date,
        test_result,
        units,
        comments,
      };

      await axios.post("http://127.0.0.1:8000/lab_test_result", data, {
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
          Lab Result Form
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Fill out the form to register as an insurance provider.
        </Typography>
        <form onSubmit={handleSubmit} className="admission_form">
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <TextField
                label=" Patient ID"
                placeholder="Enter Patient ID"
                variant="outlined"
                type="number"
                value={patient_id}
                onChange={(event) => {
                  setPatientID(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                label="Test Name"
                placeholder="Enter Test Name"
                variant="outlined"
                type="text"
                value={lab_test_name}
                onChange={(event) => {
                  setLabTestName(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Test Date"
                placeholder="Enter Test Date"
                variant="outlined"
                type="date"
                value={test_date}
                onChange={(event) => {
                  setTestDate(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Test Result"
                placeholder="Enter Test Result"
                variant="outlined"
                type="text"
                value={test_result}
                onChange={(event) => {
                  setTestResult(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Units"
                placeholder="Enter Units"
                variant="outlined"
                type="text"
                value={units}
                onChange={(event) => {
                  setUnits(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Comments"
                placeholder="Enter Comments"
                variant="outlined"
                type="text"
                value={comments}
                onChange={(event) => {
                  setComments(event.target.value);
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

export default LabResultForm;
