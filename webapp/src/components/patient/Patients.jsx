import React from "react";
import { useState, useEffect } from "react";

function Patients() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/patient")
      .then((response) => response.json())
      .then((data) => setData(data));
  }, []);

  return (
    <table>
      <thead>
        <tr>
          <th>First Name</th>
          <th>Last Name</th>
          <th>Date of Birth</th>
          <th>Gender</th>
          <th>Phone Number</th>
          <th>Email</th>
          <th>Address</th>
          <th>City</th>
          <th>State</th>
          <th>Zip Code</th>
          <th>Country</th>
          <th>Emergency Contact Name</th>
          <th>Emergency Contact Number</th>
          <th>Relationship</th>
          <th>Insured</th>
          <th>Provider Name</th>
          <th>Policy Number</th>
          <th>Group Number</th>
          <th>Effective Date</th>
          <th>Expiration Date</th>
        </tr>
      </thead>
      <tbody>
        {data.map((item) => (
          <tr key={item.id}>
            <td>{item.firstname}</td>
            <td>{item.lastname}</td>
            <td>{item.dob}</td>
            <td>{item.gender}</td>
            <td>{item.phonenumber}</td>
            <td>{item.email}</td>
            <td>{item.address}</td>
            <td>{item.city}</td>
            <td>{item.state}</td>
            <td>{item.zip_code}</td>
            <td>{item.country}</td>
            <td>{item.emergency_contact_name}</td>
            <td>{item.emergency_contact_phone}</td>
            <td>{item.relationship}</td>
            <td>{item.insurance}</td>
            <td>{item.provider_name}</td>
            <td>{item.policy_number}</td>
            <td>{item.group_number}</td>
            <td>{item.effective_date}</td>
            <td>{item.expiration_date}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default Patients;
