import { CardContent, Grid, Typography } from "@mui/material";
import React from "react";

import "./billing.scss";

const BillingView = ({ selectedRow }) => {
  const { patient_id, bill_date, amount_due, amount_paid, payment_method } =
    selectedRow;

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Billing Information
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Details about your billing.
        </Typography>
        <form>
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Patient ID: {patient_id}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Bill Date: {bill_date}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Amount Due: {amount_due}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Amount Paid: {amount_paid}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Payment Method: {payment_method}
              </Typography>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default BillingView;
