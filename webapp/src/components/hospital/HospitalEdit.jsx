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

import "./Hospital.scss";

const HospitalEdit = ({ selectedRow }) => {
  const {
    name,
    address,
    city,
    state,
    postal_code,
    country,
    email,
    phone_number,
    website,
    rating,
    verified,
  } = selectedRow;

  const [nameValue, setName] = useState(name);
  const [addressValue, setAddress] = useState(address);
  const [cityValue, setCity] = useState(city);
  const [stateValue, setState] = useState(state);
  const [postalCode, setPostalCode] = useState(postal_code);
  const [countryValue, setCountry] = useState(country);
  const [emailValue, setEmail] = useState(email);
  const [phoneNumber, setPhoneNumber] = useState(phone_number);
  const [websiteValue, setWebsite] = useState(website);
  const [ratingValue, setRating] = useState(rating);
  const [verifiedValue, setVerified] = useState(verified);

  const [countryDB, setCountryDB] = useState([]);

  //Update record
  const handleUpdate = async () => {
    const appointmentData = {
      name: nameValue,
      address: addressValue,
      city: cityValue,
      state: stateValue,
      postal_code: postalCode,
      country: countryValue,
      email: emailValue,
      phone_number: phoneNumber,
      website: websiteValue,
      rating: ratingValue,
      verified: verifiedValue,
    };

    try {
      const res = await axios.put(
        `http://127.0.0.1:8000/hospital/${selectedRow.id}`,
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
          Are you sure you want to update hospital information?
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Edit out this form and we will update hospital information.
        </Typography>
        <form onSubmit={handleUpdate} style={{ marginTop: "10px" }}>
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Hospital Name"
                placeholder="Enter Hospital Name"
                variant="outlined"
                type="text"
                value={nameValue}
                onChange={(event) => {
                  setName(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} item>
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
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="City"
                placeholder="Enter City"
                variant="outlined"
                type="text"
                value={cityValue}
                onChange={(event) => {
                  setCity(event.target.value);
                }}
                fullWidth
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
                //defaultValue="In-person"
                //helperText="Please select appointment type"
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
                label="Email"
                helperText="Enter Email"
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
                label="Phone Number"
                helperText="Enter Phone Number"
                variant="outlined"
                type="number"
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
                label="Website"
                helperText="Enter Website"
                variant="outlined"
                type="text"
                value={websiteValue}
                onChange={(event) => {
                  setWebsite(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Rating"
                helperText="Enter Rating"
                variant="outlined"
                type="number"
                value={ratingValue}
                onChange={(event) => {
                  setRating(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Verified"
                helperText="Enter Verified"
                variant="outlined"
                type="text"
                value={verifiedValue}
                onChange={(event) => {
                  setVerified(event.target.value);
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
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default HospitalEdit;
