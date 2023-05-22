import { CardContent, Grid, Typography } from "@mui/material";
import React from "react";

import "./Immunization.scss";

const DiseaseView = ({ selectedRow }) => {
  const {
    patient_id,
    vaccine_name,
    dose_number,
    date_given,
    administering_provider,
    expiration_date,
  } = selectedRow;

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Immunization Information
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Details about immunization.
        </Typography>
        <form>
          <Grid container spacing={1}>
            <Grid xs={12} item>
              <Typography variant="body1">Patient ID: {patient_id}</Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">
                Vaccine Name: {vaccine_name}
              </Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">
                Dose Number: {dose_number}
              </Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">Date Given: {date_given}</Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">
                Administering Provider: {administering_provider}
              </Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">
                Expiration Date: {expiration_date}
              </Typography>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default DiseaseView;
