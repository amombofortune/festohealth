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

    await axios
      .post("http://127.0.0.1:8000/medical_device", {
        name,
        manufacturer,
        model,
        serial_number,
        hospital,
        department,
        last_maintenance,
        next_maintenance,
      })
      .then((res) => {
        window.location.reload(true);
        console.log("Posting data to database successful!!!", res);
      })
      .catch((err) => console.log(err));
  };

  //Fetch hospital
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/hospital")
      .then((res) => {
        console.log("Fetching hospital from database successful!!!", res.data);
        setHospitalDB(res.data);
      })
      .catch((err) => console.log(err));
  }, []);

  //Fetch department
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/department")
      .then((res) => {
        console.log(
          "Fetching department from database successful!!!",
          res.data
        );
        setDepartmentDB(res.data);
      })
      .catch((err) => console.log(err));
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
