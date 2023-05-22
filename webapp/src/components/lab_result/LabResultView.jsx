import { CardContent, Grid, Typography } from "@mui/material";
import React from "react";

import "./LabResult.scss";

const LabResultView = ({ selectedRow }) => {
  const { patient_id, lab_test_name, test_date, test_result, units, comments } =
    selectedRow;

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Lab Result Information
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Details about your lab results.
        </Typography>
        <form>
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Patient ID: {patient_id}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Lab Test Name: {lab_test_name}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Test Date: {test_date}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Test Result: {test_result}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Units: {units}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Comments: {comments}</Typography>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default LabResultView;
