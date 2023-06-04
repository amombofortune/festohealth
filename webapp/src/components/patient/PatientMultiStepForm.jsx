import React, { useState, useEffect } from "react";
import {
  Button,
  Box,
  Step,
  StepLabel,
  Stepper,
  CardContent,
  Grid,
  TextField,
  Typography,
  FormControl,
  InputLabel,
  MenuItem,
  Select,
} from "@mui/material";
import axios from "axios";

const steps = [
  "Personal Information",
  "Emergency Information",
  "Insurance Information",
];

export default function PatientMultiStepForm() {
  const [formData, setFormData] = useState({
    firstname: "",
    middlename: "",
    lastname: "",
    dob: "",
    gender: "male",
    phonenumber: "",
    email: "",
    address: "",
    city: "",
    state: "",
    postal_code: "",
    country: "",
    emergency_contact_name: "",
    emergency_contact_phone: "",
    relationship: "",
    insurance: "",
    provider_name: "",
    policy_number: "",
    group_number: "",
    effective_date: "",
    expiration_date: "",
  });

  const [countryDB, setCountryDB] = useState([]);
  const [insuranceProviderDB, setInsuranceProviderDB] = useState([]);
  const [activeStep, setActiveStep] = React.useState(0);

  const handleNext = () => {
    setActiveStep((prevActiveStep) => prevActiveStep + 1);
  };

  const handleBack = () => {
    setActiveStep((prevActiveStep) => prevActiveStep - 1);
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

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
      await axios.post("http://127.0.0.1:8000/patient", formData, {
        withCredentials: true,
        headers,
      });
      window.location.reload(true);
      console.log("Posting data to database successful!!!");
    } catch (error) {
      console.error("Failed to post data to the database:", error);
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

  const renderStepContent = () => {
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
    } = formData;

    switch (activeStep) {
      case 0:
        return (
          <div>
            <Typography gutterBottom variant="h6">
              Personal Details
            </Typography>
            <Typography
              gutterBottom
              color="textSecondary"
              variant="body2"
              component="p"
            >
              Fill out the form to enter personal details.
            </Typography>
            <Grid container spacing={2}>
              <Grid item xs={12} sm={6}>
                <TextField
                  label="First Name"
                  name="firstname"
                  value={firstname}
                  onChange={handleChange}
                  fullWidth
                />
              </Grid>
              <Grid xs={12} sm={6} item>
                <TextField
                  label="Middle Name"
                  placeholder="Enter Middle Name"
                  variant="outlined"
                  type="text"
                  value={middlename}
                  onChange={handleChange}
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
                  onChange={handleChange}
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
                  onChange={handleChange}
                  fullWidth
                  required
                ></TextField>
              </Grid>
              <Grid item xs={12} sm={6}>
                <FormControl fullWidth variant="outlined">
                  <InputLabel>Gender</InputLabel>
                  <Select
                    value={gender}
                    onChange={handleChange}
                    label="Gender"
                    name="gender"
                  >
                    <MenuItem value="male">Male</MenuItem>
                    <MenuItem value="female">Female</MenuItem>
                    <MenuItem value="other">Other</MenuItem>
                  </Select>
                </FormControl>
              </Grid>
              <Grid xs={12} sm={6} item>
                <TextField
                  label="Phone Number"
                  helperText="Enter Phone Number"
                  variant="outlined"
                  type="number"
                  value={phonenumber}
                  onChange={handleChange}
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
                  onChange={handleChange}
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
                  onChange={handleChange}
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
                  onChange={handleChange}
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
                  onChange={handleChange}
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
                  onChange={handleChange}
                  fullWidth
                ></TextField>
              </Grid>

              <Grid xs={12} sm={6} item>
                <TextField
                  id="country"
                  select
                  label="Select Country"
                  value={country}
                  onChange={handleChange}
                  fullWidth
                >
                  {countryDB.map((item) => (
                    <MenuItem key={item.id} value={item.name}>
                      {item.name}
                    </MenuItem>
                  ))}
                </TextField>
              </Grid>
            </Grid>
          </div>
        );

      case 1:
        return (
          <div>
            <Typography gutterBottom variant="h6">
              Emergency Details
            </Typography>
            <Typography
              gutterBottom
              color="textSecondary"
              variant="body2"
              component="p"
            >
              Fill out the form to enter emergency information.
            </Typography>
            <Grid container spacing={2}>
              <Grid item xs={12} sm={6}>
                <TextField
                  label="Emergency Contact Name"
                  name="emergency_contact_name"
                  value={emergency_contact_name}
                  onChange={handleChange}
                  fullWidth
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <TextField
                  label="Emergency Contact Phone"
                  name="emergency_contact_phone"
                  value={emergency_contact_phone}
                  onChange={handleChange}
                  fullWidth
                />
              </Grid>
              <Grid xs={12} item>
                <TextField
                  label="Relationship"
                  placeholder="Enter Relationship"
                  variant="outlined"
                  type="text"
                  value={relationship}
                  onChange={handleChange}
                  fullWidth
                ></TextField>
              </Grid>
            </Grid>
          </div>
        );

      case 2:
        return (
          <div>
            <Typography gutterBottom variant="h6">
              Insurance Details
            </Typography>
            <Typography
              gutterBottom
              color="textSecondary"
              variant="body2"
              component="p"
            >
              Fill out the form to enter insurance information.
            </Typography>
            <Grid container spacing={2}>
              <Grid item xs={12} sm={6}>
                <TextField
                  label="Insurance"
                  name="insurance"
                  value={insurance}
                  onChange={handleChange}
                  fullWidth
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <TextField
                  label="Insurance Provider"
                  name="insurance"
                  value={provider_name}
                  onChange={handleChange}
                  select
                  fullWidth
                >
                  {insuranceProviderDB.map((provider) => (
                    <MenuItem key={provider.id} value={provider.name}>
                      {provider.name}
                    </MenuItem>
                  ))}
                </TextField>
              </Grid>
              <Grid item xs={12} sm={6}>
                <TextField
                  label="Policy Number"
                  name="policy_number"
                  value={policy_number}
                  onChange={handleChange}
                  fullWidth
                />
              </Grid>
              <Grid xs={12} sm={6} item>
                <TextField
                  label="Group Number"
                  placeholder="Enter Group Number"
                  variant="outlined"
                  type="text"
                  value={group_number}
                  onChange={handleChange}
                  fullWidth
                ></TextField>
              </Grid>
              <Grid xs={12} sm={6} item>
                <TextField
                  helperText="Enter Effective Date"
                  variant="outlined"
                  type="date"
                  value={effective_date}
                  onChange={handleChange}
                  fullWidth
                ></TextField>
              </Grid>
              <Grid xs={12} sm={6} item>
                <TextField
                  helperText="Enter Expiration Date"
                  variant="outlined"
                  type="date"
                  value={expiration_date}
                  onChange={handleChange}
                  fullWidth
                ></TextField>
              </Grid>
            </Grid>
          </div>
        );

      default:
        return null;
    }
  };

  return (
    <Box sx={{ maxWidth: 500, mx: "auto" }}>
      <Stepper activeStep={activeStep} alternativeLabel>
        {steps.map((label) => (
          <Step key={label}>
            <StepLabel>{label}</StepLabel>
          </Step>
        ))}
      </Stepper>

      <form onSubmit={handleSubmit}>
        <CardContent>{renderStepContent()}</CardContent>

        <Box sx={{ display: "flex", justifyContent: "space-between" }}>
          <Button disabled={activeStep === 0} onClick={handleBack}>
            Back
          </Button>
          <div>
            {activeStep !== steps.length - 1 && (
              <Button variant="contained" onClick={handleNext}>
                Next
              </Button>
            )}
            {activeStep === steps.length - 1 && (
              <Button
                type="submit"
                variant="contained"
                color="primary"
                onSubmit={handleSubmit}
              >
                Submit
              </Button>
            )}
          </div>
        </Box>
      </form>
    </Box>
  );
}
