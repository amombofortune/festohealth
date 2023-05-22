import { CardContent, Grid, Typography } from "@mui/material";
import React from "react";

import "./LabTest.scss";

const LabTestView = ({ selectedRow }) => {
  const { test_name, test_description, test_type, test_cost } = selectedRow;

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Lab Test Information
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Details about your lab test.
        </Typography>
        <form>
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Test Description: {test_name}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Amount Due: {test_description}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Test Type: {test_type}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Test Cost: {test_cost}</Typography>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default LabTestView;
