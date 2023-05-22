import React, { useState } from "react";
import { Link } from "react-router-dom";
import {
  Button,
  CardContent,
  Grid,
  TextField,
  Typography,
} from "@mui/material";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  //Post data to database
  const handleSubmit = async (e) => {
    e.preventDefault();
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
