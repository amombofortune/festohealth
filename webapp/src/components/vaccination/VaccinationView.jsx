import { CardContent, Grid, Typography } from "@mui/material";
import React from "react";

import "./Vaccination.scss";

const VaccinationView = ({ selectedRow }) => {
  const {
    patient_id,
    vaccine_name,
    administered_by,
    administered_at,
    next_dose_due,
  } = selectedRow;

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Vaccination Information
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Details about your vaccination.
        </Typography>
        <form>
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Patient ID: {patient_id}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Vaccine Name: {vaccine_name}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Administered By: {administered_by}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                {" "}
                Administered At: {administered_at}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Next Dose Due: {next_dose_due}
              </Typography>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default VaccinationView;
