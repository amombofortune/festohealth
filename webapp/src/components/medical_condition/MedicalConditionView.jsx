import { CardContent, Grid, Typography } from "@mui/material";
import React from "react";

import "./MedicalCondition.scss";

const MedicalConditionView = ({ selectedRow }) => {
  const { patient_id, name, description, diagnosis_date, treatment } =
    selectedRow;

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Medical Condition Information
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Details about medical condition.
        </Typography>
        <form>
          <Grid container spacing={1}>
            <Grid xs={12} item>
              <Typography variant="body1">Patient ID: {patient_id}</Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">Name: {name}</Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">
                Description: {description}
              </Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">
                Diagnosis Date: {diagnosis_date}
              </Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">Treatment: {treatment}</Typography>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default MedicalConditionView;
