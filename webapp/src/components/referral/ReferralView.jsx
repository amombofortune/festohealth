import { CardContent, Grid, Typography } from "@mui/material";
import React from "react";

import "./Referral.scss";

const ReferralView = ({ selectedRow }) => {
  const {
    referring_patient,
    referred_patient,
    referring_doctor,
    referred_doctor,
    referring_hospital,
    referred_hospital,
    referral_date,
    referral_reason,
    status,
  } = selectedRow;

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Referral Information
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Details about referral.
        </Typography>
        <form>
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Referring Patient: {referring_patient}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Referred Patient: {referred_patient}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Referring Doctor: {referring_doctor}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Referred Doctor: {referred_doctor}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Referring Hospital: {referring_hospital}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Referred Hospital: {referred_hospital}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Referral Date: {referral_date}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Referral Reason: {referral_reason}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Status: {status}</Typography>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default ReferralView;
