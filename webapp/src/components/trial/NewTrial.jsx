import React, { useState, useEffect } from "react";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import Paper from "@mui/material/Paper";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import TablePagination from "@mui/material/TablePagination";
import TableSortLabel from "@mui/material/TableSortLabel";
import { BsFillTrashFill, BsFillPencilFill } from "react-icons/bs";
import axios from "axios";
import "./Vaccination.scss";
import Button from "@mui/material/Button";
import Modal from "@mui/material/Modal";
import Box from "@mui/material/Box";
import { TextField } from "@mui/material";
import VaccinationForm from "./VaccinationForm";

function NewTrial() {
  const [patient_id, setPatientID] = useState("");
  const [vaccine_name, setVaccineName] = useState("");
  const [administered_by, setAdministeredBy] = useState("");
  const [administered_at, setAdministeredAt] = useState("");
  const [next_dose_due, setNextDoseDue] = useState("");

  const [data, setData] = useState([]);

  //Modal
  const [open, setOpen] = React.useState(false);
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);

  //editing columns
  const [editID, setEditID] = useState(-1);
  //Fetching using search
  const [searchQuery, setSearchQuery] = useState("");
  const filteredData = data.filter(
    (item) =>
      item.patient_id
        .toString()
        .toLowerCase()
        .includes(searchQuery.toLowerCase()) ||
      item.vaccine_name
        .toString()
        .toLowerCase()
        .includes(searchQuery.toLowerCase()) ||
      item.administered_by
        .toString()
        .toLowerCase()
        .includes(searchQuery.toLowerCase()) ||
      item.administered_at
        .toString()
        .toLowerCase()
        .includes(searchQuery.toLowerCase()) ||
      item.next_dose_due
        .toString()
        .toLowerCase()
        .includes(searchQuery.toLowerCase())
  );

  //pagination
  const [page, setPage] = React.useState(0);
  const [rowsPerPage, setRowsPerPage] = React.useState(10);
  const [count, setCount] = useState(0);
  const handleChangePage = (event, newPage) => {
    setPage(newPage);
  };
  const handleChangeRowsPerPage = (event) => {
    setRowsPerPage(parseInt(event.target.value, 10));
    setPage(0);
  };
  const updateCount = (data) => {
    setCount(data.length);
  };
  // Get a subset of the data based on the current page and rows per page settings
  const slicedData = filteredData.slice(
    page * rowsPerPage,
    page * rowsPerPage + rowsPerPage
  );

  //sorting columns
  const [sortDirection, setSortDirection] = useState("asc");
  const [sortColumn, setSortColumn] = useState("patient_id");

  const handleSort = (column) => {
    const isAsc = sortColumn === column && sortDirection === "asc";
    setSortDirection(isAsc ? "desc" : "asc");
    setSortColumn(column);
    setData((prevData) =>
      [...prevData].sort((a, b) => {
        if (isAsc) {
          return a[column] < b[column] ? -1 : 1;
        } else {
          return a[column] > b[column] ? -1 : 1;
        }
      })
    );
  };

  //Fetch prescriptions
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/vaccination")
      .then((res) => {
        console.log(
          "Fetching vaccination from database successful!!!",
          res.data
        );
        setData(res.data);
        updateCount(res.data);
      })
      .catch((err) => console.log(err));
  }, []);

  //Delete record
  const handleDelete = async (id, e) => {
    e.preventDefault();

    await axios
      .delete(`http://127.0.0.1:8000/vaccination/${id}`)
      .then((res) => {
        window.location.reload(true);
        console.log("Deleted!!", res);
      })
      .catch((err) => console.log(err));
  };
  //Edit record
  const handleEdit = async (id) => {
    try {
      const res = await axios.get(`http://127.0.0.1:8000/vaccination/${id}`);
      const data = res.data;

      setPatientID(data.patient_id);
      setVaccineName(data.vaccine_name);
      setAdministeredBy(data.administered_by);
      setAdministeredAt(data.administered_at);
      setNextDoseDue(data.next_dose_due);

      setEditID(id);
    } catch (err) {
      console.log(err);
    }
  };

  //Update record
  const handleUpdate = async () => {
    const appointmentData = {
      patient_id,
      vaccine_name,
      administered_by,
      administered_at,
      next_dose_due,
    };

    try {
      const res = await axios.put(
        `http://127.0.0.1:8000/vaccination/${editID}`,
        appointmentData
      );

      console.log("Updated!!", res);
      setEditID(-1);
      window.location.reload(true);
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <div>
      <div>
        <Modal open={open} onClose={handleClose}>
          <Box className="box">
            <VaccinationForm />
          </Box>
        </Modal>
      </div>
      <div>
        <div className="table-container">
          <div className="button-container">
            <div className="search-container">
              <input
                type="text"
                className="search-btn"
                placeholder="Search..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
              />
            </div>
            <div className="appointment-container">
              <Button
                className="add_appointment"
                variant="contained"
                onClick={handleOpen}
              >
                + Add Prescription
              </Button>
            </div>
          </div>
          <Paper sx={{ width: "100%", overflow: "hidden" }}>
            <TableContainer sx={{ maxHeight: 440 }}>
              <Table stickyHeader aria-label="sticky table">
                <TableHead>
                  <TableRow>
                    <TableCell>
                      <TableSortLabel
                        active={sortColumn === "id"}
                        direction={sortDirection}
                        onClick={() => handleSort("id")}
                        data="id"
                      >
                        ID
                      </TableSortLabel>
                    </TableCell>

                    <TableCell>
                      <TableSortLabel
                        active={sortColumn === "patient_id"}
                        direction={sortDirection}
                        onClick={() => handleSort("patient_id")}
                      >
                        Patient ID
                      </TableSortLabel>
                    </TableCell>
                    <TableCell>
                      <TableSortLabel
                        active={sortColumn === "vaccine_name"}
                        direction={sortDirection}
                        onClick={() => handleSort("vaccine_name")}
                      >
                        Vaccine Name
                      </TableSortLabel>
                    </TableCell>
                    <TableCell>
                      <TableSortLabel
                        active={sortColumn === "administered_by"}
                        direction={sortDirection}
                        onClick={() => handleSort("administered_by")}
                      >
                        Administered By
                      </TableSortLabel>
                    </TableCell>
                    <TableCell>
                      <TableSortLabel
                        active={sortColumn === "administered_at"}
                        direction={sortDirection}
                        onClick={() => handleSort("administered_at")}
                      >
                        Administered At
                      </TableSortLabel>
                    </TableCell>
                    <TableCell>
                      <TableSortLabel
                        active={sortColumn === "next_dose_due"}
                        direction={sortDirection}
                        onClick={() => handleSort("next_dose_due")}
                      >
                        Next Dose Due
                      </TableSortLabel>
                    </TableCell>
                    <TableCell>
                      <TableSortLabel>Action</TableSortLabel>
                    </TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {slicedData.map((item, index) =>
                    item.id === editID ? (
                      <TableRow>
                        <TableCell>{page * rowsPerPage + index + 1}</TableCell>

                        <TableCell>
                          <TextField
                            type="text"
                            id="patient_id"
                            placeholder="Enter Patient ID"
                            name="patient_id"
                            value={patient_id}
                            onChange={(event) => {
                              setPatientID(event.target.value);
                            }}
                          />
                          {item.patient_id}
                        </TableCell>
                        <TableCell>
                          <TextField
                            type="text"
                            id="docvaccine_nametor_id"
                            placeholder="Enter Vaccine Name"
                            name="vaccine_name"
                            value={vaccine_name}
                            onChange={(event) => {
                              setVaccineName(event.target.value);
                            }}
                          />
                          {item.vaccine_name}
                        </TableCell>
                        <TableCell>
                          <TextField
                            type="text"
                            id="administered_by"
                            placeholder="Enter Administered By"
                            name="administered_by"
                            value={administered_by}
                            onChange={(event) => {
                              setAdministeredBy(event.target.value);
                            }}
                          />
                          {item.administered_by}
                        </TableCell>
                        <TableCell>
                          <TextField
                            type="text"
                            id="administered_at"
                            name="administered_at"
                            value={administered_at}
                            onChange={(event) => {
                              setAdministeredAt(event.target.value);
                            }}
                          />
                          {item.administered_at}
                        </TableCell>
                        <TableCell>
                          <TextField
                            type="text"
                            id="next_dose_due"
                            name="next_dose_due"
                            value={next_dose_due}
                            onChange={(event) => {
                              setNextDoseDue(event.target.value);
                            }}
                          />
                          {item.next_dose_due}
                        </TableCell>
                        <TableCell>
                          <Button className="btn-update" onClick={handleUpdate}>
                            Update
                          </Button>{" "}
                        </TableCell>
                      </TableRow>
                    ) : (
                      <TableRow key={item.id}>
                        <TableCell>{page * rowsPerPage + index + 1}</TableCell>
                        <TableCell>{item.patient_id}</TableCell>
                        <TableCell>{item.vaccine_name}</TableCell>
                        <TableCell>{item.administered_by}</TableCell>
                        <TableCell>{item.administered_at}</TableCell>
                        <TableCell>{item.next_dose_due}</TableCell>
                        <TableCell>
                          <span className="actions">
                            <BsFillTrashFill
                              className="delete-btn"
                              onClick={(e) => handleDelete(item.id, e)}
                            />
                            <BsFillPencilFill
                              onClick={() => {
                                handleEdit(item.id);
                                setEditID(item.id);
                              }}
                            />
                          </span>
                        </TableCell>
                      </TableRow>
                    )
                  )}
                </TableBody>
              </Table>
            </TableContainer>
          </Paper>
          <TablePagination
            component="div"
            count={count}
            page={page}
            onPageChange={handleChangePage}
            rowsPerPage={rowsPerPage}
            onRowsPerPageChange={handleChangeRowsPerPage}
          />
        </div>
      </div>
    </div>
  );
}

export default NewTrial;
