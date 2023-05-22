import {
  Button,
  CardContent,
  Grid,
  TextField,
  Typography,
} from "@mui/material";
import React, { useState } from "react";
import axios from "axios";

import "./GeneticCondition.scss";

const GeneticConditionEdit = ({ selectedRow }) => {
  const { name, description, patient_id, inheritance_pattern } = selectedRow;

  const [nameValue, setName] = useState(name);
  const [descriptionValue, setDescription] = useState(description);
  const [patientID, setPatientID] = useState(patient_id);
  const [inheritancePattern, setInheritancePattern] =
    useState(inheritance_pattern);

  //Update record
  const handleUpdate = async () => {
    const appointmentData = {
      name: nameValue,
      description: descriptionValue,
      patient_id: patientID,
      inheritance_pattern: inheritancePattern,
    };

    try {
      const res = await axios.put(
        `http://127.0.0.1:8000/genetic_condition/${selectedRow.id}`,
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
          Are you sure you want to update genetic condition?
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Edit out this form and we will update genetic condition.
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
            <Grid xs={12} sm={6} item>
              <TextField
                label="description"
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
                label="Patient ID"
                placeholder="Enter Patient ID"
                variant="outlined"
                type="text"
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
                label="Inheritance Pattern"
                placeholder="Enter Inheritance Pattern"
                variant="outlined"
                type="text"
                value={inheritancePattern}
                onChange={(event) => {
                  setInheritancePattern(event.target.value);
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

export default GeneticConditionEdit;
