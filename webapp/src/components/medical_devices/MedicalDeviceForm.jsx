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
import "./MedicalDevice.scss";

const MedicalDeviceForm = () => {
  const [name, setName] = useState("");
  const [manufacturer, setManufacturer] = useState("");
  const [model, setModel] = useState("");
  const [serial_number, setSerialNumber] = useState("");
  const [hospital, setHospital] = useState("");
  const [department, setDepartment] = useState("");
  const [last_maintenance, setLastMaintenance] = useState("");
  const [next_maintenance, setNextMaintenance] = useState("");

  const [hospitalDB, setHospitalDB] = useState([]);
  const [departmentDB, setDepartmentDB] = useState([]);

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
        manufacturer,
        model,
        serial_number,
        hospital,
        department,
        last_maintenance,
        next_maintenance,
      };

      await axios.post("http://127.0.0.1:8000/medical_device", data, {
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

  //Fetch hospital
  useEffect(() => {
    const fetchData = async () => {
      try {
        const access_token = document.cookie.replace(
          /(?:(?:^|.*;\s*)access_token\s*=\s*([^;]*).*$)|^.*$/,
          "$1"
        );

        const response = await axios.get("http://127.0.0.1:8000/hospital", {
          withCredentials: true, // Enable sending cookies with the request
          headers: {
            Authorization: `Bearer ${access_token}`, // Include the access token as a request header
          },
        });

        console.log(
          "Fetching insurance provider from database successful!!!",
          response.data
        );
        setHospitalDB(response.data);
      } catch (error) {
        console.error("Failed to fetch hospital data:", error);
        // Handle error fetching insurance provider data
      }
    };

    fetchData();
  }, []);

  //Fetch department
  useEffect(() => {
    const fetchData = async () => {
      try {
        const access_token = document.cookie.replace(
          /(?:(?:^|.*;\s*)access_token\s*=\s*([^;]*).*$)|^.*$/,
          "$1"
        );

        const response = await axios.get("http://127.0.0.1:8000/department", {
          withCredentials: true, // Enable sending cookies with the request
          headers: {
            Authorization: `Bearer ${access_token}`, // Include the access token as a request header
          },
        });

        console.log(
          "Fetching department from database successful!!!",
          response.data
        );
        setDepartmentDB(response.data);
      } catch (error) {
        console.error("Failed to fetch department data:", error);
        // Handle error fetching insurance provider data
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Medical Devices Form
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Fill out the form to register a medical device.
        </Typography>
        <form onSubmit={handleSubmit} className="admission_form">
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <TextField
                label=" Name"
                placeholder="Enter Name"
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
                label="Manufacturer"
                placeholder="Enter Manufacturer"
                variant="outlined"
                type="text"
                value={manufacturer}
                onChange={(event) => {
                  setManufacturer(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Model"
                placeholder="Enter Model"
                variant="outlined"
                type="text"
                value={model}
                onChange={(event) => {
                  setModel(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Serial Number"
                helperText="Enter Serial Number"
                variant="outlined"
                type="text"
                value={serial_number}
                onChange={(event) => {
                  setSerialNumber(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                id="hospital"
                select
                label="Select Hospital"
                value={hospital}
                onChange={(event) => {
                  setHospital(event.target.value);
                }}
                fullWidth
              >
                {hospitalDB.map((item) => (
                  <MenuItem key={item.id} value={item.name}>
                    {item.name}
                  </MenuItem>
                ))}
              </TextField>
            </Grid>

            <Grid xs={12} item>
              <TextField
                id="department"
                select
                label="Select Department"
                value={department}
                onChange={(event) => {
                  setDepartment(event.target.value);
                }}
                fullWidth
              >
                {departmentDB.map((item) => (
                  <MenuItem key={item.id} value={item.name}>
                    {item.name}
                  </MenuItem>
                ))}
              </TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                helperText="Enter Last Maintenance"
                variant="outlined"
                type="date"
                value={last_maintenance}
                onChange={(event) => {
                  setLastMaintenance(event.target.value);
                }}
                fullWidth
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                helperText="Enter Next Maintenance"
                variant="outlined"
                type="date"
                value={next_maintenance}
                onChange={(event) => {
                  setNextMaintenance(event.target.value);
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

export default MedicalDeviceForm;
