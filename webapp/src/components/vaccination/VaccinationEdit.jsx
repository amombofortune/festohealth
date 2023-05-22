import {
  Button,
  CardContent,
  Grid,
  TextField,
  Typography,
} from "@mui/material";
import React, { useState } from "react";
import axios from "axios";

import "./Vaccination.scss";

const VaccinationEdit = ({ selectedRow }) => {
  const {
    patient_id,
    vaccine_name,
    administered_by,
    administered_at,
    next_dose_due,
  } = selectedRow;

  const [patientID, setPatientID] = useState(patient_id);
  const [vaccineName, setVaccineName] = useState(vaccine_name);
  const [administeredBy, setAdministeredBy] = useState(administered_by);
  const [administeredAt, setAdministeredAt] = useState(administered_at);
  const [nextDoseDue, setNextDoseDue] = useState(next_dose_due);

  //Update record
  const handleUpdate = async () => {
    const appointmentData = {
      patient_id: patientID,
      vaccine_name: vaccineName,
      administered_by: administeredBy,
      administered_at: administeredAt,
      next_dose_due: nextDoseDue,
    };

    try {
      const res = await axios.put(
        `http://127.0.0.1:8000/vaccination/${selectedRow.id}`,
        appointmentData
      );
      console.log("Updated!!", res);
      window.location.reload(true);
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Are you sure you want to update prescription information?
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Edit out this form and we will update prescription information.
        </Typography>
        <form onSubmit={handleUpdate} style={{ marginTop: "10px" }}>
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Patient ID"
                placeholder="Enter Patient ID"
                variant="outlined"
                type="number"
                value={patientID}
                onChange={(event) => {
                  setPatientID(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Vaccine Name"
                placeholder="Enter Vaccine Name"
                variant="outlined"
                type="text"
                value={vaccineName}
                onChange={(event) => {
                  setVaccineName(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                label="Administered By"
                placeholder="Enter Administered By"
                variant="outlined"
                type="text"
                value={administeredBy}
                onChange={(event) => {
                  setAdministeredBy(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Administered At"
                placeholder="Enter Administered At"
                variant="outlined"
                type="date"
                value={administeredAt}
                onChange={(event) => {
                  setAdministeredAt(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Next Dose Due"
                helperText="Enter Next Dose Due"
                variant="outlined"
                type="date"
                value={nextDoseDue}
                onChange={(event) => {
                  setNextDoseDue(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>

            <Grid xs={12} item>
              <Button
                type="submit"
                variant="contained"
                color="primary"
                fullWidth
              >
                Update
              </Button>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default VaccinationEdit;
