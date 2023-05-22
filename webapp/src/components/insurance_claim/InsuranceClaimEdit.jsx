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

const InsuranceClaimEdit = ({ selectedRow }) => {
  const {
    patient_id,
    provider_id,
    date_of_service,
    procedure_code,
    diagnosis_code,
    billed_amount,
    insurance_paid,
    patient_paid,
    status,
  } = selectedRow;

  const [patientID, setPatientID] = useState(patient_id);
  const [providerID, setProviderID] = useState(provider_id);
  const [dateOfService, setDateOfService] = useState(date_of_service);
  const [procedureCode, setProcedureCode] = useState(procedure_code);
  const [diagnosisCode, setDiagnosisCode] = useState(diagnosis_code);
  const [billedAmount, setBilledAmount] = useState(billed_amount);
  const [insurancePaid, setInsurancePaid] = useState(insurance_paid);
  const [patientPaid, setPatientPaid] = useState(patient_paid);
  const [statusValue, setStatus] = useState(status);

  const [insuranceProviderDB, setInsuranceProviderDB] = useState([]);

  //Update record
  const handleUpdate = async () => {
    const appointmentData = {
      patient_id: patientID,
      provider_id: providerID,
      date_of_service: dateOfService,
      procedure_code: procedureCode,
      diagnosis_code: diagnosisCode,
      billed_amount: billedAmount,
      insurance_paid: insurancePaid,
      patient_paid: patientPaid,
      status: statusValue,
    };

    try {
      const res = await axios.put(
        `http://127.0.0.1:8000/insurance_claim/${selectedRow.id}`,
        appointmentData
      );
      console.log("Updated!!", res);
      window.location.reload(true);
    } catch (err) {
      console.log(err);
    }
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
          Are you sure you want to update insurance claim?
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Edit out this form and we will update insurance claim.
        </Typography>
        <form onSubmit={handleUpdate} style={{ marginTop: "10px" }}>
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Patient ID"
                placeholder="Enter Patient ID"
                variant="outlined"
                type="text"
                value={patientID}
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
                value={providerID}
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
                value={dateOfService}
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
                value={procedureCode}
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
                value={diagnosisCode}
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
                value={billedAmount}
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
                value={insurancePaid}
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
                value={patientPaid}
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
                value={statusValue}
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
                Update
              </Button>
            </Grid>
          </Grid>
        </form>
      </CardContent>
    </div>
  );
};

export default InsuranceClaimEdit;
