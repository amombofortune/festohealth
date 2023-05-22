import React, { useState } from "react";
import Modal from "@mui/material/Modal";
import { Button } from "@mui/material";
import Box from "@mui/material/Box";
import AppointmentForm from "../appointment/AppointmentForm";
import VerifiedIcon from "@mui/icons-material/Verified";
import Rating from "@mui/material/Rating";
import "./trial.scss";

const modalStyle = {
  position: "fixed",
  top: "50%",
  left: "50%",
  transform: "translate(-50%, -50%)",
  backgroundColor: "white",
  border: "1px solid gray",
  borderRadius: "20px",
  padding: "10px",
  boxShadow: "0px 0px 5px gray",
  maxWidth: "95%",
  maxHeight: "95%",
  overflow: "auto",
  width: "1000px",
};

const UserProfileCard = ({ item }) => {
  const {
    firstname,
    middlename,
    lastname,
    gender,
    phone_number,
    email,
    specialty,
    city,
    country,
    consultation_fee,
    rating,
    verified,
  } = item;
  const [open, setOpen] = useState(false);
  const [openForm, setOpenForm] = useState(false);

  const handleOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  const handleOpenForm = () => {
    setOpenForm(true);
  };

  const handleCloseForm = () => {
    setOpenForm(false);
  };

  return (
    <div className="user-card">
      <div className="user-card-image">
        <img
          src="https://images.pexels.com/photos/941693/pexels-photo-941693.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500"
          alt="User Profile"
        />
      </div>
      <div className="user-card-details">
        <h4 style={{ display: "flex", alignItems: "center" }}>
          {`Dr. ${firstname} ${middlename} ${lastname}`}
          {verified && (
            <VerifiedIcon
              style={{ color: "blue", fontSize: "1.1em", marginLeft: "0.2em" }}
            />
          )}
        </h4>
        <p>{specialty}</p>
        <p style={{ color: "green", fontWeight: "bold" }}>
          Ksh {consultation_fee}
        </p>
        <Rating name="read-only" value={rating} size="small" readOnly />
      </div>
      <div className="button-group">
        <button className="view-button" onClick={handleOpen}>
          View
        </button>
        <button className="schedule-button" onClick={handleOpenForm}>
          Book Appointment
        </button>
      </div>
      <div>
        <Modal open={open} onClose={handleClose}>
          <Box style={modalStyle}>
            <Box
              sx={{
                display: "flex",
                justifyContent: "space-between",
                alignItems: "center",
              }}
            >
              <h2>Doctor Profile</h2>
              <Button variant="contained" onClick={handleClose}>
                Close
              </Button>
            </Box>
            <Box sx={{ width: "100%" }}>
              <p>Name: {`${firstname} ${middlename} ${lastname}`}</p>
              <p>Gender: {gender}</p>
              <p>Contact Number: {phone_number}</p>
              <p>Email: {email}</p>
              <p>Specialty: {specialty}</p>
              <p>Location: {city + ", " + country}</p>
            </Box>
          </Box>
        </Modal>
      </div>
      <div>
        <Modal open={openForm} onClose={handleCloseForm}>
          <Box style={modalStyle}>
            <Box sx={{ display: "flex", justifyContent: "flex-end" }}>
              <Button variant="contained" onClick={handleCloseForm}>
                Close
              </Button>
            </Box>
            <Box sx={{ width: "100%" }}>
              <AppointmentForm />
            </Box>
          </Box>
        </Modal>
      </div>
    </div>
  );
};

export default UserProfileCard;
