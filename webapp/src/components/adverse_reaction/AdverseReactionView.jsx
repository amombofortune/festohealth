import { CardContent, Grid, Typography } from "@mui/material";
import React from "react";

import "./adverseReaction.scss";

const AdverseReactionView = ({ selectedRow }) => {
  const {
    patient_id,
    reaction_date,
    reaction_time,
    reaction_type,
    reaction_details,
    medication_name,
    dosage,
    severity,
    treatment,
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
              <Typography variant="body1">
                Reaction Date: {reaction_date}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Reaction Time: {reaction_time}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Reaction Type: {reaction_type}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Reaction Details: {reaction_details}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Medication Name: {medication_name}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Dosage: {dosage}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Severity: {severity}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Treatment: {treatment}</Typography>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default AdverseReactionView;
