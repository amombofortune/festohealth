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
import { Checkbox, FormControlLabel } from "@mui/material";

const PatientForm = () => {
  const [firstname, setFirstName] = useState("");
  const [middlename, setMiddleName] = useState("");
  const [lastname, setLastName] = useState("");
  const [dob, setDOB] = useState("");
  const [gender, setGender] = useState("male");
  const [phonenumber, setPhoneNumber] = useState("");
  const [email, setEmail] = useState("");
  const [address, setAddress] = useState("");
  const [city, setCity] = useState("");
  const [state, setState] = useState("");
  const [postal_code, setPostalCode] = useState("");
  const [country, setCountry] = useState("");
  const [emergency_contact_name, setEmergencyContactName] = useState("");
  const [emergency_contact_phone, setEmergencyContactPhone] = useState("");
  const [relationship, setRelationship] = useState("");
  const [insurance, setInsurance] = useState("");
  const [provider_name, setProviderName] = useState("");
  const [policy_number, setPolicyNumber] = useState("");
  const [group_number, setGroupNumber] = useState("");
  const [effective_date, setEffectiveDate] = useState("");
  const [expiration_date, setExpirationDate] = useState("");

  const [countryDB, setCountryDB] = useState([]);
  const [insuranceProviderDB, setInsuranceProviderDB] = useState([]);

  const [insuranceTouched, setInsuranceTouched] = useState(false);

  //Post data to database
  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const access_token = document.cookie.replace(
        /(?:(?:^|.*;\s*)access_token\s*=\s*([^;]*).*$)|^.*$/,
        "$1"
      );

      const headers = {
        Authorization: `Bearer ${access_token}`,
        "Content-Type": "application/json",
      };

      const data = {
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
      };

      await axios.post("http://127.0.0.1:8000/patient", data, {
        withCredentials: true, // Enable sending cookies with the request
        headers,
      });

      window.location.reload(true);
      console.log("Posting data to database successful!!!");
    } catch (error) {
      console.error("Failed to post data to the database:", error);
      // Handle error posting data
    }
  };

  //Fetch country
  useEffect(() => {
    const fetchData = async () => {
      try {
        const access_token = document.cookie.replace(
          /(?:(?:^|.*;\s*)access_token\s*=\s*([^;]*).*$)|^.*$/,
          "$1"
        );

        const response = await axios.get("http://127.0.0.1:8000/country", {
          withCredentials: true, // Enable sending cookies with the request
          headers: {
            Authorization: `Bearer ${access_token}`, // Include the access token as a request header
          },
        });

        console.log(
          "Fetching country from database successful!!!",
          response.data
        );
        setCountryDB(response.data);
      } catch (error) {
        console.error("Failed to fetch country data:", error);
        // Handle error fetching admission data
      }
    };

    fetchData();
  }, []);

  //Fetch insurance provider
  useEffect(() => {
    const fetchData = async () => {
      try {
        const access_token = document.cookie.replace(
          /(?:(?:^|.*;\s*)access_token\s*=\s*([^;]*).*$)|^.*$/,
          "$1"
        );

        const response = await axios.get(
          "http://127.0.0.1:8000/insurance_provider",
          {
            withCredentials: true, // Enable sending cookies with the request
            headers: {
              Authorization: `Bearer ${access_token}`, // Include the access token as a request header
            },
          }
        );

        console.log(
          "Fetching insurance provider from database successful!!!",
          response.data
        );
        setInsuranceProviderDB(response.data);
      } catch (error) {
        console.error("Failed to fetch insurance provider data:", error);
        // Handle error fetching admission data
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Patient Registration Form
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Fill out the form to register as a patient.
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
                placeholder="Enter Gender"
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
                value={phonenumber}
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
            <Grid xs={12} sm={6} item>
              <TextField
                label="Emergency Contact Name"
                placeholder="Enter Emergency Contact Name"
                variant="outlined"
                type="text"
                value={emergency_contact_name}
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
                type="number"
                value={emergency_contact_phone}
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
                value={relationship}
                onChange={(event) => {
                  setRelationship(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>

            <Grid xs={12} item>
              <FormControlLabel
                control={
                  <Checkbox
                    checked={insurance}
                    onChange={(event) => {
                      setInsurance(event.target.checked);
                    }}
                    name="insurance"
                    color="primary"
                    size="small"
                    onBlur={() => setInsuranceTouched(true)}
                  />
                }
                label="Insurance"
                required={!insurance && insuranceTouched}
              />
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                id="provider_name"
                select
                label="Select Insurance Provider"
                value={provider_name}
                //defaultValue="In-person"
                //helperText="Please select appointment type"
                onChange={(event) => {
                  setProviderName(event.target.value);
                }}
                fullWidth
              >
                {insuranceProviderDB.map((item) => (
                  <MenuItem key={item.id} value={item.name}>
                    {item.name}
                  </MenuItem>
                ))}
              </TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Policy Number"
                placeholder="Enter Policy Number"
                variant="outlined"
                type="text"
                value={policy_number}
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
                value={group_number}
                onChange={(event) => {
                  setGroupNumber(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                //label="Relationship"
                helperText="Enter Effective Date"
                variant="outlined"
                type="date"
                value={effective_date}
                onChange={(event) => {
                  setEffectiveDate(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                // label="Relationship"
                helperText="Enter Expiration Date"
                variant="outlined"
                type="date"
                value={expiration_date}
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

export default PatientForm;
