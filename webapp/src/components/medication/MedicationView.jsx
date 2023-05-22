import { CardContent, Grid, Typography } from "@mui/material";
import React from "react";

import "./Medication.scss";

const MedicationView = ({ selectedRow }) => {
  const {
    name,
    description,
    route_of_administration,
    dosage,
    unit,
    frequency,
    patient_id,
    doctor_id,
  } = selectedRow;

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Medication Information
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Details about medication.
        </Typography>
        <form>
          <Grid container spacing={1}>
            <Grid xs={12} item>
              <Typography variant="body1">Name: {name}</Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">
                Description: {description}
              </Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">
                Route of Administration: {route_of_administration}
              </Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">Dosage: {dosage}</Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">Unit: {unit}</Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">Frequency: {frequency}</Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">Patient ID: {patient_id}</Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">Doctor ID: {doctor_id}</Typography>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default MedicationView;
