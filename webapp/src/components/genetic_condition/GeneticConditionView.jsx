import { CardContent, Grid, Typography } from "@mui/material";
import React from "react";

import "./GeneticCondition.scss";

const GeneticConditionView = ({ selectedRow }) => {
  const { name, description, patient_id, inheritance_pattern } = selectedRow;

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Genetic Condition Information
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Details about Genetic Condition.
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
              <Typography variant="body1">Patient ID: {patient_id}</Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">
                Inheritance Pattern: {inheritance_pattern}
              </Typography>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default GeneticConditionView;
