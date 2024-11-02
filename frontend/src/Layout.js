import React from "react";
import "./Layout.css";

function Layout({ children, email, setLoggedIn }) {
  const handleLogout = () => {
    setLoggedIn(false);
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
          <ul>
            <li>Home</li>
            <li>Cases</li>
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
