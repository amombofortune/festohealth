import {
  Button,
  CardContent,
  Grid,
  TextField,
  Typography,
} from "@mui/material";
import React, { useState, useEffect } from "react";
import axios from "axios";
import MenuItem from "@mui/material/MenuItem";

import "./adverseReaction.scss";

const AdverseReactionEdit = ({ selectedRow }) => {
  const {
    patient_id,
    reaction_date,
    reaction_time,
    reaction_type,
    reaction_details,
    medication_name,
    dosage,
    severity,
    treatment,
  } = selectedRow;

  const [patientID, setPatientID] = useState(patient_id);
  const [reactionDate, setReactionDate] = useState(reaction_date);
  const [reactionTime, setReactionTime] = useState(reaction_time);
  const [reactionType, setReactionType] = useState(reaction_type);
  const [reactionDetails, setReactionDetails] = useState(reaction_details);
  const [medicationName, setMedicationName] = useState(medication_name);
  const [dosageValue, setDosageValue] = useState(dosage);
  const [severityValue, setSeverityValue] = useState(severity);
  const [treatmentValue, setTreatmentValue] = useState(treatment);
  const [reactionTypeDB, setReactionTypeDB] = useState([]);

  //Update record
  const handleUpdate = async () => {
    const appointmentData = {
      patient_id: patientID,
      reaction_date: reactionDate,
      reaction_time: reactionTime,
      reaction_type: reactionType,
      reaction_details: reactionDetails,
      medication_name: medicationName,
      dosage: dosageValue,
      severity: severityValue,
      treatment: treatmentValue,
    };

    try {
      const res = await axios.put(
        `http://127.0.0.1:8000/adverse_reaction/${selectedRow.id}`,
        appointmentData
      );
      console.log("Updated!!", res);
      window.location.reload(true);
    } catch (err) {
      console.log(err);
    }
  };

  //Fetch appointment type
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/adverse_reaction_type")
      .then((res) => {
        console.log(
          "Fetching appointment type from database successful!!!",
          res.data
        );
        setReactionTypeDB(res.data);
      })
      .catch((err) => console.log(err));
  }, []);

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Are you sure you want to update adverse reaction?
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Edit out this form and we will update your adverse reaction.
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
                //label="Reaction Date"
                helperText="Enter Reaction Date"
                variant="outlined"
                type="date"
                value={reactionDate}
                onChange={(event) => {
                  setReactionDate(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                //label="Reaction Date"
                helperText="Enter Reaction Time"
                variant="outlined"
                type="datetime"
                value={reactionTime}
                onChange={(event) => {
                  setReactionTime(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                id="reactionType"
                select
                label="Select Reaction Type"
                value={reactionType}
                onChange={(event) => {
                  setReactionType(event.target.value);
                }}
                fullWidth
              >
                {reactionTypeDB.map((item) => (
                  <MenuItem key={item.id} value={item.name}>
                    {item.name}
                  </MenuItem>
                ))}
              </TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                label="Reaction Details"
                helperText="Enter Reaction Details"
                variant="outlined"
                type="text"
                value={reactionDetails}
                onChange={(event) => {
                  setReactionDetails(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Medication Name"
                helperText="Enter Medication Name"
                variant="outlined"
                type="text"
                value={medicationName}
                onChange={(event) => {
                  setMedicationName(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Dosage"
                helperText="Enter Dosage"
                variant="outlined"
                type="text"
                value={dosageValue}
                onChange={(event) => {
                  setDosageValue(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                label="Severity"
                placeholder="Enter Severity"
                variant="outlined"
                type="text"
                value={severityValue}
                onChange={(event) => {
                  setSeverityValue(event.target.value);
                }}
                multiline
                rows={4}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                label="Treatment"
                placeholder="Enter Treatment"
                variant="outlined"
                type="text"
                value={treatmentValue}
                onChange={(event) => {
                  setTreatmentValue(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>

            <Grid xs={12} item>
              <Button
                type="submit"
                variant="contained"
                color="primary"
                style={{ backgroundColor: "#6439ff" }}
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

export default AdverseReactionEdit;
