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

import "./InsuranceProvider.scss";

const InsuranceProviderEdit = ({ selectedRow }) => {
  const {
    name,
    type,
    address,
    city,
    state,
    postal_code,
    country,
    phone_number,
    email,
    website,
  } = selectedRow;

  const [nameValue, setName] = useState(name);
  const [typeValue, setType] = useState(type);
  const [addressValue, setAddress] = useState(address);
  const [cityValue, setCity] = useState(city);
  const [stateValue, setState] = useState(state);
  const [postalCode, setPostalCode] = useState(postal_code);
  const [countryValue, setCountry] = useState(country);
  const [phoneNumber, setPhoneNumber] = useState(phone_number);
  const [emailValue, setEmail] = useState(email);
  const [websiteValue, setWebsite] = useState(website);

  const [countryDB, setCountryDB] = useState([]);
  const [providerTypeDB, setProviderTypeDB] = useState([]);

  //Update record
  const handleUpdate = async () => {
    const appointmentData = {
      name: nameValue,
      type: typeValue,
      address: addressValue,
      city: cityValue,
      state: stateValue,
      postal_code: postalCode,
      country: countryValue,
      phone_number: phoneNumber,
      email: emailValue,
      website: websiteValue,
    };

    try {
      const res = await axios.put(
        `http://127.0.0.1:8000/insurance_provider/${selectedRow.id}`,
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
        console.log("Fetching country from database successful!!!", res.data);
        setCountryDB(res.data);
      })
      .catch((err) => console.log(err));
  }, []);

  //Fetch insurance provider type
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/insurance_provider_type")
      .then((res) => {
        console.log(
          "Fetching provider type from database successful!!!",
          res.data
        );
        setProviderTypeDB(res.data);
      })
      .catch((err) => console.log(err));
  }, []);

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Are you sure you want to update insurance provider?
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Edit out this form and we will update your insurance provider.
        </Typography>
        <form onSubmit={handleUpdate} style={{ marginTop: "10px" }}>
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <TextField
                label=" Provider Name"
                placeholder="Enter Provider Name"
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
            <Grid xs={12} sm={6} item>
              <TextField
                id="type"
                select
                label="Select Type"
                value={typeValue}
                onChange={(event) => {
                  setType(event.target.value);
                }}
                fullWidth
              >
                {providerTypeDB.map((item) => (
                  <MenuItem key={item.id} value={item.name}>
                    {item.name}
                  </MenuItem>
                ))}
              </TextField>
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
                label="Phone number"
                placeholder="Enter Phone Number"
                variant="outlined"
                type="text"
                value={phoneNumber}
                onChange={(event) => {
                  setPhoneNumber(event.target.value);
                }}
                fullWidth
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
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Website"
                placeholder="Enter Website"
                variant="outlined"
                type="text"
                value={websiteValue}
                onChange={(event) => {
                  setWebsite(event.target.value);
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
                Update
              </Button>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default InsuranceProviderEdit;
