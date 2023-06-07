import React, { useState } from "react";
import { Link } from "react-router-dom";
import {
  Button,
  CardContent,
  Grid,
  TextField,
  Typography,
} from "@mui/material";
import MenuItem from "@mui/material/MenuItem";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { validateRegistration } from "./RegistrationValidation";
import "./registration.scss";

function Registration() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [user_type, setUserType] = useState("");
  const [errors, setErrors] = useState({});

  const navigate = useNavigate();

  const handleRegistrationSuccess = (user_type) => {
    // Redirect the user to the appropriate form component based on the userType
    const customURL = getCustomURL(user_type);
    navigate(customURL);
  };

  //Post data to database
  const handleSubmit = async (e) => {
    e.preventDefault();

    const validationErrors = validateRegistration(
      email,
      password,
      confirmPassword,
      user_type
    );
    setErrors(validationErrors);

    if (Object.keys(validationErrors).length > 0) {
      return;
    }

    try {
      const data = {
        email,
        password,
        user_type,
      };

      await axios.post("http://127.0.0.1:8000/users", data);

      // Redirect to the appropriate form component after successful registration
      handleRegistrationSuccess(user_type);
      console.log("Posting data to the database successful!!!");
    } catch (error) {
      console.error("Failed to post data to the database:", error);
      // Handle error posting data
    }
  };

  let formComponent;
  const getCustomURL = (user_type) => {
    // Define your custom URL paths based on user_type in the App.js Route component
    switch (user_type) {
      case "patient":
        return "/patientregistrationform";
      case "doctor":
        return "/doctorform";
      case "insuranceProvider":
        return "/insuranceproviderform";
      default:
        return "/";
    }
  };

  return (
    <div>
      {formComponent}
      <div
        style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          height: "100vh",
        }}
      >
        <div
          style={{
            width: "600px",
            border: "1px solid gray",
            borderRadius: "5px",
            padding: "5px",
          }}
        >
          <CardContent>
            <Typography gutterBottom variant="h5">
              Sign Up
            </Typography>
            <Typography
              gutterBottom
              color="textSecondary"
              variant="body2"
              component="p"
            >
              Fill out the form to sign up.
            </Typography>
            <form onSubmit={handleSubmit}>
              <Grid container spacing={1}>
                <Grid item xs={12}>
                  <TextField
                    select
                    label="User Type"
                    variant="outlined"
                    value={user_type}
                    onChange={(e) => setUserType(e.target.value)}
                    fullWidth
                  >
                    <MenuItem value="">Select user type</MenuItem>
                    <MenuItem value="patient">Patient</MenuItem>
                    <MenuItem value="doctor">Doctor</MenuItem>
                    <MenuItem value="insuranceProvider">
                      Insurance Provider
                    </MenuItem>
                  </TextField>
                  {errors.userTypeError && (
                    <p className="error-message">{errors.userTypeError}</p>
                  )}
                </Grid>
                <Grid xs={12} item>
                  <TextField
                    label="Email"
                    placeholder="Enter Email"
                    variant="outlined"
                    type="text"
                    name="email"
                    value={email}
                    onChange={(event) => {
                      setEmail(event.target.value);
                      setErrors((prevErrors) => ({
                        ...prevErrors,
                        emailError: "",
                      })); // Clear previous error
                    }}
                    fullWidth
                  ></TextField>
                  {errors.emailError && (
                    <p className="error-message">{errors.emailError}</p>
                  )}
                </Grid>
                <Grid xs={12} item>
                  <TextField
                    label="Password"
                    placeholder="Enter Password"
                    variant="outlined"
                    type="password"
                    name="password"
                    value={password}
                    onChange={(event) => {
                      setPassword(event.target.value);
                      setErrors((prevErrors) => ({
                        ...prevErrors,
                        passwordError: "",
                      })); // Clear previous error
                    }}
                    fullWidth
                  ></TextField>
                  {errors.passwordError && (
                    <p className="error-message">{errors.passwordError}</p>
                  )}
                </Grid>
                <Grid xs={12} item>
                  <TextField
                    label="Confirm Password"
                    placeholder="Confirm Password"
                    variant="outlined"
                    type="password"
                    name="confirmPassword"
                    value={confirmPassword}
                    onChange={(event) => {
                      setConfirmPassword(event.target.value);
                      setErrors((prevErrors) => ({
                        ...prevErrors,
                        confirmPasswordError: "",
                      })); // Clear previous error
                    }}
                    fullWidth
                  ></TextField>
                  {errors.confirmPasswordError && (
                    <p className="error-message">
                      {errors.confirmPasswordError}
                    </p>
                  )}
                </Grid>

                <Grid xs={12} item>
                  <Button
                    type="submit"
                    variant="contained"
                    color="primary"
                    fullWidth
                  >
                    Sign Up
                  </Button>
                </Grid>
                <p>You agree to our terms and policies</p>

                <Grid xs={12} item>
                  <Link to="/login" className="text-decoration-none">
                    <Button
                      type="submit"
                      variant="contained"
                      color="primary"
                      fullWidth
                    >
                      Login
                    </Button>
                  </Link>
                </Grid>
              </Grid>
            </form>
          </CardContent>
        </div>
      </div>
    </div>
  );
}

export default Registration;
