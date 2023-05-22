import { CardContent, Grid, Typography } from "@mui/material";
import React from "react";

import "./appointment.scss";

const AppointmentView = ({ selectedRow }) => {
  const {
    patient_id,
    doctor_id,
    appointment_type,
    appointment_date,
    appointment_start_time,
    appointment_end_time,
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
              <Typography variant="body1">
                Appointment Type: {appointment_type}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Appointment Date: {appointment_date}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Appointment Start Time: {appointment_start_time}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Appointment End Time: {appointment_end_time}
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
