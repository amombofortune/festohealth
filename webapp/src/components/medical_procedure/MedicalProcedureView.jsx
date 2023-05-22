import { CardContent, Grid, Typography } from "@mui/material";
import React from "react";

import "./MedicalProcedure.scss";

const MedicalProcedureView = ({ selectedRow }) => {
  const { patient_id, doctor_id, name, date, notes } = selectedRow;

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Medical Procedure Information
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Details about medical procedure.
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
              <Typography variant="body1">Name: {name}</Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">Date: {date}</Typography>
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

export default MedicalProcedureView;
