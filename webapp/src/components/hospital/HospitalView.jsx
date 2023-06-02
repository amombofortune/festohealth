import { CardContent, Grid, Typography } from "@mui/material";
import React from "react";

import "./Hospital.scss";

const HospitalView = ({ selectedRow }) => {
  const {
    name,
    address,
    city,
    state,
    postal_code,
    country,
    phone_number,
    website,
    rating,
  } = selectedRow;

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Hospital Information
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Details about hospital.
        </Typography>
        <form>
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">First Name: {name}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Address: {address}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">City: {city}</Typography>
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
              <Typography variant="body1">Websiter: {website}</Typography>
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

export default HospitalView;
