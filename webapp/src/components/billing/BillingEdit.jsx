import {
  Button,
  CardContent,
  Grid,
  TextField,
  Typography,
} from "@mui/material";
import React, { useState } from "react";
import axios from "axios";

import "./billing.scss";

const BillingEdit = ({ selectedRow }) => {
  const { patient_id, bill_date, amount_due, amount_paid, payment_method } =
    selectedRow;

  const [patientID, setPatientID] = useState(patient_id);
  const [billDate, setBillDate] = useState(bill_date);
  const [amountDue, setAmountDue] = useState(amount_due);
  const [amountPaid, setAmountPaid] = useState(amount_paid);
  const [paymentMethod, setPaymentMethod] = useState(payment_method);

  //Update record
  const handleUpdate = async () => {
    const appointmentData = {
      patient_id: patientID,
      bill_date: billDate,
      amount_due: amountDue,
      amount_paid: amountPaid,
      payment_method: paymentMethod,
    };

    try {
      const res = await axios.put(
        `http://127.0.0.1:8000/billing/${selectedRow.id}`,
        appointmentData
      );
      console.log("Updated!!", res);
      window.location.reload(true);
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Are you sure you want to update bill?
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Edit out this form and we will update your appointment.
        </Typography>
        <form onSubmit={handleUpdate} style={{ marginTop: "10px" }}>
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Patient ID"
                placeholder="Enter Patient ID"
                variant="outlined"
                type="number"
                value={patientID}
                onChange={(event) => {
                  setPatientID(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                //label="Doctor ID"
                helperText="Enter Bill Date"
                variant="outlined"
                type="date"
                value={billDate}
                onChange={(event) => {
                  setBillDate(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                label="Amount Due"
                placeholder="Enter Amount Due"
                variant="outlined"
                type="number"
                value={amountDue}
                onChange={(event) => {
                  setAmountDue(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Amount Paid"
                helperText="Enter Amount Paid"
                variant="outlined"
                type="number"
                value={amountPaid}
                onChange={(event) => {
                  setAmountPaid(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} item>
              <TextField
                label="Payment Method"
                placeholder="Enter Payment Method"
                variant="outlined"
                type="text"
                value={paymentMethod}
                onChange={(event) => {
                  setPaymentMethod(event.target.value);
                }}
                multiline
                rows={4}
                fullWidth
              ></TextField>
            </Grid>

            <Grid xs={12} item>
              <Button
                type="submit"
                variant="contained"
                color="primary"
                style={{ backgroundColor: "#6439ff" }}
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

export default BillingEdit;
