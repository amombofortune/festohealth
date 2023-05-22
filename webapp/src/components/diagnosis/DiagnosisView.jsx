import { CardContent, Grid, Typography } from "@mui/material";
import React from "react";

import "./diagnosis.scss";

const DiagnosisView = ({ selectedRow }) => {
  const { patient_id, disease, diagnosis, date, doctor_id, notes } =
    selectedRow;

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Diagnosis Information
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Details about your diagnosis.
        </Typography>
        <form>
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Patient ID: {patient_id}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Disease: {disease}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Diagnosis: {diagnosis}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1"> Date: {date}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Doctor ID: {doctor_id}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Notes: {notes}</Typography>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default DiagnosisView;
