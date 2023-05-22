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

const MedicationForm = () => {
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [route_of_administration, setRouteOfAdministration] = useState("");
  const [dosage, setDosage] = useState("");
  const [unit, setUnit] = useState("");
  const [frequency, setFrequency] = useState("");
  const [patient_id, setPatientID] = useState("");
  const [doctor_id, setDoctorID] = useState("");

  //Post data to database
  const handleSubmit = async (e) => {
    e.preventDefault();

    await axios
      .post("http://127.0.0.1:8000/medication", {
        name,
        description,
        route_of_administration,
        dosage,
        unit,
        frequency,
        patient_id,
        doctor_id,
      })
      .then((res) => {
        window.location.reload(true);
        console.log("Posting data to database successful!!!", res);
      })
      .catch((err) => console.log(err));
  };

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Medication Form
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Fill out the form to administer medication to a patient.
        </Typography>
        <form onSubmit={handleSubmit} className="admission_form">
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <TextField
                label=" Name"
                placeholder="Enter Name"
                variant="outlined"
                type="text"
                value={name}
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
                value={description}
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
                value={route_of_administration}
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
                value={dosage}
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
                value={unit}
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
                value={frequency}
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
                value={patient_id}
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
                value={doctor_id}
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
                Submit
              </Button>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default MedicationForm;
