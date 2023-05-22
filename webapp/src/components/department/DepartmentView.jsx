import { CardContent, Grid, Typography } from "@mui/material";
import React from "react";

import "./Department.scss";

const DepartmentView = ({ selectedRow }) => {
  const { name, description, hospital, head_doctor } = selectedRow;

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Department Information
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Details about department.
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
              <Typography variant="body1">Hospital: {hospital}</Typography>
            </Grid>
            <Grid xs={12} item>
              <Typography variant="body1">
                Head Doctor: {head_doctor}
              </Typography>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default DepartmentView;
