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

const DiseaseForm = () => {
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [symptoms, setSymptoms] = useState("");
  const [treatment, setTreatment] = useState("");
  const [prevention, setPrevention] = useState("");

  //Post data to database
  const handleSubmit = async (e) => {
    e.preventDefault();

    await axios
      .post("http://127.0.0.1:8000/disease", {
        name,
        description,
        symptoms,
        treatment,
        prevention,
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
          Disease Form
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
                label="Name"
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
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Symptoms"
                placeholder="Enter Symptoms"
                variant="outlined"
                type="text"
                value={symptoms}
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
                value={treatment}
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
                value={prevention}
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
                Submit
              </Button>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default DiseaseForm;
