import { CardContent, Grid, Typography } from "@mui/material";
import React from "react";

import "./VitalSign.scss";

const VitalSignView = ({ selectedRow }) => {
  const {
    patient_id,
    doctor_id,
    heart_rate,
    blood_pressure_systolic,
    blood_pressure_diastolic,
    respiratory_rate,
    temperature,
    height,
    weight,
    oxygen_saturation,
    recorded_at,
  } = selectedRow;

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Vital Sign Information
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Details about your vital sign.
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
              <Typography variant="body1">Heart Rate: {heart_rate}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                {" "}
                Blood Pressure Systolic: {blood_pressure_systolic}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Blood Pressure Dyastolic: {blood_pressure_diastolic}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Respiratory Rate: {respiratory_rate}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Temperature: {temperature}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Height: {height}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Weight: {weight}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Oxygen Saturation: {oxygen_saturation}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Recorded At: {recorded_at}
              </Typography>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default VitalSignView;
