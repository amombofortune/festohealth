import { CardContent, Grid, Typography } from "@mui/material";
import React from "react";

import "./InsuranceClaim.scss";

const InsuranceClaimView = ({ selectedRow }) => {
  const {
    patient_id,
    provider_id,
    date_of_service,
    procedure_code,
    diagnosis_code,
    billed_amount,
    insurance_paid,
    patient_paid,
    status,
  } = selectedRow;

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Insurance Claim Information
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Details about insurance claim.
        </Typography>
        <form>
          <Grid container spacing={1}>
            <Grid xs={12} item>
              <Typography variant="body1">Patient ID: {patient_id}</Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">
                Provider ID: {provider_id}
              </Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">
                Date of Service: {date_of_service}
              </Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">
                Procedure Code: {procedure_code}
              </Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">
                Diagnosis Code: {diagnosis_code}
              </Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">
                Billed Amount: {billed_amount}
              </Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">
                Insurance Paid: {insurance_paid}
              </Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">
                Patient Paid: {patient_paid}
              </Typography>
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

export default InsuranceClaimView;
