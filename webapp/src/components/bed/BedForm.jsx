import {
  Button,
  Card,
  CardContent,
  Grid,
  TextField,
  Typography,
} from "@mui/material";
import React, { useState, useEffect } from "react";
import axios from "axios";
import MenuItem from "@mui/material/MenuItem";
import "./Bed.scss";
import { Checkbox, FormControlLabel } from "@mui/material";

const BedForm = () => {
  const [ward, setWard] = useState("");
  const [bed_no, setBedNo] = useState("");
  const [bed_type, setBedType] = useState("");
  const [availability, setAvailability] = useState(false);
  const [occupied_by, setOccupiedBy] = useState("");

  const [wardDB, setWardDB] = useState([]);

  const [availabilityTouched, setAvailabilityTouched] = useState(false);

  //Post data to database
  const handleSubmit = async (e) => {
    e.preventDefault();

    await axios
      .post("http://127.0.0.1:8000/bed", {
        ward,
        bed_no,
        bed_type,
        availability,
        occupied_by,
      })
      .then((res) => {
        window.location.reload(true);
        console.log("Posting data to database successful!!!", res);
      })
      .catch((err) => console.log(err));
  };

  //Fetch ward
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/ward")
      .then((res) => {
        console.log("Fetching ward from database successful!!!", res.data);
        setWardDB(res.data);
      })
      .catch((err) => console.log(err));
  }, []);

  return (
    <div>
      <Card
        style={{
          maxWidth: 700,
          margin: "0 auto",
          padding: "20px 5px",
        }}
      >
        <CardContent>
          <Typography gutterBottom variant="h5">
            Bed Form
          </Typography>
          <Typography
            gutterBottom
            color="textSecondary"
            variant="body2"
            component="p"
          >
            Fill out the form to add a bed.
          </Typography>
          <form onSubmit={handleSubmit} className="admission_form">
            <Grid container spacing={1}>
              <Grid xs={12} item>
                <TextField
                  id="ward"
                  select
                  label="Select Ward"
                  value={ward}
                  //defaultValue="In-person"
                  //helperText="Please select appointment type"
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
                  value={bed_no}
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
                  value={bed_type}
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
                      checked={availability}
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
                  value={occupied_by}
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
                  Submit
                </Button>
              </Grid>
            </Grid>
          </form>
        </CardContent>
      </Card>
    </div>
  );
};

export default BedForm;
