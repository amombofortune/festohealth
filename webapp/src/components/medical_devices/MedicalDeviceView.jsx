import { CardContent, Grid, Typography } from "@mui/material";
import React from "react";

import "./MedicalDevice.scss";

const MedicalDeviceView = ({ selectedRow }) => {
  const {
    name,
    manufacturer,
    model,
    serial_number,
    hospital,
    department,
    last_maintenance,
    next_maintenance,
  } = selectedRow;

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Medical Device Information
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Details about medical device.
        </Typography>
        <form>
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Name: {name}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Manufacturer: {manufacturer}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Model: {model}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                {" "}
                Serial Number: {serial_number}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Hospital: {hospital}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Department: {department}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Last Maintenance: {last_maintenance}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Next Maintenance: {next_maintenance}
              </Typography>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default MedicalDeviceView;
