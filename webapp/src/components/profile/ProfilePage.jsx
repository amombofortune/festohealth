import React, { useState, useContext } from "react";
import { Dialog, DialogContent, DialogTitle, Button } from "@mui/material";
import AvatarEditor from "react-avatar-edit";
import axios from "axios";
import UserContext from "../../contexts/UserContext";

const ProfilePage = () => {
  const [file, setFile] = useState("");
  const [dialogOpen, setDialogOpen] = useState(false);
  const [newImage, setNewImage] = useState(null);
  const [editorKey, setEditorKey] = useState(Date.now());

  const { userData } = useContext(UserContext);

  // Access user data
  const { access_token, user_id, email, user_type } = userData;

  const handleImageClick = () => {
    setDialogOpen(true);
  };

  const handleDialogClose = () => {
    setDialogOpen(false);
  };

  const handleFileUpload = (e) => {
    setFile(e.target.files[0]);
    setDialogOpen(false); // Close the dialog after selecting the image
  };

  const handleImageCrop = (preview) => {
    setNewImage(preview);
  };

  const handleSaveImage = async () => {
    if (newImage) {
      const dataURLtoBlob = (dataURL) => {
        const arr = dataURL.split(",");
        const mime = arr[0].match(/:(.*?);/)[1];
        const bstr = atob(arr[1]);
        let n = bstr.length;
        const u8arr = new Uint8Array(n);
        while (n--) {
          u8arr[n] = bstr.charCodeAt(n);
        }
        return new Blob([u8arr], { type: mime });
      };

      const blob = dataURLtoBlob(newImage); // Convert the dataURL to Blob
      setFile(blob); // Update the current file state with the new image

      const formData = new FormData();
      formData.append("image", blob);

      try {
        // Send the image data to the server for uploading
        await axios.post(`/${user_id}/profile_image`, formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        });

        console.log("Image uploaded successfully");
        // Handle success, e.g., show a success message to the user
      } catch (error) {
        console.error("Image upload failed:", error);
        // Handle error, e.g., display an error message to the user
      }
    }

    setDialogOpen(false); // Close the dialog after saving
  };

  const handleRemoveImage = () => {
    setFile(""); // Remove the current image by resetting the file state
    setNewImage(null); // Remove the image in the dialog by resetting the newImage state
    setEditorKey(Date.now());
    setDialogOpen(true); // Open the dialog for uploading a new image
  };

  return (
    <div className="new">
      <div className="newContainer">
        <div className="top"></div>
        <div className="bottom">
          <div className="left">
            <img
              src={
                file
                  ? URL.createObjectURL(file)
                  : "https://icon-library.com/images/no-image-icon/no-image-icon-0.jpg"
              }
              alt=""
              onClick={handleImageClick}
            />
          </div>
          <div className="right">
            <form>
              {/* Rest of the form inputs */}
              <div className="formInput">
                <label>User ID</label>
                <input type="text" value={user_id} disabled />
              </div>
              <div className="formInput">
                <label>Email</label>
                <input type="text" value={email} disabled />
              </div>
              <div className="formInput">
                <label>User Type</label>
                <input type="text" value={user_type} disabled />
              </div>
              <div className="formInput">
                <label>Access Token</label>
                <input type="text" value={access_token} disabled />
              </div>

              <button>Save</button>
            </form>
          </div>
        </div>
      </div>

      {/* Dialog for image upload */}
      <Dialog
        open={dialogOpen}
        onClose={handleDialogClose}
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          height: "100vh",
        }}
      >
        <DialogTitle>Upload Image</DialogTitle>
        <DialogContent
          style={{
            width: "400px",
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
          }}
        >
          <AvatarEditor
            width={200}
            height={200}
            key={editorKey}
            onCrop={handleImageCrop}
            onClose={handleDialogClose}
            src={file ? URL.createObjectURL(file) : ""}
            style={{
              borderRadius: "50%",
              objectFit: "cover",
              width: "100%",
              height: "100%",
            }}
          />
          <input
            type="file"
            id="file"
            onChange={handleFileUpload}
            style={{ display: "none" }}
          />
          <div
            style={{
              display: "flex",
              justifyContent: "center",
              marginTop: "10px",
            }}
          >
            <Button onClick={handleDialogClose}>Cancel</Button>
            <Button onClick={handleSaveImage}>Save</Button>
          </div>
          {file && <Button onClick={handleRemoveImage}>Remove Image</Button>}
        </DialogContent>
      </Dialog>
    </div>
  );
};

export default ProfilePage;
