import { CardContent, Grid, Typography } from "@mui/material";
import React from "react";

import "./Ward.scss";

const WardView = ({ selectedRow }) => {
  const { name, type, capacity, location, hospital_id } = selectedRow;

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Ward Information
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Details about your ward.
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
              <Typography variant="body1">Capacity: {capacity}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1"> Location: {location}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Hospital ID: {hospital_id}
              </Typography>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default WardView;
