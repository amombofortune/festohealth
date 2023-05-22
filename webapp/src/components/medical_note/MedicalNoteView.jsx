import { CardContent, Grid, Typography } from "@mui/material";
import React from "react";

import "./MedicalNote.scss";

const MedicalNoteView = ({ selectedRow }) => {
  const { patient_id, doctor_id, date, content } = selectedRow;

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Medical Note Information
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Details about medical note.
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
              <Typography variant="body1">Date: {date}</Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">Content: {content}</Typography>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default MedicalNoteView;
