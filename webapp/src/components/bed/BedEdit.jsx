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
import { Checkbox, FormControlLabel } from "@mui/material";

import "./Bed.scss";

const BedEdit = ({ selectedRow }) => {
  const { ward, bed_no, bed_type, availability, occupied_by } = selectedRow;

  const [wardValue, setWard] = useState(ward);
  const [bedNo, setBedNo] = useState(bed_no);
  const [bedType, setBedType] = useState(bed_type);
  const [availabilityValue, setAvailability] = useState(availability);
  const [occupiedBy, setOccupiedBy] = useState(occupied_by);

  const [wardDB, setWardDB] = useState([]);
  const [availabilityTouched, setAvailabilityTouched] = useState(false);

  //Update record
  const handleUpdate = async () => {
    const appointmentData = {
      ward: wardValue,
      bed_no: bedNo,
      bed_type: bedType,
      availability: availabilityValue,
      occupied_by: occupiedBy,
    };

    try {
      const res = await axios.put(
        `http://127.0.0.1:8000/bed/${selectedRow.id}`,
        appointmentData
      );
      console.log("Updated!!", res);
      window.location.reload(true);
    } catch (err) {
      console.log(err);
    }
  };

  //Fetch ward
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/ward")
      .then((res) => {
        console.log(
          "Fetching appointment type from database successful!!!",
          res.data
        );
        setWardDB(res.data);
      })
      .catch((err) => console.log(err));
  }, []);

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Are you sure you want to update bed?
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Edit out this form and we will update bed.
        </Typography>
        <form onSubmit={handleUpdate} style={{ marginTop: "10px" }}>
          <Grid container spacing={1}>
            <Grid xs={12} item>
              <TextField
                id="ward"
                select
                label="Select Ward"
                value={wardValue}
                onChange={(event) => {
                  setWard(event.target.value);
                }}
                fullWidth
              >
                {wardDB.map((item) => (
                  <MenuItem key={item.id} value={item.name}>
                    {item.name}
                  </MenuItem>
                ))}
              </TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Bed Number"
                placeholder="Enter Bed Number"
                variant="outlined"
                type="number"
                value={bedNo}
                onChange={(event) => {
                  setBedNo(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                label="Bed Type"
                placeholder="Enter Bed Type"
                variant="outlined"
                type="text"
                value={bedType}
                onChange={(event) => {
                  setBedType(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <FormControlLabel
                control={
                  <Checkbox
                    checked={availabilityValue}
                    onChange={(event) => {
                      setAvailability(event.target.checked);
                    }}
                    name="availability"
                    color="primary"
                    size="small"
                    onBlur={() => setAvailabilityTouched(true)}
                  />
                }
                label="Availability"
                required={!availability && availabilityTouched}
              />
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Occupied By"
                placeholder="Occupied By"
                variant="outlined"
                type="number"
                value={occupiedBy}
                onChange={(event) => {
                  setOccupiedBy(event.target.value);
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
                Update
              </Button>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default BedEdit;
