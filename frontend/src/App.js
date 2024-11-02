// App.js
import { Route, Routes, Navigate } from "react-router-dom";
import Login from "./Login";
import Dashboard from "./Dashboard";
import CaseDetail from "./CaseDetail";
import UploadPage from "./UploadPage"; // Import the UploadPage component
import "./App.css";
import { useState } from "react";

function App() {
  const [loggedIn, setLoggedIn] = useState(false);
  const [email, setEmail] = useState("");

  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<Navigate to="/login" />} />
        <Route
          path="/login"
          element={
            loggedIn ? (
              <Navigate to="/dashboard" />
            ) : (
              <Login setLoggedIn={setLoggedIn} setEmail={setEmail} />
            )
          }
        />
        <Route
          path="/dashboard"
          element={
            loggedIn ? (
              <Dashboard email={email} setLoggedIn={setLoggedIn} />
            ) : (
              <Navigate to="/login" />
            )
          }
        />
        <Route
          path="/case/:id"
          element={
            loggedIn ? (
              <CaseDetail email={email} setLoggedIn={setLoggedIn} />
            ) : (
              <Navigate to="/login" />
            )
          }
        />
        {/* Add the new route for UploadPage */}
        <Route
          path="/upload"
          element={
            loggedIn ? (
              <UploadPage email={email} setLoggedIn={setLoggedIn} />
            ) : (
              <Navigate to="/login" />
            )
          }
        />
      </Routes>
    </div>
  );
}

export default App;
