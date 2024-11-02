// Layout.js
import React from "react";
import { useNavigate } from "react-router-dom";
import "./Layout.css";

function Layout({ children, email, setLoggedIn }) {
  const navigate = useNavigate();

  const handleLogout = () => {
    setLoggedIn(false);
  };

  const handleAddNewCase = () => {
    navigate("/upload");
  };

  return (
    <div className="dashboard-container">
      <header className="dashboard-header">
        <h1>Lawmma</h1>
        <button onClick={handleLogout} className="logout-button">
          Logout
        </button>
      </header>
      <div className="dashboard-content">
        <nav className="sidebar">
          <div className="user-profile">
            <div className="avatar">
              {/* Placeholder for user avatar */}
              <img
                src={`https://ui-avatars.com/api/?name=${encodeURIComponent(
                  email
                )}&background=004080&color=fff`}
                alt="User Avatar"
              />
            </div>
            <div className="user-name">{email}</div>
          </div>
          {/* Add the "Add New Case" button */}
          <button className="add-case-button" onClick={handleAddNewCase}>
            Add New Case
          </button>
          <ul>
            <li onClick={() => navigate("/dashboard")}>Home</li>
            <li onClick={() => navigate("/dashboard")}>Cases</li>
            <li>Reports</li>
            <li>Settings</li>
          </ul>
        </nav>
        <main className="main-content">{children}</main>
      </div>
    </div>
  );
}

export default Layout;
