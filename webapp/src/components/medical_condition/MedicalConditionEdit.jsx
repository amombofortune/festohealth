import {
  Button,
  CardContent,
  Grid,
  TextField,
  Typography,
} from "@mui/material";
import React, { useState } from "react";
import axios from "axios";

import "./MedicalCondition.scss";

const MedicalConditionEdit = ({ selectedRow }) => {
  const { patient_id, name, description, diagnosis_date, treatment } =
    selectedRow;

  const [patientID, setPatientID] = useState(patient_id);
  const [nameValue, setName] = useState(name);
  const [descriptionValue, setDescription] = useState(description);
  const [diagnosisDate, setDiagnosisDate] = useState(diagnosis_date);
  const [treatmentValue, setTreatment] = useState(treatment);

  //Update record
  const handleUpdate = async () => {
    const appointmentData = {
      patient_id: patientID,
      name: nameValue,
      description: descriptionValue,
      diagnosis_date: diagnosisDate,
      treatment: treatmentValue,
    };

    try {
      const res = await axios.put(
        `http://127.0.0.1:8000/medical_condition/${selectedRow.id}`,
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
          Are you sure you want to update medical condition?
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Edit out this form and we will update medical condition.
        </Typography>
        <form onSubmit={handleUpdate} style={{ marginTop: "10px" }}>
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <TextField
                label=" Patient ID"
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
            <Grid xs={12} item>
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
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
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
            <Grid xs={12} sm={6} item>
              <TextField
                //label="Diagnosis Date"
                helperText="Enter Diagnosis Date"
                variant="outlined"
                type="date"
                value={diagnosisDate}
                onChange={(event) => {
                  setDiagnosisDate(event.target.value);
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

export default MedicalConditionEdit;
