import React, { useState, useContext } from "react";
import { Link } from "react-router-dom";
import {
  Button,
  CardContent,
  Grid,
  TextField,
  Typography,
} from "@mui/material";
import { useNavigate } from "react-router-dom";
import { axiosInstance, handleExpiredToken } from "./axiosInstance";
import "react-toastify/dist/ReactToastify.css";
import { validateLogin } from "./LoginValidation";
import UserContext from "../../contexts/UserContext";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState({});

  const { setUserData } = useContext(UserContext);

  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    const validationErrors = validateLogin(email, password);
    setErrors(validationErrors);

    if (Object.keys(validationErrors).length > 0) {
      console.log("Validation Errors:", validationErrors);
      return;
    }

    try {
      const formData = new FormData();
      formData.append("username", email);
      formData.append("password", password);

      const response = await axiosInstance.post("/login", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
        withCredentials: true,
      });

      const {
        data: { access_token, user_id, email: userEmail, user_type, image },
      } = response;

      setUserData({
        access_token,
        user_id,
        email: userEmail,
        user_type,
        image,
      });

      console.log("Login Successful");
      document.cookie = `access_token=${access_token}; path=/;`;

      navigate("/");
    } catch (error) {
      console.error("Login Failed:", error);
      if (error.response && error.response.status === 401) {
        handleExpiredToken(navigate);
      } else {
        setErrors({ login: "Failed to log in. Please try again." });
      }
    } finally {
      setEmail("");
      setPassword("");
    }
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
            Sign In
          </Typography>
          <Typography
            gutterBottom
            color="textSecondary"
            variant="body2"
            component="p"
          >
            Fill out the form to sign in.
          </Typography>
          <form onSubmit={handleSubmit}>
            <Grid container spacing={1}>
              <Grid xs={12} item>
                <TextField
                  label="Email"
                  placeholder="Enter Email"
                  variant="outlined"
                  type="text"
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
                <Button
                  type="submit"
                  variant="contained"
                  color="primary"
                  fullWidth
                >
                  Login
                </Button>
              </Grid>
              <p>Not registered yet. Sign Up!</p>

              <Grid xs={12} item>
                <Link to="/registration" className="text-decoration-none">
                  <Button
                    type="submit"
                    variant="contained"
                    color="primary"
                    fullWidth
                  >
                    Sign Up
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

export default Login;
