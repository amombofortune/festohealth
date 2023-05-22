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
import "./Doctor.scss";
import { Checkbox, FormControlLabel } from "@mui/material";

const DoctorForm = () => {
  const [firstname, setFirstName] = useState("");
  const [middlename, setMiddleName] = useState("");
  const [lastname, setLastName] = useState("");
  const [dob, setDOB] = useState("");
  const [gender, setGender] = useState("");
  const [phone_number, setPhoneNumber] = useState("");
  const [email, setEmail] = useState("");
  const [specialty, setSpecialty] = useState("");
  const [licence_number, setLicenceNumber] = useState("");
  const [address, setAddress] = useState("");
  const [city, setCity] = useState("");
  const [state, setState] = useState("");
  const [postal_code, setPostalCode] = useState("");
  const [country, setCountry] = useState("");
  const [verified, setVerified] = useState("");

  const [countryDB, setCountryDB] = useState([]);
  const [specialtyDB, setSpecialtyDB] = useState([]);

  const [verifiedTouched, setVerifiedTouched] = useState(false);

  //Post data to database
  const handleSubmit = async (e) => {
    e.preventDefault();

    await axios
      .post("http://127.0.0.1:8000/doctor", {
        firstname,
        middlename,
        lastname,
        dob,
        gender,
        phone_number,
        email,
        specialty,
        licence_number,
        address,
        city,
        state,
        postal_code,
        country,
        verified,
      })
      .then((res) => {
        window.location.reload(true);
        console.log("Posting data to database successful!!!", res);
      })
      .catch((err) => console.log(err));
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

  //Fetch specialties
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/specialty")
      .then((res) => {
        console.log("Fetching specialty from database successful!!!", res.data);
        setSpecialtyDB(res.data);
      })
      .catch((err) => console.log(err));
  }, []);

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Doctor Registration Form
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Fill out the form to register as a doctor.
        </Typography>
        <form onSubmit={handleSubmit} className="admission_form">
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <TextField
                label="First Name"
                placeholder="Enter First Name"
                variant="outlined"
                type="text"
                value={firstname}
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
                value={middlename}
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
                value={lastname}
                onChange={(event) => {
                  setLastName(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>

            <Grid xs={12} sm={6} item>
              <TextField
                //label="Appointment Date"
                helperText="Enter Date of Birth"
                variant="outlined"
                type="date"
                value={dob}
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
                helperText="Enter Gender"
                variant="outlined"
                type="text"
                value={gender}
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
                helperText="Enter Phone Number"
                variant="outlined"
                type="number"
                value={phone_number}
                onChange={(event) => {
                  setPhoneNumber(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                label="Email"
                placeholder="Enter Email"
                variant="outlined"
                type="email"
                value={email}
                onChange={(event) => {
                  setEmail(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                id="specialty"
                select
                label="Select Specialty"
                value={specialty}
                //defaultValue="In-person"
                //helperText="Please select appointment type"
                onChange={(event) => {
                  setSpecialty(event.target.value);
                }}
                fullWidth
              >
                {specialtyDB.map((item) => (
                  <MenuItem key={item.id} value={item.name}>
                    {item.name}
                  </MenuItem>
                ))}
              </TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                label="Licence number"
                placeholder="Enter Licence number"
                variant="outlined"
                type="text"
                value={licence_number}
                onChange={(event) => {
                  setLicenceNumber(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                label="Address"
                placeholder="Enter Address"
                variant="outlined"
                type="text"
                value={address}
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
                value={city}
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
                value={state}
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
                value={postal_code}
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
                value={country}
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

            <Grid xs={12} item>
              <FormControlLabel
                control={
                  <Checkbox
                    checked={verified}
                    onChange={(event) => {
                      setVerified(event.target.checked);
                    }}
                    name="verified"
                    color="primary"
                    size="small"
                    onBlur={() => setVerifiedTouched(true)}
                  />
                }
                label="Verified"
                required={!verified && verifiedTouched}
              />
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

export default DoctorForm;
