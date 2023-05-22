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
import "./InsuranceClaim.scss";

const InsuranceClaimForm = () => {
  const [patient_id, setPatientID] = useState("");
  const [provider_id, setProviderID] = useState("");
  const [date_of_service, setDateOfService] = useState("");
  const [procedure_code, setProcedureCode] = useState("");
  const [diagnosis_code, setDiagnosisCode] = useState("");
  const [billed_amount, setBilledAmount] = useState("");
  const [insurance_paid, setInsurancePaid] = useState("");
  const [patient_paid, setPatientPaid] = useState("");
  const [status, setStatus] = useState("");

  const [insuranceProviderDB, setInsuranceProviderDB] = useState([]);

  //Post data to database
  const handleSubmit = async (e) => {
    e.preventDefault();

    await axios
      .post("http://127.0.0.1:8000/insurance_claim", {
        patient_id,
        provider_id,
        date_of_service,
        procedure_code,
        diagnosis_code,
        billed_amount,
        insurance_paid,
        patient_paid,
        status,
      })
      .then((res) => {
        window.location.reload(true);
        console.log("Posting data to database successful!!!", res);
      })
      .catch((err) => console.log(err));
  };

  //Fetch insurance providers
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/insurance_provider")
      .then((res) => {
        console.log(
          "Fetching insurance provider from database successful!!!",
          res.data
        );
        setInsuranceProviderDB(res.data);
      })
      .catch((err) => console.log(err));
  }, []);

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Insurance Claim Form
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Fill out the form to make an insurance claim.
        </Typography>
        <form onSubmit={handleSubmit} className="admission_form">
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Patient ID"
                placeholder="Enter Patient ID"
                variant="outlined"
                type="text"
                value={patient_id}
                onChange={(event) => {
                  setPatientID(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                id="provider_id"
                select
                label="Select Insurance Provider"
                value={provider_id}
                //defaultValue="In-person"
                //helperText="Please select appointment type"
                onChange={(event) => {
                  setProviderID(event.target.value);
                }}
                fullWidth
              >
                {insuranceProviderDB.map((item) => (
                  <MenuItem key={item.id} value={item.name}>
                    {item.name}
                  </MenuItem>
                ))}
              </TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                //label="Date of Service"
                helperText="Enter Date of Service"
                variant="outlined"
                type="date"
                value={date_of_service}
                onChange={(event) => {
                  setDateOfService(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Procedure Code"
                placeholder="Enter Procedure Code"
                variant="outlined"
                type="text"
                value={procedure_code}
                onChange={(event) => {
                  setProcedureCode(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Diagnosis Code"
                placeholder="Enter Diagnosis Code"
                variant="outlined"
                type="text"
                value={diagnosis_code}
                onChange={(event) => {
                  setDiagnosisCode(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Billed Amount"
                placeholder="Enter Billed Amount"
                variant="outlined"
                type="number"
                value={billed_amount}
                onChange={(event) => {
                  setBilledAmount(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Insurance Paid"
                placeholder="Enter Insurance Paid"
                variant="outlined"
                type="text"
                value={insurance_paid}
                onChange={(event) => {
                  setInsurancePaid(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Patient Paid"
                placeholder="Enter Patient Paid"
                variant="outlined"
                type="text"
                value={patient_paid}
                onChange={(event) => {
                  setPatientPaid(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Status"
                placeholder="Enter Status"
                variant="outlined"
                type="text"
                value={status}
                onChange={(event) => {
                  setStatus(event.target.value);
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
    </div>
  );
};

export default InsuranceClaimForm;
