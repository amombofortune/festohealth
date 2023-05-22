import { CardContent, Grid, Typography } from "@mui/material";
import React from "react";

import "./PatientConsent.scss";

const PatientConsentView = ({ selectedRow }) => {
  const { patient_id, consent_type, consent_date, expiration_date } =
    selectedRow;

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Patient Consent Information
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Details about patient consent.
        </Typography>
        <form>
          <Grid container spacing={1}>
            <Grid xs={12} item>
              <Typography variant="body1">Patient ID: {patient_id}</Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">
                Consent Type: {consent_type}
              </Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">
                Consent Date: {consent_date}
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

export default PatientConsentView;
