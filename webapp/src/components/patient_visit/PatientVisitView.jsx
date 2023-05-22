import { CardContent, Grid, Typography } from "@mui/material";
import React from "react";

import "./PatientVisit.scss";

const PatientVisitView = ({ selectedRow }) => {
  const {
    patient_id,
    doctor_id,
    appointment_id,
    visit_date,
    chief_complaint,
    diagnosis_id,
    notes,
  } = selectedRow;

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Patient Visit Information
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Details about patient visit.
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
              <Typography variant="body1">
                Appointment ID: {appointment_id}
              </Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">Visit Date: {visit_date}</Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">
                Chief Complaint: {chief_complaint}
              </Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">
                Diagnosis ID: {diagnosis_id}
              </Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">Notes: {notes}</Typography>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default PatientVisitView;
