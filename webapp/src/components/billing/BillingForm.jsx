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

const BillingForm = () => {
  const [patient_id, setPatientID] = useState("");
  const [bill_date, setBillDate] = useState("");
  const [amount_due, setAmountDue] = useState("");
  const [amount_paid, setAmountPaid] = useState("");
  const [payment_method, setPaymentMethod] = useState("");

  //Post data to database
  const handleSubmit = async (e) => {
    e.preventDefault();

    await axios
      .post("http://127.0.0.1:8000/billing", {
        patient_id,
        bill_date,
        amount_due,
        amount_paid,
        payment_method,
      })
      .then((res) => {
        window.location.reload(true);
        console.log("Posting data to database successful!!!", res);
      })
      .catch((err) => console.log(err));
  };

  return (
    <div>
      <CardContent>
        <Typography gutterBottom variant="h5">
          Billing Form
        </Typography>
        <Typography
          gutterBottom
          color="textSecondary"
          variant="body2"
          component="p"
        >
          Fill out the form to add a bill.
        </Typography>
        <form onSubmit={handleSubmit} className="admission_form">
          <Grid container spacing={1}>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Patient ID"
                placeholder="Enter Patient ID"
                variant="outlined"
                type="number"
                value={patient_id}
                onChange={(event) => {
                  setPatientID(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                //label="Bill Date"
                helperText="Enter Bill Date"
                variant="outlined"
                type="date"
                value={bill_date}
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
                value={amount_due}
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
                placeholder="Amount Paid"
                variant="outlined"
                type="number"
                value={amount_paid}
                onChange={(event) => {
                  setAmountPaid(event.target.value);
                }}
                fullWidth
                required
              ></TextField>
            </Grid>
            <Grid xs={12} sm={6} item>
              <TextField
                label="Payment Method"
                placeholder="Payment Method"
                variant="outlined"
                type="text"
                value={payment_method}
                onChange={(event) => {
                  setPaymentMethod(event.target.value);
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

export default BillingForm;
