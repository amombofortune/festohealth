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

import "./Referral.scss";

const ReferralEdit = ({ selectedRow }) => {
  const {
    referring_patient,
    referred_patient,
    referring_doctor,
    referred_doctor,
    referring_hospital,
    referred_hospital,
    referral_date,
    referral_reason,
    status,
  } = selectedRow;

  const [referringPatient, setReferringPatient] = useState(referring_patient);
  const [referredPatient, setReferredPatient] = useState(referred_patient);
  const [referringDoctor, setReferringDoctor] = useState(referring_doctor);
  const [referredDoctor, setReferredDoctor] = useState(referred_doctor);
  const [referringHospital, setReferringHospital] =
    useState(referring_hospital);
  const [referredHospital, setReferredHospital] = useState(referred_hospital);
  const [referralDate, setReferralDate] = useState(referral_date);
  const [referralReason, setReferralReason] = useState(referral_reason);
  const [statusValue, setStatus] = useState(status);

  const [hospitalDB, setHospitalDB] = useState([]);

  //Update record
  const handleUpdate = async () => {
    const appointmentData = {
      referring_patient: referringPatient,
      referred_patient: referredPatient,
      referring_doctor: referringDoctor,
      referred_doctor: referredDoctor,
      referring_hospital: referringHospital,
      referred_hospital: referredHospital,
      referral_date: referralDate,
      referral_reason: referralReason,
      status: statusValue,
    };

    try {
      const res = await axios.put(
        `http://127.0.0.1:8000/referral/${selectedRow.id}`,
        appointmentData
      );
      console.log("Updated!!", res);
      window.location.reload(true);
    } catch (err) {
      console.log(err);
    }
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
          Are you sure you want to update patient information?
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Edit out this form and we will update patient information.
        </Typography>
        <form onSubmit={handleUpdate} style={{ marginTop: "10px" }}>
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Referring Patient"
                placeholder="Enter Referring Patient"
                variant="outlined"
                type="text"
                value={referringPatient}
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
                value={referredPatient}
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
                value={referringDoctor}
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
                value={referredDoctor}
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
                value={referringHospital}
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
                value={referredHospital}
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
                value={referralDate}
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
                value={referralReason}
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
                value={statusValue}
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
                Update
              </Button>
            </Grid>
          </Grid>{" "}
        </form>
      </CardContent>
    </div>
  );
};

export default ReferralEdit;
