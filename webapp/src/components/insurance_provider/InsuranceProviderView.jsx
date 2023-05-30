import { CardContent, Grid, Typography } from "@mui/material";
import React from "react";

import "./InsuranceProvider.scss";

const InsuranceProviderView = ({ selectedRow }) => {
  const {
    name,
    type,
    address,
    city,
    state,
    postal_code,
    country,
    phone_number,
    email,
    rating,
    website,
  } = selectedRow;

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Insurance Provider Information
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Details about insurance provider.
        </Typography>
        <form>
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Name: {name}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Type: {type}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Address: {address}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1"> City: {city}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">State: {state}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Postal Code: {postal_code}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Country: {country}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Phone Number: {phone_number}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Email: {email}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Website: {website}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Rating: {rating}</Typography>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default InsuranceProviderView;
