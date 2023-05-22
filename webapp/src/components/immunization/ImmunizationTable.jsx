import * as React from "react";
import Box from "@mui/material/Box";
import { DataGrid } from "@mui/x-data-grid";
import axios from "axios";
import { useState, useEffect } from "react";
import Modal from "@mui/material/Modal";
import "./immunizationTable.scss";
import SearchOutlinedIcon from "@mui/icons-material/SearchOutlined";
import { Button } from "@mui/material";

import ImmunizationForm from "../immunization/ImmunizationForm";
import ImmunizationEdit from "../immunization/ImmunizationEdit";
import ImmunizationView from "../immunization/ImmunizationView";

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

export default function ImmunizationTable() {
  const columns = [
    { field: "id", headerName: "ID", width: 90 },
    {
      field: "patient_id",
      headerName: "Patient ID",
      width: 100,
      editable: true,
    },
    {
      field: "vaccine_name",
      headerName: "Vaccine Name",
      width: 150,
      editable: true,
    },
    {
      field: "dose_number",
      headerName: "Dose Number",
      width: 150,
      editable: true,
    },
    {
      field: "date_given",
      headerName: "Date Given",
      width: 150,
      editable: true,
    },
    {
      field: "administering_provider",
      headerName: "Administering Provider",
      width: 150,
      editable: true,
    },
    {
      field: "expiration_date",
      headerName: "Expiration Date",
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

  //Fetch immunization
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/immunization")
      .then((res) => {
        console.log(
          "Fetching immunization from database successful!!!",
          res.data
        );
        setData(res.data);
      })
      .catch((err) => console.log(err));
  }, []);

  // Delete record
  const handleDelete = async (id, e) => {
    e.preventDefault();

    await axios
      .delete(`http://127.0.0.1:8000/immunization/${id}`)
      .then((res) => {
        setData((prevData) => prevData.filter((row) => row.id !== id));
        console.log("Deleted!!", res);
      })
      .catch((err) => console.log(err));
  };

  return (
    <div className="datatable">
      <div className="datatableTitle">
        Immunization
        <div className="search">
          <input
            type="text"
            placeholder="Search department table..."
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
            Add Immunization
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
              <ImmunizationForm />
            </Box>
          </Box>
        </Modal>
      </div>
      <div>
        {selectedRow && (
          <Modal open={openEditForm} onClose={handleCloseEditForm}>
            <Box style={modalStyle}>
              <Box sx={{ width: "100%" }}>
                <ImmunizationEdit selectedRow={selectedRow} />
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
                <ImmunizationView selectedRow={selectedRow} />
              </Box>
            </Box>
          </Modal>
        )}
      </div>
    </div>
  );
}
