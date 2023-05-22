import {
  Button,
  CardContent,
  Grid,
  TextField,
  Typography,
} from "@mui/material";
import React, { useState, useEffect } from "react";
import MenuItem from "@mui/material/MenuItem";

import axios from "axios";
import "./Referral.scss";

const ReferralForm = () => {
  const [referring_patient, setReferringPatient] = useState("");
  const [referred_patient, setReferredPatient] = useState("");
  const [referring_doctor, setReferringDoctor] = useState("");
  const [referred_doctor, setReferredDoctor] = useState("");
  const [referring_hospital, setReferringHospital] = useState("");
  const [referred_hospital, setReferredHospital] = useState("");
  const [referral_date, setReferralDate] = useState("");
  const [referral_reason, setReferralReason] = useState("");
  const [status, setStatus] = useState("");

  const [hospitalDB, setHospitalDB] = useState([]);

  //Post data to database
  const handleSubmit = async (e) => {
    e.preventDefault();

    await axios
      .post("http://127.0.0.1:8000/referral", {
        referring_patient,
        referred_patient,
        referring_doctor,
        referred_doctor,
        referring_hospital,
        referred_hospital,
        referral_date,
        referral_reason,
        status,
      })
      .then((res) => {
        window.location.reload(true);
        console.log("Posting data to database successful!!!", res);
      })
      .catch((err) => console.log(err));
  };

  //Fetch hospital
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/hospital")
      .then((res) => {
        console.log(
          "Fetching appointment from database successful!!!",
          res.data
        );
        setHospitalDB(res.data);
      })
      .catch((err) => console.log(err));
  }, []);

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Referral Form
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Fill out the form to refer a patient.
        </Typography>
        <form onSubmit={handleSubmit} className="admission_form">
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Referring Patient"
                placeholder="Enter Referring Patient"
                variant="outlined"
                type="text"
                value={referring_patient}
                onChange={(event) => {
                  setReferringPatient(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Referred Patient"
                placeholder="Enter Referred Patient"
                variant="outlined"
                type="text"
                value={referred_patient}
                onChange={(event) => {
                  setReferredPatient(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Referring Doctor"
                placeholder="Enter Referring Doctor"
                variant="outlined"
                type="text"
                value={referring_doctor}
                onChange={(event) => {
                  setReferringDoctor(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Referred Doctor"
                placeholder="Enter Referred Doctor"
                variant="outlined"
                type="text"
                value={referred_doctor}
                onChange={(event) => {
                  setReferredDoctor(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>

            <Grid xs={12} sm={6} item>
              <TextField
                id="referring_hospital"
                select
                label="Select Referring Hospital"
                value={referring_hospital}
                onChange={(event) => {
                  setReferringHospital(event.target.value);
                }}
                fullWidth
              >
                {hospitalDB.map((item) => (
                  <MenuItem key={item.id} value={item.name}>
                    {item.name}
                  </MenuItem>
                ))}
              </TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                id="referred_hospital"
                select
                label="Select Referred Hospital"
                value={referred_hospital}
                onChange={(event) => {
                  setReferredHospital(event.target.value);
                }}
                fullWidth
              >
                {hospitalDB.map((item) => (
                  <MenuItem key={item.id} value={item.name}>
                    {item.name}
                  </MenuItem>
                ))}
              </TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Referral Date"
                placeholder="Enter Referral Date"
                variant="outlined"
                type="date"
                value={referral_date}
                onChange={(event) => {
                  setReferralDate(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Referral Reason"
                helperText="Enter Referral Reason"
                variant="outlined"
                type="text"
                value={referral_reason}
                onChange={(event) => {
                  setReferralReason(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>

            <Grid xs={12} sm={6} item>
              <TextField
                label="Status"
                helperText="Enter Status"
                variant="outlined"
                type="text"
                value={status}
                onChange={(event) => {
                  setStatus(event.target.value);
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
                Submit
              </Button>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default ReferralForm;
