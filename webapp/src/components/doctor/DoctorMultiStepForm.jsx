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
  FormControlLabel,
  FormLabel,
  MenuItem,
  Radio,
  RadioGroup,
} from "@mui/material";
import axios from "axios";

const steps = [
  "Personal Information",
  "Professional Information",
  "Insurance Information",
];

export default function DoctorMultiStepForm() {
  const [firstname, setFirstName] = useState("");
  const [middlename, setMiddleName] = useState("");
  const [lastname, setLastName] = useState("");
  const [dob, setDOB] = useState("");
  const [gender, setGender] = useState("male");
  const [phone_number, setPhoneNumber] = useState("");
  const [email, setEmail] = useState("");
  const [specialty, setSpecialty] = useState("");
  const [licence_number, setLicenceNumber] = useState("");
  const [address, setAddress] = useState("");
  const [city, setCity] = useState("");
  const [state, setState] = useState("");
  const [postal_code, setPostalCode] = useState("");
  const [country, setCountry] = useState("");
  const [consultation_fee, setConsultationFee] = useState("");
  const [rating, setRating] = useState("");
  const [membership, setMembership] = useState("");
  const [organization_name, setOrganizationName] = useState("");
  const [membership_type, setMembershipType] = useState("");
  const [membership_number, setMembershipNumber] = useState("");
  const [start_date, setStartDate] = useState("");
  const [expiration_date, setExpirationDate] = useState("");
  const [membership_status, setMembershipStatus] = useState("");
  const [verified, setVerified] = useState("");

  const [countryDB, setCountryDB] = useState([]);
  const [organizationDB, setOrganizationDB] = useState([]);
  const [specialtyDB, setSpecialtyDB] = useState([]);
  const [hasMembership, setHasMembership] = useState(false);

  const [activeStep, setActiveStep] = React.useState(0);

  const handleNext = () => {
    setActiveStep((prevActiveStep) => prevActiveStep + 1);
  };

  const handleBack = () => {
    setActiveStep((prevActiveStep) => prevActiveStep - 1);
  };

  const handleMembershipChange = (event) => {
    const value = event.target.value;
    const isMembership = value === "yes";

    setMembership(value); // Update the insurance state variable with the selected value
    setHasMembership(isMembership);

    if (!isMembership) {
      setOrganizationName("");
      setMembershipType("");
      setMembershipNumber("");
      setStartDate("");
      setExpirationDate("");
      setMembershipStatus("");
    }
  };

  //Post data to database
  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const access_token = document.cookie
        .split(";")
        .map((cookie) => cookie.trim())
        .find((cookie) => cookie.startsWith("access_token="))
        ?.split("=")[1];

      const headers = {
        Authorization: `Bearer ${access_token}`,
        "Content-Type": "application/json",
      };

      console.log("Access Token:", access_token);
      console.log("document.cookie:", document.cookie);

      const data = {
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
        consultation_fee,
        rating,
        membership,
        organization_name: hasMembership ? organization_name : null,
        membership_type: hasMembership ? membership_type : null,
        membership_number: hasMembership ? membership_number : null,
        start_date: hasMembership ? start_date : null,
        expiration_date: hasMembership ? expiration_date : null,
        membership_status: hasMembership ? membership_status : null,
        verified,
      };

      await axios.post("http://127.0.0.1:8000/doctor", data, {
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

  //Fetch specialties
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/specialty");
        console.log(
          "Fetching specialty from database successful!!!",
          response.data
        );
        setSpecialtyDB(response.data);
      } catch (error) {
        console.error("Failed to fetch specialty data:", error);
        // Handle error fetching country data
      }
    };

    fetchData();
  }, []);

  //Fetch organization
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(
          "http://127.0.0.1:8000/doctor_membership"
        );
        console.log(
          "Fetching membership organization from database successful!!!",
          response.data
        );
        setOrganizationDB(response.data);
      } catch (error) {
        console.error("Failed to fetch organization data:", error);
        // Handle error fetching membership organization data
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

              <Grid xs={12} item>
                <FormControl>
                  <FormLabel id="demo-row-radio-buttons-group-label">
                    Gender
                  </FormLabel>
                  <RadioGroup
                    row
                    aria-labelledby="demo-row-radio-buttons-group-label"
                    name="row-radio-buttons-group"
                    type="text"
                    value={gender}
                    onChange={(event) => {
                      setGender(event.target.value);
                    }}
                  >
                    <FormControlLabel
                      value="male"
                      control={<Radio />}
                      label="Male"
                    />
                    <FormControlLabel
                      value="female"
                      control={<Radio />}
                      label="Female"
                    />
                    <FormControlLabel
                      value="other"
                      control={<Radio />}
                      label="Other"
                    />
                  </RadioGroup>
                </FormControl>
              </Grid>
              <Grid xs={12} sm={6} item>
                <TextField
                  label="Phone Number"
                  helperText="Enter Phone Number"
                  variant="outlined"
                  type="text"
                  value={phone_number}
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
              Professional Information
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
              <Grid xs={12} item>
                <TextField
                  label="Medical Licence number"
                  placeholder="Enter Medical Licence number"
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
                  id="specialty"
                  select
                  label="Select Specialty"
                  value={specialty}
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
              <Grid item xs={12}>
                <TextField
                  label="Do you have professional membership?"
                  name="membership"
                  value={membership}
                  onChange={handleMembershipChange}
                  select
                  fullWidth
                >
                  <MenuItem value="yes">Yes</MenuItem>
                  <MenuItem value="no">No</MenuItem>
                </TextField>
              </Grid>
              {hasMembership && ( // Render the text fields conditionally based on the value of hasMembership
                <>
                  <Grid xs={12} item>
                    <TextField
                      id="organization_name"
                      select
                      label="Select Organization Name"
                      value={organization_name}
                      onChange={(event) => {
                        setOrganizationName(event.target.value);
                      }}
                      fullWidth
                    >
                      {organizationDB.map((item) => (
                        <MenuItem key={item.id} value={item.name}>
                          {item.name}
                        </MenuItem>
                      ))}
                    </TextField>
                  </Grid>
                  <Grid item xs={12} sm={6}>
                    <TextField
                      label="Membership Type"
                      name="membership_type"
                      value={membership_type}
                      onChange={(event) => {
                        setMembershipType(event.target.value);
                      }}
                      fullWidth
                    />
                  </Grid>
                  <Grid xs={12} sm={6} item>
                    <TextField
                      label="Membership Number"
                      placeholder="Enter Membership Number"
                      variant="outlined"
                      type="text"
                      value={membership_number}
                      onChange={(event) => {
                        setMembershipNumber(event.target.value);
                      }}
                      fullWidth
                    ></TextField>
                  </Grid>
                  <Grid xs={12} sm={6} item>
                    <TextField
                      helperText="Enter Membership Start Date"
                      variant="outlined"
                      type="date"
                      value={start_date}
                      onChange={(event) => {
                        setStartDate(event.target.value);
                      }}
                      fullWidth
                    ></TextField>
                  </Grid>
                  <Grid xs={12} sm={6} item>
                    <TextField
                      helperText="Enter Membership Expiration Date"
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
                    <TextField
                      helperText="Enter Membership Status"
                      variant="outlined"
                      type="text"
                      value={membership_status}
                      onChange={(event) => {
                        setMembershipStatus(event.target.value);
                      }}
                      fullWidth
                    ></TextField>
                  </Grid>
                </>
              )}
              <Grid xs={12} sm={6} item>
                <TextField
                  label="Consultation Fee"
                  placeholder="Enter Consultation Fee"
                  variant="outlined"
                  type="number"
                  value={consultation_fee}
                  onChange={(event) => {
                    setConsultationFee(event.target.value);
                  }}
                  fullWidth
                ></TextField>
              </Grid>
              <Grid xs={12} sm={6} item>
                <TextField
                  label="Rating"
                  placeholder="Enter Rating"
                  variant="outlined"
                  type="number"
                  value={rating}
                  onChange={(event) => {
                    setRating(event.target.value);
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
                  value={verified}
                  onChange={(event) => {
                    setVerified(event.target.value);
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
              Profile Picture
            </Typography>
            <Typography
              gutterBottom
              color="textSecondary"
              variant="body2"
              component="p"
            >
              Upload your profile pictures so clients can see you.
            </Typography>
            <Typography>This is where to upload profile picture</Typography>
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
