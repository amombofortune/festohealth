import React, { createContext, useState } from "react";

const DoctorAvailabilityContext = createContext();

const DoctorAvailabilityProvider = ({ children }) => {
  const [unavailableTimeSlots, setUnavailableTimeSlots] = useState([]);

  return (
    <DoctorAvailabilityContext.Provider
      value={{ unavailableTimeSlots, setUnavailableTimeSlots }}
    >
      {children}
    </DoctorAvailabilityContext.Provider>
  );
};

export { DoctorAvailabilityContext, DoctorAvailabilityProvider };
