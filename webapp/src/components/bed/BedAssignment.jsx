import React from "react";
import { useState } from "react";

function BedAssignment() {
  const [bed_id, setBedID] = useState("");
  const [patient_id, setPatientID] = useState("");
  const [assigned_by, setAssignedBy] = useState("");
  const [assigned_at, setAssignedAt] = useState("");
  const [discharged_at, setDischargedAt] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();

    const newBedAssignment = {
      bed_id,
      patient_id,
      assigned_by,
      assigned_at,
      discharged_at,
    };

    fetch("http://127.0.0.1:8000/bed_assignment", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(newBedAssignment),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => {
        console.log("User registration successful:", data);
        // do something with successful response
      })
      .catch((error) => {
        console.error("Error during user registration:", error);
        // do something with error
      });
  };

  return (
    <section className="container">
      <form onSubmit={handleSubmit} className="form">
        <header>Bed Assignment</header>
        <div className="input-box">
          <label>Bed ID: </label>
          <input
            type="number"
            value={bed_id}
            onChange={(event) => {
              setBedID(event.target.value);
            }}
          ></input>
        </div>
        <div className="input-box">
          <label>Patient ID: </label>
          <input
            type="number"
            value={patient_id}
            onChange={(event) => {
              setPatientID(event.target.value);
            }}
          ></input>
        </div>
        <div className="input-box">
          <label>Assigned By: </label>
          <input
            type="number"
            value={assigned_by}
            onChange={(event) => {
              setAssignedBy(event.target.value);
            }}
          ></input>
        </div>
        <div className="input-box">
          <label>Assigned At: </label>
          <input
            type="datetime-local"
            value={assigned_at}
            onChange={(event) => {
              setAssignedAt(event.target.value);
            }}
          ></input>
        </div>
        <div className="input-box">
          <label>Discharged At: </label>
          <input
            type="datetime-local"
            value={discharged_at}
            onChange={(event) => {
              setDischargedAt(event.target.value);
            }}
          ></input>
        </div>

        <button type="submit">Assign Bed</button>
      </form>
    </section>
  );
}

export default BedAssignment;
