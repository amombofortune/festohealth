import axios from "axios";
import { toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

const axiosInstance = axios.create({
  baseURL: "http://127.0.0.1:8000", // Replace with your API base URL
});

axiosInstance.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response && error.response.status === 401) {
      // Handle expired token error
      handleExpiredToken();
    }
    return Promise.reject(error);
  }
);

function handleExpiredToken(navigate) {
  // Clear the access token from cookies or local storage
  document.cookie =
    "access_token=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
  // or localStorage.removeItem('access_token');

  // Redirect the user to the login page
  navigate("/login");

  // Display a notification or message indicating the session has expired
  // You can use a notification library like react-toastify or implement your own logic
  // Example using react-toastify:
  toast.error("Session expired. Please log in again.");

  // Additional cleanup or actions you want to perform when logging out the user
}

export { axiosInstance, handleExpiredToken };
