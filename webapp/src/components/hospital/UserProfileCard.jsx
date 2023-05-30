import React, { useState } from "react";
import Modal from "@mui/material/Modal";
import { Button, Card } from "@mui/material";
import Box from "@mui/material/Box";
import AppointmentForm from "../appointment/AppointmentForm";
import VerifiedIcon from "@mui/icons-material/Verified";
import Rating from "@mui/material/Rating";
import "./hospitalOne.scss";

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
  width: "900px",
};

const viewModalStyle = {
  position: "fixed",
  top: "50%",
  left: "50%",
  transform: "translate(-50%, -50%)",
  backgroundColor: "white",
  border: "1px solid gray",
  borderRadius: "20px",
  padding: "10px",
  boxShadow: "0px 0px 5px gray",
  maxWidth: "100%",
  maxHeight: "100%",
  overflow: "auto",
  width: "600px",
};

const UserProfileCard = ({ item }) => {
  const {
    name,
    address,
    city,
    state,
    postal_code,
    country,
    email,
    phone_number,
    website,
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
          {name}
          {verified && (
            <VerifiedIcon
              style={{ color: "blue", fontSize: "1.1em", marginLeft: "0.2em" }}
            />
          )}
        </h4>
        <p>{phone_number}</p>
        <p>{website}</p>
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
      <div className="user-modal">
        <Modal open={open} onClose={handleClose}>
          <Card style={viewModalStyle}>
            <div className="user-modal-container">
              <h2 style={{ fontSize: "25px", color: "gray" }}>
                Hospital Profile
              </h2>
              <Button
                variant="outlined"
                size="small"
                onClick={handleClose}
                style={{ color: "#6439ff" }}
              >
                Close
              </Button>
            </div>
            <div className="information-container">
              <div className="image-container">
                <div>
                  <div className="image-container-wrapper">
                    <img
                      src="https://images.pexels.com/photos/941693/pexels-photo-941693.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500"
                      alt="User Profile"
                      className="profile-img"
                    />
                  </div>
                </div>
                <div className="name-specialty-container">
                  <div>
                    <p
                      style={{
                        color: "gray",
                        fontWeight: "bold",
                        marginBottom: "5px",
                      }}
                    >
                      {name}
                    </p>
                    <p
                      style={{
                        color: "#6439ff",
                      }}
                    >
                      {phone_number}
                    </p>
                  </div>
                </div>
                <div className="user-info">
                  <div>
                    <h3 style={{ fontSize: "16px" }}>Hospital Information</h3>
                    <p className="text">Email: {email}</p>
                    <p className="text">Phone Number: {phone_number}</p>
                    <p className="text">Website: {website}</p>
                    <p className="text">
                      Location:{" "}
                      {address +
                        ", " +
                        city +
                        ", " +
                        state +
                        ", " +
                        postal_code +
                        ", " +
                        country}
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </Card>
        </Modal>
      </div>
      <div>
        <Modal open={openForm} onClose={handleCloseForm}>
          <Box style={modalStyle} className="scrollbar-style">
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
