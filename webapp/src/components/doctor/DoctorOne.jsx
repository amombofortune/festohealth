import React, { useEffect, useState } from "react";
import axios from "axios";
import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  TablePagination,
} from "@mui/material";
import SearchOutlinedIcon from "@mui/icons-material/SearchOutlined";
import "./doctorOne.scss";
import UserProfileCard from "./UserProfileCard";
import ArrowDropDownIcon from "@mui/icons-material/ArrowDropDown";
import ArrowDropUpIcon from "@mui/icons-material/ArrowDropUp";

const DoctorOne = () => {
  const [data, setData] = useState([]);
  const [page, setPage] = useState(0);
  const [rowsPerPage, setRowsPerPage] = useState(10);
  const [searchQuery, setSearchQuery] = useState("");
  const [sortColumn, setSortColumn] = useState("");
  const [sortDirection, setSortDirection] = useState("asc");

  const handleChangePage = (event, newPage) => {
    setPage(newPage);
  };

  const handleChangeRowsPerPage = (event) => {
    setRowsPerPage(parseInt(event.target.value, 10));
    setPage(0);
  };

  const handleSearch = (event) => {
    setSearchQuery(event.target.value);
  };

  //Fetch doctor
  useEffect(() => {
    const fetchData = async () => {
      try {
        const access_token = document.cookie.replace(
          /(?:(?:^|.*;\s*)access_token\s*=\s*([^;]*).*$)|^.*$/,
          "$1"
        );

        const response = await axios.get("http://127.0.0.1:8000/doctor", {
          withCredentials: true, // Enable sending cookies with the request
          headers: {
            Authorization: `Bearer ${access_token}`, // Include the access token as a request header
          },
        });

        console.log(
          "Fetching doctor from database successful!!!",
          response.data
        );
        setData(response.data);
      } catch (error) {
        console.error("Failed to fetch doctor data:", error);
        // Handle error fetching doctor data
      }
    };

    fetchData();
  }, []);

  // Filter the data based on the search query
  const filteredData = data.filter(
    (item) =>
      item.firstname.toLowerCase().includes(searchQuery.toLowerCase()) ||
      item.middlename.toLowerCase().includes(searchQuery.toLowerCase()) ||
      item.lastname.toLowerCase().includes(searchQuery.toLowerCase()) ||
      item.specialty.toLowerCase().includes(searchQuery.toLowerCase())
  );

  const handleSort = (column) => {
    if (sortColumn === column) {
      // If the same column is clicked, toggle the sort direction
      setSortDirection((prevSortDirection) =>
        prevSortDirection === "asc" ? "desc" : "asc"
      );
    } else {
      // If a different column is clicked, set it as the new sort column and set the default sort direction
      setSortColumn(column);
      setSortDirection("asc");
    }
  };

  const sortedData = filteredData.sort((a, b) => {
    // Compare the values based on the sort column
    if (sortColumn === "name") {
      const nameA = `${a.firstname} ${a.middlename} ${a.lastname}`;
      const nameB = `${b.firstname} ${b.middlename} ${b.lastname}`;
      return nameA.localeCompare(nameB);
    } else if (sortColumn === "specialty") {
      return a.specialty.localeCompare(b.specialty);
    } else if (sortColumn === "consultation_fee") {
      return a.consultation_fee - b.consultation_fee;
    } else if (sortColumn === "rating") {
      return a.rating - b.rating;
    } else if (sortColumn === "verified") {
      return a.verified - b.verified;
    }
    // Return 0 if the values are equal (maintains original order)
    return 0;
  });

  // Reverse the sorted data if the sort direction is descending
  const sortedAndDirectionalData =
    sortDirection === "desc" ? sortedData.reverse() : sortedData;

  const displayedData = sortedAndDirectionalData.slice(
    page * rowsPerPage,
    page * rowsPerPage + rowsPerPage
  );

  return (
    <div className="user-table-container">
      <div className="user-table">
        <div className="table-title">
          Doctors
          <div className="search">
            <input
              type="text"
              value={searchQuery}
              onChange={handleSearch}
              placeholder="Search..."
              style={{
                fontSize: "15px",
                lineHeight: "18px",
              }}
            />
            <SearchOutlinedIcon />
          </div>
        </div>
        <div className="wrapper-table">
          <div className="table-header-container">
            <TableContainer component={Paper}>
              <Table>
                <TableHead>
                  <TableRow>
                    <TableCell
                      onClick={() => handleSort("name")}
                      className="sticky-header"
                    >
                      Name{" "}
                      {sortColumn === "name" && sortDirection === "asc" ? (
                        <ArrowDropUpIcon />
                      ) : (
                        <ArrowDropDownIcon />
                      )}
                    </TableCell>
                    <TableCell
                      onClick={() => handleSort("specialty")}
                      className="sticky-header"
                    >
                      Specialty{" "}
                      {sortColumn === "specialty" && sortDirection === "asc" ? (
                        <ArrowDropUpIcon />
                      ) : (
                        <ArrowDropDownIcon />
                      )}
                    </TableCell>
                    <TableCell
                      onClick={() => handleSort("consultation_fee")}
                      className="sticky-header"
                    >
                      Consultation Fee{" "}
                      {sortColumn === "consultation_fee" &&
                      sortDirection === "asc" ? (
                        <ArrowDropUpIcon />
                      ) : (
                        <ArrowDropDownIcon />
                      )}
                    </TableCell>
                    <TableCell
                      onClick={() => handleSort("rating")}
                      className="sticky-header"
                    >
                      Rating{" "}
                      {sortColumn === "rating" && sortDirection === "asc" ? (
                        <ArrowDropUpIcon />
                      ) : (
                        <ArrowDropDownIcon />
                      )}
                    </TableCell>
                    <TableCell
                      onClick={() => handleSort("verified")}
                      className="sticky-header"
                    >
                      Verified{" "}
                      {sortColumn === "verified" && sortDirection === "asc" ? (
                        <ArrowDropUpIcon />
                      ) : (
                        <ArrowDropDownIcon />
                      )}
                    </TableCell>
                  </TableRow>
                </TableHead>
              </Table>
            </TableContainer>
          </div>
          <div>
            <TableContainer component={Paper}>
              <Table style={{ border: "none", marginTop: "10px" }}>
                <TableBody>
                  {displayedData.map((item) => (
                    <TableRow key={item.id} style={{ border: "none" }}>
                      <TableCell style={{ border: "none" }}>
                        <UserProfileCard item={item} />
                      </TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </TableContainer>
          </div>
        </div>

        <TablePagination
          rowsPerPageOptions={[5, 10, 25, 50, 100]}
          component="div"
          count={filteredData.length}
          rowsPerPage={rowsPerPage}
          page={page}
          onPageChange={handleChangePage}
          onRowsPerPageChange={handleChangeRowsPerPage}
        />
      </div>
    </div>
  );
};

export default DoctorOne;
