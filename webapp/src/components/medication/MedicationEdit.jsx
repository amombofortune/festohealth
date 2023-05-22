import {
  Button,
  CardContent,
  Grid,
  TextField,
  Typography,
} from "@mui/material";
import React, { useState } from "react";
import axios from "axios";

import "./Medication.scss";

const MedicationEdit = ({ selectedRow }) => {
  const {
    name,
    description,
    route_of_administration,
    dosage,
    unit,
    frequency,
    patient_id,
    doctor_id,
  } = selectedRow;

  const [nameValue, setName] = useState(name);
  const [descriptionValue, setDescription] = useState(description);
  const [routeOfAdministration, setRouteOfAdministration] = useState(
    route_of_administration
  );
  const [dosageValue, setDosage] = useState(dosage);
  const [unitValue, setUnit] = useState(unit);
  const [frequencyValue, setFrequency] = useState(frequency);
  const [patientID, setPatientID] = useState(patient_id);
  const [doctorID, setDoctorID] = useState(doctor_id);

  //Update record
  const handleUpdate = async () => {
    const appointmentData = {
      name: nameValue,
      description: descriptionValue,
      route_of_administration: routeOfAdministration,
      dosage: dosageValue,
      unit: unitValue,
      frequency: frequencyValue,
      patient_id: patientID,
      doctor_id: doctorID,
    };

    try {
      const res = await axios.put(
        `http://127.0.0.1:8000/medication/${selectedRow.id}`,
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
          Are you sure you want to update medication?
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Edit out this form and we will update medication.
        </Typography>
        <form onSubmit={handleUpdate} style={{ marginTop: "10px" }}>
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <TextField
                label=" Name"
                placeholder="Enter Name"
                variant="outlined"
                type="text"
                value={nameValue}
                onChange={(event) => {
                  setName(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                label="Description"
                placeholder="Enter Description"
                variant="outlined"
                type="text"
                value={descriptionValue}
                onChange={(event) => {
                  setDescription(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                label="Route of Administration"
                placeholder="Enter Route of Administration"
                variant="outlined"
                type="text"
                value={routeOfAdministration}
                onChange={(event) => {
                  setRouteOfAdministration(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Dosage"
                placeholder="Enter Dosage"
                variant="outlined"
                type="dosage"
                value={dosageValue}
                onChange={(event) => {
                  setDosage(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Unit"
                helperText="Enter Unit"
                variant="outlined"
                type="text"
                value={unitValue}
                onChange={(event) => {
                  setUnit(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Frequency"
                helperText="Enter Frequency"
                variant="outlined"
                type="text"
                value={frequencyValue}
                onChange={(event) => {
                  setFrequency(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Patient ID"
                helperText="Enter Patient ID"
                variant="outlined"
                type="number"
                value={patientID}
                onChange={(event) => {
                  setPatientID(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Doctor ID"
                helperText="Enter Doctor ID"
                variant="outlined"
                type="number"
                value={doctorID}
                onChange={(event) => {
                  setDoctorID(event.target.value);
                }}
                fullWidth
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

export default MedicationEdit;
