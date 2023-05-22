import { CardContent, Grid, Typography } from "@mui/material";
import React from "react";

import "./Country.scss";

const CountryView = ({ selectedRow }) => {
  const { name, code } = selectedRow;

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Country Information
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Details about country.
        </Typography>
        <form>
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Name: {name}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Code: {code}</Typography>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default CountryView;
