import React from "react";
import { useState } from "react";

function User() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [user_type, setUserType] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();

    const newUser = {
      username,
      password,
      user_type,
    };

    fetch("http://127.0.0.1:8000/user_account", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(newUser),
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
    <form onSubmit={handleSubmit}>
      <div className="Appointment">
        <div className="information">
          <label>Username: </label>
          <input
            type="text"
            value={username}
            onChange={(event) => {
              setUsername(event.target.value);
            }}
          ></input>
          <label>Password: </label>
          <input
            type="text"
            value={password}
            onChange={(event) => {
              setPassword(event.target.value);
            }}
          ></input>
          <label>User Type: </label>
          <input
            type="text"
            value={user_type}
            onChange={(event) => {
              setUserType(event.target.value);
            }}
          ></input>

          <button type="submit">User</button>
        </div>
      </div>
    </form>
  );
}

export default User;
