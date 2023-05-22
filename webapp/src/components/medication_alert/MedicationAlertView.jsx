import { CardContent, Grid, Typography } from "@mui/material";
import React from "react";

import "./MedicationAlert.scss";

const MedicationAlertView = ({ selectedRow }) => {
  const {
    patient_id,
    medication_id,
    dosage,
    frequency,
    alert_date,
    alert_text,
    status,
  } = selectedRow;

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Medical Alert Information
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Details about medical alert.
        </Typography>
        <form>
          <Grid container spacing={1}>
            <Grid xs={12} item>
              <Typography variant="body1">Patient ID: {patient_id}</Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">
                Medication ID: {medication_id}
              </Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">Dosage: {dosage}</Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">Frequency: {frequency}</Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">Alert Date: {alert_date}</Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">Alert Text: {alert_text}</Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">Status: {status}</Typography>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default MedicationAlertView;
