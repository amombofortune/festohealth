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

const LabTestEdit = ({ selectedRow }) => {
  const { test_name, test_description, test_type, test_cost } = selectedRow;

  const [testName, setTestName] = useState(test_name);
  const [testDescription, setTestDescription] = useState(test_description);
  const [testType, setTestType] = useState(test_type);
  const [testCost, setTestCost] = useState(test_cost);

  //Update record
  const handleUpdate = async () => {
    const appointmentData = {
      test_name: testName,
      test_description: testDescription,
      test_type: testType,
      test_cost: testCost,
    };

    try {
      const res = await axios.put(
        `http://127.0.0.1:8000/lab_test/${selectedRow.id}`,
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
          Are you sure you want to update lab test?
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Edit out this form and we will update your lab test.
        </Typography>
        <form onSubmit={handleUpdate} style={{ marginTop: "10px" }}>
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Test Name"
                placeholder="Enter Test Name"
                variant="outlined"
                type="text"
                value={testName}
                onChange={(event) => {
                  setTestName(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Test Description"
                placeholder="Enter Test Description"
                variant="outlined"
                type="text"
                value={testDescription}
                onChange={(event) => {
                  setTestDescription(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>

            <Grid xs={12} sm={6} item>
              <TextField
                label="Test Type"
                helperText="Enter Test Type"
                variant="outlined"
                type="text"
                value={testType}
                onChange={(event) => {
                  setTestType(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                label=" Test Cost"
                placeholder="Enter Test Cost"
                variant="outlined"
                type="number"
                value={testCost}
                onChange={(event) => {
                  setTestCost(event.target.value);
                }}
                multiline
                rows={4}
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

export default LabTestEdit;
