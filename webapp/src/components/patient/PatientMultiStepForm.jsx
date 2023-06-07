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
  const [hasInsurance, setHasInsurance] = useState(false);

  const [activeStep, setActiveStep] = React.useState(0);

  const handleNext = () => {
    setActiveStep((prevActiveStep) => prevActiveStep + 1);
  };

  const handleBack = () => {
    setActiveStep((prevActiveStep) => prevActiveStep - 1);
  };

  const handleInsuranceChange = (event) => {
    const value = event.target.value;
    const isInsurance = value === "yes";

    setInsurance(value); // Update the insurance state variable with the selected value
    setHasInsurance(isInsurance);

    if (!isInsurance) {
      setProviderName("");
      setPolicyNumber("");
      setGroupNumber("");
      setEffectiveDate("");
      setExpirationDate("");
    }
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
        insurance: insurance,
        provider_name: hasInsurance ? provider_name : null,
        policy_number: hasInsurance ? policy_number : null,
        group_number: hasInsurance ? group_number : null,
        effective_date: hasInsurance ? effective_date : null,
        expiration_date: hasInsurance ? expiration_date : null,
      };

      await axios.post("http://127.0.0.1:8000/patient", data, {
        withCredentials: true, // Enable sending cookies with the request
        headers,
      });

      window.location.reload();
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
        const response = await axios.get("http://127.0.0.1:8000/country");
        console.log(
          "Fetching country from database successful!!!",
          response.data
        );
        setCountryDB(response.data);
      } catch (error) {
        console.error("Failed to fetch country data:", error);
        // Handle error fetching country data
      }
    };

    fetchData();
  }, []);

  //Fetch insurance provider
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(
          "http://127.0.0.1:8000/insurance_provider"
        );
        console.log(
          "Fetching insurance provider from database successful!!!",
          response.data
        );
        setInsuranceProviderDB(response.data);
      } catch (error) {
        console.error("Failed to fetch insurance provider data:", error);
        // Handle error fetching country data
      }
    };

    fetchData();
  }, []);

  const renderStepContent = () => {
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
                  onChange={(event) => {
                    setFirstName(event.target.value);
                  }}
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
              <Grid item xs={12} sm={6}>
                <FormControl fullWidth variant="outlined">
                  <InputLabel>Gender</InputLabel>
                  <Select
                    value={gender}
                    onChange={(event) => {
                      setGender(event.target.value);
                    }}
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
                  type="text"
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
                  onChange={(event) => {
                    setEmergencyContactName(event.target.value);
                  }}
                  fullWidth
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <TextField
                  label="Emergency Contact Phone"
                  name="emergency_contact_phone"
                  value={emergency_contact_phone}
                  onChange={(event) => {
                    setEmergencyContactPhone(event.target.value);
                  }}
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
                  onChange={(event) => {
                    setRelationship(event.target.value);
                  }}
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
              <Grid item xs={12}>
                <TextField
                  label="Do you have insurance?"
                  name="insurance"
                  value={insurance}
                  onChange={handleInsuranceChange}
                  select
                  fullWidth
                >
                  <MenuItem value="yes">Yes</MenuItem>
                  <MenuItem value="no">No</MenuItem>
                </TextField>
              </Grid>
              {hasInsurance && ( // Render the text fields conditionally based on the value of hasInsurance
                <>
                  <Grid xs={12} item>
                    <TextField
                      id="provider_name"
                      select
                      label="Select Provider Name"
                      value={provider_name}
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
                  <Grid item xs={12} sm={6}>
                    <TextField
                      label="Policy Number"
                      name="policy_number"
                      value={policy_number}
                      onChange={(event) => {
                        setPolicyNumber(event.target.value);
                      }}
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
                      onChange={(event) => {
                        setGroupNumber(event.target.value);
                      }}
                      fullWidth
                    ></TextField>
                  </Grid>
                  <Grid xs={12} sm={6} item>
                    <TextField
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
                </>
              )}
            </Grid>
          </div>
        );

      default:
        return null;
    }
  };

  return (
    <Box sx={{ maxWidth: 900, mx: "auto" }}>
      <div>
        <Stepper activeStep={activeStep} alternativeLabel>
          {steps.map((label) => (
            <Step key={label}>
              <StepLabel>{label}</StepLabel>
            </Step>
          ))}
        </Stepper>

        <form onSubmit={handleSubmit}>
          <CardContent>{renderStepContent()}</CardContent>

          <Box
            sx={{
              display: "flex",
              justifyContent: "space-between",
              marginBottom: "50px",
            }}
          >
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
      </div>
    </Box>
  );
}
