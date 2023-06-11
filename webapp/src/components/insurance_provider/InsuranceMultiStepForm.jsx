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
  MenuItem,
} from "@mui/material";
import axios from "axios";

const steps = [
  "Provider Information",
  "Business Information",
  "Contact Information",
];

export default function InsuranceMultiStepForm() {
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [products, setProducts] = useState("");
  const [address, setAddress] = useState("");
  const [city, setCity] = useState("");
  const [state, setState] = useState("");
  const [postal_code, setPostalCode] = useState("");
  const [country, setCountry] = useState("");
  const [phone_number, setPhoneNumber] = useState("");
  const [email, setEmail] = useState("");
  const [website, setWebsite] = useState("");
  const [licence_number, setLicenceNumber] = useState("");
  const [certification, setCertification] = useState("");
  const [certification_type, setCertificationType] = useState("");
  const [certification_number, setCertificationNumber] = useState("");
  const [issuing_authority, setIssuingAuthority] = useState("");
  const [issue_date, setIssueDate] = useState("");
  const [expiration_date, setExpirationDate] = useState("");
  const [customer_support_phone, setCustomerSupportPhone] = useState("");
  const [customer_support_email, setCustomerSupportEmail] = useState("");
  const [rating, setRating] = useState("");
  const [verified, setVerified] = useState(false);

  const [countryDB, setCountryDB] = useState([]);
  const [hasCertification, setHasCertification] = useState(false);

  const [activeStep, setActiveStep] = React.useState(0);

  const handleNext = () => {
    setActiveStep((prevActiveStep) => prevActiveStep + 1);
  };

  const handleBack = () => {
    setActiveStep((prevActiveStep) => prevActiveStep - 1);
  };

  const handleCertificationChange = (event) => {
    const value = event.target.value;
    const isCertified = value === "yes";

    setCertification(value); // Update the insurance state variable with the selected value
    setHasCertification(isCertified);

    if (!isCertified) {
      setCertificationType("");
      setCertificationNumber("");
      setIssuingAuthority("");
      setIssueDate("");
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
        name,
        description,
        products,
        address,
        city,
        state,
        postal_code,
        country,
        phone_number,
        email,
        website,
        licence_number,
        certification: certification,
        certification_type: hasCertification ? certification_type : null,
        certification_number: hasCertification ? certification_number : null,
        issuing_authority: hasCertification ? issuing_authority : null,
        issue_date: hasCertification ? issue_date : null,
        expiration_date: hasCertification ? expiration_date : null,
        customer_support_phone,
        customer_support_email,
        rating,
        verified,
      };

      await axios.post("http://127.0.0.1:8000/insurance_provider", data, {
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

  const renderStepContent = () => {
    switch (activeStep) {
      case 0:
        return (
          <div>
            <Typography gutterBottom variant="h6">
              Provider Details
            </Typography>
            <Typography
              gutterBottom
              color="textSecondary"
              variant="body2"
              component="p"
            >
              Fill out the form to enter provider details.
            </Typography>
            <Grid container spacing={2}>
              <Grid xs={12} item>
                <TextField
                  label=" Provider Name"
                  placeholder="Enter Provider Name"
                  variant="outlined"
                  type="text"
                  value={name}
                  onChange={(event) => {
                    setName(event.target.value);
                  }}
                  fullWidth
                  required
                ></TextField>
              </Grid>
              <Grid xs={12} item>
                <TextField
                  label=" Description"
                  placeholder="Enter Description"
                  variant="outlined"
                  type="text"
                  value={description}
                  onChange={(event) => {
                    setDescription(event.target.value);
                  }}
                  fullWidth
                  multiline
                  rows={4}
                  required
                ></TextField>
              </Grid>
              <Grid xs={12} item>
                <TextField
                  label=" Products"
                  placeholder="Enter Products"
                  variant="outlined"
                  type="text"
                  value={products}
                  onChange={(event) => {
                    setProducts(event.target.value);
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
              <Grid xs={12} sm={6} item>
                <TextField
                  label="Phone number"
                  placeholder="Enter Phone Number"
                  variant="outlined"
                  type="text"
                  value={phone_number}
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
                  value={email}
                  onChange={(event) => {
                    setEmail(event.target.value);
                  }}
                  fullWidth
                ></TextField>
              </Grid>
              <Grid xs={12} item>
                <TextField
                  label="Website"
                  placeholder="Enter Website"
                  variant="outlined"
                  type="text"
                  value={website}
                  onChange={(event) => {
                    setWebsite(event.target.value);
                  }}
                  fullWidth
                ></TextField>
              </Grid>
            </Grid>
          </div>
        );

      case 1:
        return (
          <div>
            <Typography gutterBottom variant="h6">
              Business Details
            </Typography>
            <Typography
              gutterBottom
              color="textSecondary"
              variant="body2"
              component="p"
            >
              Fill out the form to enter business information.
            </Typography>
            <Grid container spacing={2}>
              <Grid xs={12} item>
                <TextField
                  label="Licence Number"
                  placeholder="Enter Licence Number"
                  variant="outlined"
                  type="text"
                  value={licence_number}
                  onChange={(event) => {
                    setLicenceNumber(event.target.value);
                  }}
                  fullWidth
                ></TextField>
              </Grid>
              <Grid item xs={12}>
                <TextField
                  label="Do you have certification?"
                  name="certification"
                  value={certification}
                  onChange={handleCertificationChange}
                  select
                  fullWidth
                >
                  <MenuItem value="yes">Yes</MenuItem>
                  <MenuItem value="no">No</MenuItem>
                </TextField>
              </Grid>
              {hasCertification && ( // Render the text fields conditionally based on the value of hasInsurance
                <>
                  <Grid item xs={12} sm={6}>
                    <TextField
                      label="Certification Type"
                      name="certification_type"
                      value={certification_type}
                      onChange={(event) => {
                        setCertificationType(event.target.value);
                      }}
                      fullWidth
                    />
                  </Grid>
                  <Grid item xs={12} sm={6}>
                    <TextField
                      label="Certification Number"
                      name="certification_number"
                      value={certification_number}
                      onChange={(event) => {
                        setCertificationNumber(event.target.value);
                      }}
                      fullWidth
                    />
                  </Grid>
                  <Grid xs={12} sm={6} item>
                    <TextField
                      label="Issuing Authority"
                      placeholder="Enter Issuing Authority"
                      variant="outlined"
                      type="text"
                      value={issuing_authority}
                      onChange={(event) => {
                        setIssuingAuthority(event.target.value);
                      }}
                      fullWidth
                    ></TextField>
                  </Grid>
                  <Grid xs={12} sm={6} item>
                    <TextField
                      helperText="Enter Issue Date"
                      variant="outlined"
                      type="date"
                      value={issue_date}
                      onChange={(event) => {
                        setIssueDate(event.target.value);
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

      case 2:
        return (
          <div>
            <Typography gutterBottom variant="h6">
              Contact Details
            </Typography>
            <Typography
              gutterBottom
              color="textSecondary"
              variant="body2"
              component="p"
            >
              Fill out the form to enter contact information.
            </Typography>
            <Grid container spacing={2}>
              <Grid xs={12} sm={6} item>
                <TextField
                  label="Customer Phone Number"
                  placeholder="Enter Customer Phone Number"
                  variant="outlined"
                  type="text"
                  value={customer_support_phone}
                  onChange={(event) => {
                    setCustomerSupportPhone(event.target.value);
                  }}
                  fullWidth
                ></TextField>
              </Grid>
              <Grid xs={12} sm={6} item>
                <TextField
                  label="Customer Phone Email"
                  placeholder="Enter Customer Phone Email"
                  variant="outlined"
                  type="text"
                  value={customer_support_email}
                  onChange={(event) => {
                    setCustomerSupportEmail(event.target.value);
                  }}
                  fullWidth
                ></TextField>
              </Grid>
              <Grid xs={12} sm={6} item>
                <TextField
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
                  placeholder="Enter Verification"
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
