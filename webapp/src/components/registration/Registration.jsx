import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import {
  Button,
  CardContent,
  Grid,
  TextField,
  Typography,
} from "@mui/material";
import axios from "axios";

function Registration() {
  const initialValues = {
    email: "",
    password: "",
    role: "",
  };
  const [formValues, setFormValues] = useState(initialValues);
  const [formErrors, setFormErrors] = useState({});
  const [isSubmit, setIsSubmit] = useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormValues({ ...formValues, [name]: value });
  };

  //Post data to database
  const handleSubmit = async (e) => {
    e.preventDefault();
    setFormErrors(validate(formValues));
    setIsSubmit(true);

    await axios
      .post("http://127.0.0.1:8000/user_account", formValues)
      .then((res) => {
        window.location.reload(true);
        console.log("Posting data to database successful!!!", res);
      })
      .catch((err) => console.log(err));
  };

  useEffect(() => {
    console.log(formErrors);
    if (Object.keys(formErrors).length === 0 && isSubmit) {
      console.log(formValues);
    }
  }, [formErrors, formValues, isSubmit]);

  const validate = (values) => {
    const errors = {};
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/i;
    if (!values.role) {
      errors.role = "Role is required!";
    }
    if (!values.email) {
      errors.email = "Email is required!";
    } else if (!regex.test(values.email)) {
      errors.email = "This is not a valid email format!";
    }
    if (!values.password) {
      errors.password = "Password is required";
    } else if (values.password.length < 4) {
      errors.password = "Password must be more than 4 characters";
    } else if (values.password.length > 10) {
      errors.password = "Password cannot exceed more than 10 characters";
    }
    return errors;
  };

  return (
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
              <Grid xs={12} item>
                <TextField
                  label="Email"
                  placeholder="Enter Email"
                  variant="outlined"
                  type="text"
                  name="email"
                  value={formValues.email}
                  onChange={handleChange}
                  fullWidth
                ></TextField>
              </Grid>
              <p>{formErrors.email}</p>
              <Grid xs={12} item>
                <TextField
                  label="Password"
                  placeholder="Enter Password"
                  variant="outlined"
                  type="password"
                  name="password"
                  value={formValues.password}
                  onChange={handleChange}
                  fullWidth
                ></TextField>
              </Grid>
              <p>{formErrors.password}</p>

              <Grid xs={12} item>
                <TextField
                  label="Role"
                  placeholder="Enter Role"
                  variant="outlined"
                  type="text"
                  name="role"
                  value={formValues.role}
                  onChange={handleChange}
                  fullWidth
                ></TextField>
              </Grid>
              <p>{formErrors.role}</p>

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
  );
}

export default Registration;
