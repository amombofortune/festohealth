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

import "./Patient.scss";

const PatientEdit = ({ selectedRow }) => {
  const {
    firstname,
    middlename,
    lastname,
    dob,
    gender,
    phonenumber,
    email,
    address,
    city,
    state,
    postal_code,
    country,
    emergency_contact_name,
    emergency_contact_phone,
    relationship,
    insurance,
    provider_name,
    policy_number,
    group_number,
    effective_date,
    expiration_date,
  } = selectedRow;

  const [firstName, setFirstName] = useState(firstname);
  const [middleName, setMiddleName] = useState(middlename);
  const [lastName, setLastName] = useState(lastname);
  const [dobValue, setDOB] = useState(dob);
  const [genderValue, setGender] = useState(gender);
  const [phoneNumber, setPhoneNumber] = useState(phonenumber);
  const [emailValue, setEmail] = useState(email);
  const [addressValue, setAddress] = useState(address);
  const [cityValue, setCity] = useState(city);
  const [stateValue, setState] = useState(state);
  const [postalCode, setPostalCode] = useState(postal_code);
  const [countryValue, setCountry] = useState(country);
  const [emergencyContactName, setEmergencyContactName] = useState(
    emergency_contact_name
  );
  const [emergencyContactPhone, setEmergencyContactPhone] = useState(
    emergency_contact_phone
  );
  const [relationshipValue, setRelationshipValue] = useState(relationship);
  const [insuranceValue, setInsuranceValue] = useState(insurance);
  const [providerName, setProviderName] = useState(provider_name);
  const [policyNumber, setPolicyNumber] = useState(policy_number);
  const [groupNumber, setGroupNumber] = useState(group_number);
  const [effectiveDate, setEffectiveDate] = useState(effective_date);
  const [expirationDate, setExpirationDate] = useState(expiration_date);

  const [countryDB, setCountryDB] = useState([]);

  //Update record
  const handleUpdate = async () => {
    const appointmentData = {
      firstname: firstName,
      middlename: middleName,
      lastname: lastName,
      dob: dobValue,
      gender: genderValue,
      phonenumber: phoneNumber,
      email: emailValue,
      address: addressValue,
      city: cityValue,
      state: stateValue,
      postal_code: postalCode,
      country: countryValue,
      emergency_contact_name: emergencyContactName,
      emergency_contact_phone: emergencyContactPhone,
      relationship: relationshipValue,
      insurance: insuranceValue,
      provider_name: providerName,
      policy_number: policyNumber,
      group_number: groupNumber,
      effective_date: effectiveDate,
      expiration_date: expirationDate,
    };

    try {
      const res = await axios.put(
        `http://127.0.0.1:8000/patient/${selectedRow.id}`,
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
                label="Middle Name"
                placeholder="Enter Middle Name"
                variant="outlined"
                type="text"
                value={middleName}
                onChange={(event) => {
                  setMiddleName(event.target.value);
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
                label="Emergency Contact Name"
                placeholder="Enter Emergency Contact Name"
                variant="outlined"
                type="text"
                value={emergencyContactName}
                onChange={(event) => {
                  setEmergencyContactName(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Emergency Contact Phone"
                placeholder="Enter Emergency Contact Phone"
                variant="outlined"
                type="text"
                value={emergencyContactPhone}
                onChange={(event) => {
                  setEmergencyContactPhone(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Relationship"
                placeholder="Enter Relationship"
                variant="outlined"
                type="text"
                value={relationshipValue}
                onChange={(event) => {
                  setRelationshipValue(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Insurance"
                placeholder="Enter Insurance"
                variant="outlined"
                type="text"
                value={insuranceValue}
                onChange={(event) => {
                  setInsuranceValue(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Provider Name"
                placeholder="Enter Provider Name"
                variant="outlined"
                type="text"
                value={providerName}
                onChange={(event) => {
                  setProviderName(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Policy Number"
                placeholder="Enter Policy Number"
                variant="outlined"
                type="text"
                value={policyNumber}
                onChange={(event) => {
                  setPolicyNumber(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Group Number"
                placeholder="Enter Group Number"
                variant="outlined"
                type="text"
                value={groupNumber}
                onChange={(event) => {
                  setGroupNumber(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                //label="Emergency Contact Name"
                helperText="Enter Effective Date"
                variant="outlined"
                type="date"
                value={effectiveDate}
                onChange={(event) => {
                  setEffectiveDate(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                //label="Expiration Date"
                helperText="Enter Expiration Date"
                variant="outlined"
                type="date"
                value={expirationDate}
                onChange={(event) => {
                  setExpirationDate(event.target.value);
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

export default PatientEdit;
