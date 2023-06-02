import * as React from "react";
import Box from "@mui/material/Box";
import { DataGrid } from "@mui/x-data-grid";
import axios from "axios";
import { useState, useEffect } from "react";
import Modal from "@mui/material/Modal";
import "./vitalSignTable.scss";
import SearchOutlinedIcon from "@mui/icons-material/SearchOutlined";
import { Button } from "@mui/material";

import VitalSignForm from "../vital_sign/VitalSignForm";
import VitalSignEdit from "../vital_sign/VitalSignEdit";
import VitalSignView from "../vital_sign/VitalSignView";

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

export default function VitalSignTable() {
  const columns = [
    { field: "id", headerName: "ID", width: 90 },
    {
      field: "patient_id",
      headerName: "Patient ID",
      width: 100,
      editable: true,
    },
    {
      field: "doctor_id",
      headerName: "Doctor ID",
      width: 150,
      editable: true,
    },
    {
      field: "heart_rate",
      headerName: "Heart Rate",
      width: 160,
      editable: true,
    },
    {
      field: "blood_pressure_systolic",
      headerName: "Blood Pressure Systolic",
      width: 150,
      editable: true,
    },
    {
      field: "blood_pressure_diastolic",
      headerName: "Blood Pressure Dyastolic",
      width: 150,
      editable: true,
    },
    {
      field: "respiratory_rate",
      headerName: "Respiratory Rate",
      width: 150,
      editable: true,
    },
    {
      field: "temperature",
      headerName: "Temperature",
      width: 150,
      editable: true,
    },
    {
      field: "height",
      headerName: "Height",
      width: 150,
      editable: true,
    },
    {
      field: "weight",
      headerName: "Weight",
      width: 150,
      editable: true,
    },
    {
      field: "oxygen_saturation",
      headerName: "Oxygen Saturation",
      width: 150,
      editable: true,
    },
    {
      field: "recorded_at",
      headerName: "Recorded At",
      width: 150,
      editable: true,
    },

    {
      field: "actions",
      headerName: "Actions",
      width: 250,
      renderCell: (params) => {
        return (
          <div className="cellAction">
            <div>
              <Button
                size="small"
                onClick={() => handleViewClick(params)}
                className="viewButton"
              >
                View
              </Button>
            </div>
            <Button
              size="small"
              className="editButton"
              onClick={() => handleEditClick(params)}
            >
              Edit
            </Button>
            <Button
              size="small"
              className="deleteButton"
              onClick={(e) => handleDelete(params.row.id, e)}
            >
              Delete
            </Button>
          </div>
        );
      },
    },
  ];

  const [data, setData] = useState([]);
  const [selectedRow, setSelectedRow] = useState(null);
  const [searchTerm, setSearchTerm] = useState("");
  //Modal
  const [openEditForm, setOpenEditForm] = useState(false);
  const [openViewForm, setOpenViewForm] = useState(false);
  const [openAddForm, setOpenAddForm] = useState(false);

  const handleCloseEditForm = () => {
    console.log("Closing modal...");
    setSelectedRow(null);
    setOpenEditForm(false);
  };
  const handleCloseViewForm = () => {
    console.log("Closing modal...");
    setSelectedRow(null);
    setOpenViewForm(false);
  };
  const handleCloseAddForm = () => {
    console.log("Closing modal...");
    setSelectedRow(null);
    setOpenAddForm(false);
  };
  //Opens schedule appointment

  const handleOpenAddForm = () => {
    setOpenAddForm(true);
  };

  //Opens Edit Modal
  const handleEditClick = (params) => {
    console.log("Opening modal...", params.row);
    setSelectedRow(params.row);
    setOpenEditForm(true);
  };

  const handleViewClick = (params) => {
    console.log("Opening modal...", params.row);
    setSelectedRow(params.row);
    setOpenViewForm(true);
  };

  //Edits and updates selected row
  const handleRowSelected = (currentSelection) => {
    if (currentSelection.length > 0) {
      setSelectedRow(data.find((row) => row.id === currentSelection[0]));
      setOpenEditForm(true);
      setOpenViewForm(true);
    } else {
      setSelectedRow(null);
      setOpenEditForm(false);
      setOpenViewForm(false);
    }
  };

  const filteredData = data.filter((row) =>
    Object.values(row).some(
      (cellValue) =>
        cellValue &&
        cellValue.toString().toLowerCase().includes(searchTerm.toLowerCase())
    )
  );

  //Fetch vital sign
  useEffect(() => {
    const fetchData = async () => {
      try {
        const access_token = document.cookie.replace(
          /(?:(?:^|.*;\s*)access_token\s*=\s*([^;]*).*$)|^.*$/,
          "$1"
        );

        const response = await axios.get("http://127.0.0.1:8000/vital_sign", {
          withCredentials: true, // Enable sending cookies with the request
          headers: {
            Authorization: `Bearer ${access_token}`, // Include the access token as a request header
          },
        });

        console.log(
          "Fetching vital sign from database successful!!!",
          response.data
        );
        setData(response.data);
      } catch (error) {
        console.error("Failed to fetch vital sign data:", error);
        // Handle error fetching vital sign data
      }
    };

    fetchData();
  }, []);

  // Delete record
  const handleDelete = async (id, e) => {
    e.preventDefault();

    await axios
      .delete(`http://127.0.0.1:8000/vital_sign/${id}`)
      .then((res) => {
        setData((prevData) => prevData.filter((row) => row.id !== id));
        console.log("Deleted!!", res);
      })
      .catch((err) => console.log(err));
  };

  return (
    <div className="datatable">
      <div className="datatableTitle">
        Vital Signs
        <div className="search">
          <input
            type="text"
            placeholder="Search patient visit table..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            style={{
              fontSize: "15px",
              lineHeight: "18px",
            }}
          />{" "}
          <SearchOutlinedIcon />
        </div>
        <div>
          <button onClick={handleOpenAddForm} className="appointmentLink">
            Add Vital Sign
          </button>
        </div>
      </div>
      <div className="datagridContainer">
        <Box sx={{ height: 400, width: "100%" }}>
          <DataGrid
            className="datagrid"
            rows={filteredData}
            columns={columns}
            initialState={{
              ...data.initialState,
              pagination: { paginationModel: { pageSize: 10 } },
            }}
            pageSizeOptions={[10, 25, 50, 100]}
            checkboxSelection
            onSelectionModelChange={handleRowSelected}
          />
        </Box>
      </div>
      <div>
        <Modal open={openAddForm} onClose={handleCloseAddForm}>
          <Box style={modalStyle}>
            <Box sx={{ width: "100%" }}>
              <VitalSignForm />
            </Box>
          </Box>
        </Modal>
      </div>
      <div>
        {selectedRow && (
          <Modal open={openEditForm} onClose={handleCloseEditForm}>
            <Box style={modalStyle}>
              <Box sx={{ width: "100%" }}>
                <VitalSignEdit selectedRow={selectedRow} />
              </Box>
            </Box>
          </Modal>
        )}
      </div>
      <div>
        {selectedRow && (
          <Modal open={openViewForm} onClose={handleCloseViewForm}>
            <Box style={modalStyle}>
              <Box sx={{ width: "100%" }}>
                <VitalSignView selectedRow={selectedRow} />
              </Box>
            </Box>
          </Modal>
        )}
      </div>
    </div>
  );
}
