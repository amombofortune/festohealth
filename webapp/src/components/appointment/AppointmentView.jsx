import { CardContent, Grid, Typography } from "@mui/material";
import React from "react";

import "./appointment.scss";

const AppointmentView = ({ selectedRow }) => {
  const {
    patient_id,
    doctor_id,
    type,
    date,
    start_time,
    end_time,
    description,
    status,
  } = selectedRow;

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Appointment Information
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Details about your appointment.
        </Typography>
        <form>
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Patient ID: {patient_id}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Doctor ID: {doctor_id}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Appointment Type: {type}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Appointment Date: {date}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Appointment Time: {start_time + " to " + end_time}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Description: {description}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Status: {status}</Typography>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default AppointmentView;
