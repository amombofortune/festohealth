import { CardContent, Grid, Typography } from "@mui/material";
import React from "react";

import "./Disease.scss";

const DiseaseView = ({ selectedRow }) => {
  const { name, description, symptoms, treatment, prevention } = selectedRow;

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Disease Information
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Details about disease.
        </Typography>
        <form>
          <Grid container spacing={1}>
            <Grid xs={12} item>
              <Typography variant="body1">Name: {name}</Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">
                Description: {description}
              </Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">Symptoms: {symptoms}</Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">Treatment: {treatment}</Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">Prevention: {prevention}</Typography>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default DiseaseView;
