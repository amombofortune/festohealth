import { CardContent, Grid, Typography } from "@mui/material";
import React from "react";

import "./Doctor.scss";

const DoctorView = ({ selectedRow }) => {
  const {
    firstname,
    middlename,
    lastname,
    dob,
    gender,
    phone_number,
    email,
    specialty,
    licence_number,
    address,
    city,
    state,
    postal_code,
    country,
    consultation_fee,
    rating,
    verified,
  } = selectedRow;

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Doctor Information
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Details about doctors.
        </Typography>
        <form>
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">First Name: {firstname}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Middle Name: {middlename}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Last Name: {lastname}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Date of Birth: {dob}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Gender: {gender}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Phone Number: {phone_number}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Email: {email}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Specialty: {specialty}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Licence Number: {licence_number}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Address: {address}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">City: {city}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">State: {state}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Postal Code: {postal_code}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Country: {country}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Consultation Fee: {consultation_fee}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Rating: {rating}</Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Verified: {verified ? "Yes" : "No"}
              </Typography>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default DoctorView;
