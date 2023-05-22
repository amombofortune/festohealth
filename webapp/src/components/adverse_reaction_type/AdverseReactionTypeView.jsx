import { CardContent, Grid, Typography } from "@mui/material";
import React from "react";

import "./AdverseReactionType.scss";

const AdverseReactionTypeView = ({ selectedRow }) => {
  const { name, description } = selectedRow;

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Adverse Reaction Type Information
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Details about adverse reaction type.
        </Typography>
        <form>
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Name: {name}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Description: {description}
              </Typography>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default AdverseReactionTypeView;
