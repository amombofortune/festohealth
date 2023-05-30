import React, { useState } from "react";
import { Link } from "react-router-dom";
import {
  Button,
  CardContent,
  Grid,
  TextField,
  Typography,
} from "@mui/material";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import { toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post("http://127.0.0.1:8000/login", {
        email,
        password,
      });
      // Do something with the response, such as storing the authentication token
      // and redirecting to a protected page
      // ...

      // Reset the form fields after successful login
      setEmail("");
      setPassword("");

      navigate("/"); // Replace '/' with your desired route
    } catch (error) {
      if (error.response) {
        // The request was made and the server responded with a status code
        // that falls out of the range of 2xx
        const { status, data } = error.response;
        console.log("Error status:", status);
        console.log("Error data:", data);

        // Display an error toast notification to the user
        toast.error(data.message); // Replace 'data.message' with the actual error message from the API response
      } else if (error.request) {
        // The request was made but no response was received
        // Error with the network or server is down
        console.log("Error request:", error.request);

        // Display an error toast notification to the user
        toast.error("Network Error. Please try again later.");
      } else {
        // Something else happened in making the request
        console.log("Error message:", error.message);

        // Display an error toast notification to the user
        toast.error("An error occurred. Please try again.");
      }
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
                  }}
                  fullWidth
                  required
                ></TextField>
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
                  }}
                  fullWidth
                  required
                ></TextField>
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
