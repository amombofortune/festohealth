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

import "./nurse.scss";

const NurseEdit = ({ selectedRow }) => {
  const {
    firstname,
    lastname,
    dob,
    gender,
    phone_number,
    email,
    licence_number,
    hospital_id,
    address,
    city,
    state,
    postal_code,
    country,
    work_schedule,
    verified,
  } = selectedRow;

  const [firstName, setFirstName] = useState(firstname);
  const [lastName, setLastName] = useState(lastname);
  const [dobValue, setDOB] = useState(dob);
  const [genderValue, setGender] = useState(gender);
  const [phoneNumber, setPhoneNumber] = useState(phone_number);
  const [emailValue, setEmail] = useState(email);
  const [licenceNumber, setLicenceNumber] = useState(licence_number);
  const [hospitalID, setHospitalID] = useState(hospital_id);
  const [addressValue, setAddress] = useState(address);
  const [cityValue, setCity] = useState(city);
  const [stateValue, setState] = useState(state);
  const [postalCode, setPostalCode] = useState(postal_code);
  const [countryValue, setCountry] = useState(country);
  const [workSchedule, setWorkSchedule] = useState(work_schedule);
  const [verifiedValue, setVerified] = useState(verified);

  const [countryDB, setCountryDB] = useState([]);

  //Update record
  const handleUpdate = async () => {
    const appointmentData = {
      firstname: firstName,
      lastname: lastName,
      dob: dobValue,
      gender: genderValue,
      phone_number: phoneNumber,
      email: emailValue,
      licence_number: licenceNumber,
      hospital_id: hospitalID,
      address: addressValue,
      city: cityValue,
      state: stateValue,
      postal_code: postalCode,
      country: countryValue,
      work_schedule: workSchedule,
      verified: verifiedValue,
    };

    try {
      const res = await axios.put(
        `http://127.0.0.1:8000/nurse/${selectedRow.id}`,
        appointmentData
      );
      console.log("Updated!!", res);
      window.location.reload(true);
    } catch (err) {
      console.log(err);
    }
  };

  //Fetch country
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/country")
      .then((res) => {
        console.log(
          "Fetching appointment type from database successful!!!",
          res.data
        );
        setCountryDB(res.data);
      })
      .catch((err) => console.log(err));
  }, []);

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Are you sure you want to update nurse information?
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Edit out this form and we will update nurse information.
        </Typography>
        <form onSubmit={handleUpdate} style={{ marginTop: "10px" }}>
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <TextField
                label="First Name"
                placeholder="Enter First Name"
                variant="outlined"
                type="text"
                value={firstName}
                onChange={(event) => {
                  setFirstName(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>

            <Grid xs={12} sm={6} item>
              <TextField
                label="Last Name"
                placeholder="Enter Last Name"
                variant="outlined"
                type="text"
                value={lastName}
                onChange={(event) => {
                  setLastName(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Date of Birth"
                placeholder="Enter Date of Birth"
                variant="outlined"
                type="date"
                value={dobValue}
                onChange={(event) => {
                  setDOB(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Gender"
                placeholder="Enter Gender"
                variant="outlined"
                type="text"
                value={genderValue}
                onChange={(event) => {
                  setGender(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Phone Number"
                placeholder="Enter Phone Number"
                variant="outlined"
                type="text"
                value={phoneNumber}
                onChange={(event) => {
                  setPhoneNumber(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Email"
                placeholder="Enter Email"
                variant="outlined"
                type="email"
                value={emailValue}
                onChange={(event) => {
                  setEmail(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>

            <Grid xs={12} sm={6} item>
              <TextField
                label="Licence Number"
                placeholder="Enter Licence Number"
                variant="outlined"
                type="text"
                value={licenceNumber}
                onChange={(event) => {
                  setLicenceNumber(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Hospital ID"
                placeholder="Enter Hospital ID"
                variant="outlined"
                type="text"
                value={hospitalID}
                onChange={(event) => {
                  setHospitalID(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Address"
                placeholder="Enter Address"
                variant="outlined"
                type="text"
                value={addressValue}
                onChange={(event) => {
                  setAddress(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="City"
                helperText="Enter City"
                variant="outlined"
                type="text"
                value={cityValue}
                onChange={(event) => {
                  setCity(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="State"
                placeholder="Enter State"
                variant="outlined"
                type="text"
                value={stateValue}
                onChange={(event) => {
                  setState(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Postal Code"
                placeholder="Enter Postal Code"
                variant="outlined"
                type="text"
                value={postalCode}
                onChange={(event) => {
                  setPostalCode(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                id="country"
                select
                label="Select Country"
                value={countryValue}
                onChange={(event) => {
                  setCountry(event.target.value);
                }}
                fullWidth
              >
                {countryDB.map((item) => (
                  <MenuItem key={item.id} value={item.name}>
                    {item.name}
                  </MenuItem>
                ))}
              </TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Work Schedule"
                placeholder="Enter Work Schedule"
                variant="outlined"
                type="text"
                value={workSchedule}
                onChange={(event) => {
                  setWorkSchedule(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Verified"
                placeholder="Enter Verified"
                variant="outlined"
                type="text"
                value={verifiedValue}
                onChange={(event) => {
                  setVerified(event.target.value);
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

export default NurseEdit;
