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

function AdverseReactionForm() {
  const [patient_id, setPatientID] = useState("");
  const [reaction_date, setReactionDate] = useState("");
  const [reaction_time, setReactionTime] = useState("");
  const [reaction_type, setReactionType] = useState("");
  const [reaction_details, setReactionDetails] = useState("");
  const [medication_name, setMedicationName] = useState("");
  const [dosage, setDosage] = useState("");
  const [severity, setSeverity] = useState("");
  const [treatment, setTreatment] = useState("");

  const [reactionTypeDB, setReactionTypeDB] = useState([]);

  //Post data to database
  const handleSubmit = async (e) => {
    e.preventDefault();

    await axios
      .post("http://127.0.0.1:8000/adverse_reaction", {
        patient_id,
        reaction_date,
        reaction_time,
        reaction_type,
        reaction_details,
        medication_name,
        dosage,
        severity,
        treatment,
      })
      .then((res) => {
        window.location.reload(true);
        console.log("Posting data to database successful!!!", res);
      })
      .catch((err) => console.log(err));
  };

  //Fetch reaction type
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/adverse_reaction_type")
      .then((res) => {
        console.log(
          "Fetching reaction type from database successful!!!",
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
          Adverse Reaction Form
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Fill out the form to record adverse reaction of patients.
        </Typography>
        <form onSubmit={handleSubmit} className="admission_form">
          <Grid container spacing={1}>
            <Grid xs={12} item>
              <TextField
                label="Patient ID"
                placeholder="Enter Patient ID"
                variant="outlined"
                type="number"
                value={patient_id}
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
                value={reaction_date}
                onChange={(event) => {
                  setReactionDate(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                //label="Reaction Time"
                helperText="Enter Reaction Time"
                variant="outlined"
                type="time"
                value={reaction_time}
                onChange={(event) => {
                  setReactionTime(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                id="reaction_type"
                select
                label="Select Reaction Type"
                value={reaction_type}
                //defaultValue="In-person"
                //helperText="Please select appointment type"
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
            <Grid xs={12} sm={6} item>
              <TextField
                label="Reaction Details"
                placeholder="Enter Reaction Details"
                variant="outlined"
                type="text"
                value={reaction_details}
                onChange={(event) => {
                  setReactionDetails(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                label="Medication Name"
                placeholder="Enter Medication Name"
                variant="outlined"
                type="text"
                value={medication_name}
                onChange={(event) => {
                  setMedicationName(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                label="Dosage"
                placeholder="Enter Dosage"
                variant="outlined"
                type="text"
                value={dosage}
                onChange={(event) => {
                  setDosage(event.target.value);
                }}
                multiline
                rows={4}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                label="Severity"
                placeholder="Enter Severity"
                variant="outlined"
                type="text"
                value={severity}
                onChange={(event) => {
                  setSeverity(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                label="Treatment"
                placeholder="Enter Treatment"
                variant="outlined"
                type="text"
                value={treatment}
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
                Submit
              </Button>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
}

export default AdverseReactionForm;
