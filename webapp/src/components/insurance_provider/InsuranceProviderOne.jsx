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
import "./insuranceProviderOne.scss";
import UserProfileCard from "./UserProfileCard";
import ArrowDropDownIcon from "@mui/icons-material/ArrowDropDown";
import ArrowDropUpIcon from "@mui/icons-material/ArrowDropUp";

const InsuranceProviderOne = () => {
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

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/insurance_provider")
      .then((res) => {
        console.log("Getting from database...", res.data);
        setData(res.data);
      })
      .catch((err) => console.log(err));
  }, []);

  // Filter the data based on the search query
  const filteredData = data.filter(
    (item) =>
      item.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
      item.licence_number.toLowerCase().includes(searchQuery.toLowerCase()) ||
      item.city.toLowerCase().includes(searchQuery.toLowerCase()) ||
      item.country.toLowerCase().includes(searchQuery.toLowerCase())
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
      return a.name.localeCompare(b.name);
    } else if (sortColumn === "city") {
      return a.city.localeCompare(b.city);
    } else if (sortColumn === "country") {
      return a.country - b.country;
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
          Insurance Providers
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
                      onClick={() => handleSort("city")}
                      className="sticky-header"
                    >
                      City{" "}
                      {sortColumn === "city" && sortDirection === "asc" ? (
                        <ArrowDropUpIcon />
                      ) : (
                        <ArrowDropDownIcon />
                      )}
                    </TableCell>
                    <TableCell
                      onClick={() => handleSort("country")}
                      className="sticky-header"
                    >
                      Country{" "}
                      {sortColumn === "country" && sortDirection === "asc" ? (
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

export default InsuranceProviderOne;
