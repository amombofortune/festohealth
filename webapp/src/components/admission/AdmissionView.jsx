import { CardContent, Grid, Typography } from "@mui/material";
import React from "react";

import "./admission.scss";

const AdmissionView = ({ selectedRow }) => {
  const {
    patient_id,
    admission_date,
    admission_time,
    discharge_date,
    discharge_time,
    reason,
    diagnosis,
    treatment,
    doctor_id,
  } = selectedRow;

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Admission Information
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Details about your admission.
        </Typography>
        <form>
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Patient ID: {patient_id}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Admission Date: {admission_date}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Admission Time: {admission_time}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Discharge Date: {discharge_date}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Discharge Time: {discharge_time}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Reason: {reason}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Diagnosis: {diagnosis}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Treatment: {treatment}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Doctor ID: {doctor_id}</Typography>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default AdmissionView;
