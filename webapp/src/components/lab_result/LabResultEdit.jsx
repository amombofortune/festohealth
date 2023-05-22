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

const LabResultEdit = ({ selectedRow }) => {
  const { patient_id, lab_test_name, test_date, test_result, units, comments } =
    selectedRow;

  const [patientID, setPatientID] = useState(patient_id);
  const [labTestName, setLabTestName] = useState(lab_test_name);
  const [testDate, setTestDate] = useState(test_date);
  const [testResult, setTestResult] = useState(test_result);
  const [unitsValue, setUnits] = useState(units);
  const [commentsValue, setComments] = useState(comments);

  //Update record
  const handleUpdate = async () => {
    const appointmentData = {
      patient_id: patientID,
      lab_test_name: labTestName,
      test_date: testDate,
      test_result: testResult,
      units: unitsValue,
      comments: commentsValue,
    };

    try {
      const res = await axios.put(
        `http://127.0.0.1:8000/lab_test_result/${selectedRow.id}`,
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
          Are you sure you want to update lab test result?
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Edit out this form and we will update your lab test result.
        </Typography>
        <form onSubmit={handleUpdate} style={{ marginTop: "10px" }}>
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <TextField
                label=" Patient ID"
                placeholder="Enter Patient ID"
                variant="outlined"
                type="number"
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
                label="Test Name"
                placeholder="Enter Test Name"
                variant="outlined"
                type="text"
                value={labTestName}
                onChange={(event) => {
                  setLabTestName(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Test Date"
                placeholder="Enter Test Date"
                variant="outlined"
                type="date"
                value={testDate}
                onChange={(event) => {
                  setTestDate(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>

            <Grid xs={12} sm={6} item>
              <TextField
                label="Test Result"
                placeholder="Enter Test Result"
                variant="outlined"
                type="text"
                value={testResult}
                onChange={(event) => {
                  setTestResult(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                label="Units"
                placeholder="Enter Units"
                variant="outlined"
                type="text"
                value={unitsValue}
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
                value={commentsValue}
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

export default LabResultEdit;
