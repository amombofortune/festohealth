import { CardContent, Grid, Typography } from "@mui/material";
import React from "react";

import "./MedicalImage.scss";

const MedicalImageView = ({ selectedRow }) => {
  const { patient_id, doctor_id, image_type, image_date } = selectedRow;

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Medical Image Information
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Details about medical image.
        </Typography>
        <form>
          <Grid container spacing={1}>
            <Grid xs={12} item>
              <Typography variant="body1">Patient ID: {patient_id}</Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">Doctor ID: {doctor_id}</Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">Image Type: {image_type}</Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">Image Date: {image_date}</Typography>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default MedicalImageView;
