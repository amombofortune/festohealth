import { CardContent, Grid, Typography } from "@mui/material";
import React from "react";

import "./Bed.scss";

const BedView = ({ selectedRow }) => {
  const { ward, bed_no, bed_type, availability, occupied_by } = selectedRow;

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Bed Information
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Details about bed.
        </Typography>
        <form>
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Ward: {ward}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Bed Number: {bed_no}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Bed Type: {bed_type}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Availability: {availability ? "Yes" : "No"}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Occupied By: {occupied_by}
              </Typography>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default BedView;
