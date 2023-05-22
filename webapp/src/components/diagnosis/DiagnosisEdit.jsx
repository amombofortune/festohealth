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

const DiagnosisEdit = ({ selectedRow }) => {
  const { patient_id, disease, diagnosis, date, doctor_id, notes } =
    selectedRow;

  const [patientID, setPatientID] = useState(patient_id);
  const [diseaseValue, setDiseaseValue] = useState(disease);
  const [diagnosisValue, setDiagnosisValue] = useState(diagnosis);
  const [dateValue, setDateValue] = useState(date);
  const [doctorID, setDoctorID] = useState(doctor_id);
  const [notesValue, setNotesValue] = useState(notes);

  const [diseaseDB, setDiseaseDB] = useState([]);

  //Update record
  const handleUpdate = async () => {
    const appointmentData = {
      patient_id: patientID,
      disease: diseaseValue,
      diagnosis: diagnosisValue,
      date: dateValue,
      doctor_id: doctorID,
      notes: notesValue,
    };

    try {
      const res = await axios.put(
        `http://127.0.0.1:8000/diagnosis/${selectedRow.id}`,
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
          Are you sure you want to update appointment?
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Edit out this form and we will update your appointment.
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
            <Grid xs={12} item>
              <TextField
                id="disease"
                select
                label="Select Disease"
                value={diseaseValue}
                onChange={(event) => {
                  setDiseaseValue(event.target.value);
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
                helperText="Enter Diagnosis"
                variant="outlined"
                type="text"
                value={diagnosis}
                onChange={(event) => {
                  setDiagnosisValue(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                //label="Start Time"
                helperText="Enter Date"
                variant="outlined"
                type="date"
                value={dateValue}
                onChange={(event) => {
                  setDateValue(event.target.value);
                }}
                fullWidth
                required
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
                required
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                label="Notes"
                placeholder="Enter Notes"
                variant="outlined"
                type="text"
                value={notesValue}
                onChange={(event) => {
                  setNotesValue(event.target.value);
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

export default DiagnosisEdit;
