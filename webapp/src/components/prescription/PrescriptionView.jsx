import { CardContent, Grid, Typography } from "@mui/material";
import React from "react";

import "./Prescription.scss";

const PrescriptionView = ({ selectedRow }) => {
  const { doctor_id, patient_id, medication, dosage, instructions } =
    selectedRow;

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Prescription Information
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Details about your prescription.
        </Typography>
        <form>
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Doctor ID: {doctor_id}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Patient ID: {patient_id}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Medication: {medication}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Dosage: {dosage}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Instructions: {instructions}
              </Typography>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default PrescriptionView;
