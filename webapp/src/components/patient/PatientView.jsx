import { CardContent, Grid, Typography } from "@mui/material";
import React from "react";

import "./Patient.scss";

const PatientView = ({ selectedRow }) => {
  const {
    firstname,
    middlename,
    lastname,
    dob,
    gender,
    phonenumber,
    email,
    address,
    city,
    state,
    postal_code,
    country,
    emergency_contact_name,
    emergency_contact_phone,
    relationship,
    insurance,
    provider_name,
    policy_number,
    group_number,
    effective_date,
    expiration_date,
  } = selectedRow;

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Patient Information
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Details about patient.
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
                Phone Number: {phonenumber}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">Email: {email}</Typography>
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
                Emergency Contact Name: {emergency_contact_name}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Emergency Contact Phone: {emergency_contact_phone}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Relationship: {relationship}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Insurance: {insurance ? "Yes" : "No"}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Provider Name: {provider_name}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Policy Number: {policy_number}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Group Number: {group_number}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Effective Date: {effective_date}
              </Typography>
            </Grid>
            <Grid xs={12} sm={6} item>
              <Typography variant="body1">
                Expiration Date: {expiration_date}
              </Typography>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default PatientView;
