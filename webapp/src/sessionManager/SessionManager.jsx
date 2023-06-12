import React, { useEffect, useState } from "react";

const SessionManager = ({ children }) => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  // Function to handle user logout
  const logout = () => {
    // Your logout logic here
    console.log("Logging out due to inactivity");
    setIsLoggedIn(false);
  };

  useEffect(() => {
    let timeoutId;

    const resetTimer = () => {
      clearTimeout(timeoutId);
      timeoutId = setTimeout(logout, 300000); // 5 minutes (300,000 milliseconds)
    };

    const events = [
      "load",
      "mousemove",
      "mousedown",
      "click",
      "scroll",
      "keypress",
    ];

    const addEventListeners = () => {
      events.forEach((event) => {
        window.addEventListener(event, resetTimer);
      });
    };

    const removeEventListeners = () => {
      events.forEach((event) => {
        window.removeEventListener(event, resetTimer);
      });
    };

    if (isLoggedIn) {
      resetTimer();
      addEventListeners();
    } else {
      clearTimeout(timeoutId);
      removeEventListeners();
    }

    return () => {
      clearTimeout(timeoutId);
      removeEventListeners();
    };
  }, [isLoggedIn]);

  return <>{children}</>;
};

export default SessionManager;
