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

const MedicalDeviceEdit = ({ selectedRow }) => {
  const {
    name,
    manufacturer,
    model,
    serial_number,
    hospital,
    department,
    last_maintenance,
    next_maintenance,
  } = selectedRow;

  const [nameValue, setName] = useState(name);
  const [manufacturerValue, setManufacturer] = useState(manufacturer);
  const [modelValue, setModel] = useState(model);
  const [serialNumber, setSerialNumber] = useState(serial_number);
  const [hospitalValue, setHospital] = useState(hospital);
  const [departmentValue, setDepartment] = useState(department);
  const [lastMaintenance, setLastMaintenance] = useState(last_maintenance);
  const [nextMaintenance, setNextMaintenance] = useState(next_maintenance);

  const [hospitalDB, setHospitalDB] = useState([]);
  const [departmentDB, setDepartmentDB] = useState([]);

  //Update record
  const handleUpdate = async () => {
    const appointmentData = {
      name: nameValue,
      manufacturer: manufacturerValue,
      model: modelValue,
      serial_number: serialNumber,
      hospital: hospitalValue,
      department: departmentValue,
      last_maintenance: lastMaintenance,
      next_maintenance: nextMaintenance,
    };

    try {
      const res = await axios.put(
        `http://127.0.0.1:8000/medical_device/${selectedRow.id}`,
        appointmentData
      );
      console.log("Updated!!", res);
      window.location.reload(true);
    } catch (err) {
      console.log(err);
    }
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
          Are you sure you want to update medical device?
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Edit out this form and we will update your medical device.
        </Typography>
        <form onSubmit={handleUpdate} style={{ marginTop: "10px" }}>
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <TextField
                label=" Name"
                placeholder="Enter Name"
                variant="outlined"
                type="text"
                value={nameValue}
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
                value={manufacturerValue}
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
                value={modelValue}
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
                value={serialNumber}
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
                value={hospitalValue}
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
                value={departmentValue}
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
                value={lastMaintenance}
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
                value={nextMaintenance}
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
                Update
              </Button>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default MedicalDeviceEdit;
