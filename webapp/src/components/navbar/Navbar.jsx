import React, { useRef, useState, useEffect } from "react";
import "./navbar.scss";
import SearchOutlinedIcon from "@mui/icons-material/SearchOutlined";
import LanguageOutlinedIcon from "@mui/icons-material/LanguageOutlined";
import DarkModeOutlinedIcon from "@mui/icons-material/DarkModeOutlined";
import FullscreenExitOutlinedIcon from "@mui/icons-material/FullscreenExitOutlined";
import NotificationsNoneOutlinedIcon from "@mui/icons-material/NotificationsNoneOutlined";
import ChatBubbleOutlineOutlinedIcon from "@mui/icons-material/ChatBubbleOutlineOutlined";
import ListOutlinedIcon from "@mui/icons-material/ListOutlined";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const Navbar = () => {
  const menu = ["Profile", "Settings", "Logout"];
  const [open, setOpen] = useState(false);

  const menuRef = useRef();
  const imgRef = useRef();

  useEffect(() => {
    const handleClickOutside = (event) => {
      if (
        menuRef.current &&
        !menuRef.current.contains(event.target) &&
        event.target !== imgRef.current
      ) {
        setOpen(false);
      }
    };

    document.addEventListener("click", handleClickOutside);
    return () => {
      document.removeEventListener("click", handleClickOutside);
    };
  }, []);

  const navigate = useNavigate();

  const handleLogout = async () => {
    try {
      // Send a POST request to the logout endpoint
      await axios.post("http://127.0.0.1:8000/logout", null, {
        withCredentials: true,
      });

      // Clear the access token cookie
      document.cookie =
        "access_token=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";

      // Redirect or perform any additional client-side cleanup
      navigate("/login");
    } catch (error) {
      console.error("Logout Failed:", error);
      // Handle logout error, e.g., display error message to the user
    }
  };

  const handleMenuClick = (item) => {
    if (item === "Logout") {
      handleLogout();
    } else {
      // Handle clicks for other menu items if needed
    }
  };

  return (
    <div className="navbar">
      <div className="wrapper">
        <div className="search">
          <input type="text" placeholder="Search..." />
          <SearchOutlinedIcon />
        </div>
        <div className="items">
          <div className="item">
            <LanguageOutlinedIcon />
            English
          </div>
          <div className="item">
            <DarkModeOutlinedIcon className="icon" />
          </div>
          <div className="item">
            <FullscreenExitOutlinedIcon className="icon" />
          </div>
          <div className="item">
            <NotificationsNoneOutlinedIcon className="icon" />
            <div className="counter">1</div>
          </div>
          <div className="item">
            <ChatBubbleOutlineOutlinedIcon className="icon" />
            <div className="counter">2</div>
          </div>
          <div className="item">
            <ListOutlinedIcon className="icon" />
          </div>
          <div className="item">
            <img
              ref={imgRef}
              onClick={() => setOpen(!open)}
              src="https://images.pexels.com/photos/941693/pexels-photo-941693.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500"
              alt=""
              className="avatar"
            />
            {open && (
              <div ref={menuRef} className="menu-item">
                <ul>
                  {menu.map((item) => (
                    <li
                      //onClick={() => setOpen(false)}
                      onClick={() => handleMenuClick(item)}
                      className="item-menu"
                      key={item}
                    >
                      {item}
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Navbar;
