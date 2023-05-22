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
import "./diagnosis.scss";

const DiagnosisForm = () => {
  const [patient_id, setPatientID] = useState("");
  const [disease, setDisease] = useState("");
  const [diagnosis, setDiagnosis] = useState("");
  const [date, setDate] = useState("");
  const [doctor_id, setDoctorID] = useState("");
  const [notes, setNotes] = useState("");

  const [diseaseDB, setDiseaseDB] = useState([]);

  //Post data to database
  const handleSubmit = async (e) => {
    e.preventDefault();

    await axios
      .post("http://127.0.0.1:8000/diagnosis", {
        patient_id,
        disease,
        diagnosis,
        date,
        doctor_id,
        notes,
      })
      .then((res) => {
        window.location.reload(true);
        console.log("Posting data to database successful!!!", res);
      })
      .catch((err) => console.log(err));
  };

  //Fetch appointment type
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/disease")
      .then((res) => {
        console.log("Fetching disease from database successful!!!", res.data);
        setDiseaseDB(res.data);
      })
      .catch((err) => console.log(err));
  }, []);

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Disease Diagnosis Form
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Fill out the form to diagnose a patient.
        </Typography>
        <form onSubmit={handleSubmit} className="admission_form">
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Patient ID"
                placeholder="Enter Patient ID"
                variant="outlined"
                type="text"
                value={patient_id}
                onChange={(event) => {
                  setPatientID(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>

            <Grid xs={12} item>
              <TextField
                id="disease"
                select
                label="Select Disease"
                value={disease}
                //defaultValue="In-person"
                //helperText="Please select appointment type"
                onChange={(event) => {
                  setDisease(event.target.value);
                }}
                fullWidth
              >
                {diseaseDB.map((item) => (
                  <MenuItem key={item.id} value={item.name}>
                    {item.name}
                  </MenuItem>
                ))}
              </TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                label="Diagnosis"
                placeholder="Enter Diagnosis"
                variant="outlined"
                type="text"
                value={diagnosis}
                onChange={(event) => {
                  setDiagnosis(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                //label="Date"
                helperText="Enter Date"
                variant="outlined"
                type="date"
                value={date}
                onChange={(event) => {
                  setDate(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                //label="End Time"
                placeholder="Enter Doctor ID"
                variant="outlined"
                type="text"
                value={doctor_id}
                onChange={(event) => {
                  setDoctorID(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                label="Notes"
                placeholder="Enter Notes"
                variant="outlined"
                type="text"
                value={notes}
                onChange={(event) => {
                  setNotes(event.target.value);
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
                Submit
              </Button>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default DiagnosisForm;
