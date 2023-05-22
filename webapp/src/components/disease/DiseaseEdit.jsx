import {
  Button,
  CardContent,
  Grid,
  TextField,
  Typography,
} from "@mui/material";
import React, { useState } from "react";
import axios from "axios";

import "./Disease.scss";

const DiseaseEdit = ({ selectedRow }) => {
  const { name, description, symptoms, treatment, prevention } = selectedRow;

  const [nameValue, setName] = useState(name);
  const [descriptionValue, setDescription] = useState(description);
  const [symptomsValue, setSymptoms] = useState(symptoms);
  const [treatmentValue, setTreatment] = useState(treatment);
  const [preventionValue, setPrevention] = useState(prevention);

  //Update record
  const handleUpdate = async () => {
    const appointmentData = {
      name: nameValue,
      description: descriptionValue,
      symptoms: symptomsValue,
      treatment: treatmentValue,
      prevention: preventionValue,
    };

    try {
      const res = await axios.put(
        `http://127.0.0.1:8000/disease/${selectedRow.id}`,
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
          Are you sure you want to update disease?
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Edit out this form and we will update disease.
        </Typography>
        <form onSubmit={handleUpdate} style={{ marginTop: "10px" }}>
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Name"
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
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Symptoms"
                placeholder="Enter Symptoms"
                variant="outlined"
                type="text"
                value={symptomsValue}
                onChange={(event) => {
                  setSymptoms(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Treatment"
                placeholder="Enter Treatment"
                variant="outlined"
                type="text"
                value={treatmentValue}
                onChange={(event) => {
                  setTreatment(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                label="Prevention"
                placeholder="Enter Prevention"
                variant="outlined"
                type="text"
                value={preventionValue}
                onChange={(event) => {
                  setPrevention(event.target.value);
                }}
                multiline
                rows={4}
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

export default DiseaseEdit;
