import { CardContent, Grid, Typography } from "@mui/material";
import React from "react";

import "./PatientFeedback.scss";

const PatientFeedbackView = ({ selectedRow }) => {
  const { patient_id, doctor_id, date, text, rating } = selectedRow;

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Patient Feedback Information
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Details about patient feedback.
        </Typography>
        <form>
          <Grid container spacing={1}>
            <Grid xs={12} item>
              <Typography variant="body1">Patient ID: {patient_id}</Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">Doctor ID: {doctor_id}</Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">Date: {date}</Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">Text: {text}</Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">Rating: {rating}</Typography>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default PatientFeedbackView;
