import React, { useState } from "react";
import "./Login.css";

function Login({ setLoggedIn, setEmail }) {
  const [emailInput, setEmailInput] = useState("");
  const [passwordInput, setPasswordInput] = useState("");
  const [error, setError] = useState("");

  const handleLogin = () => {
    // Simple validation (replace with real authentication logic)
    if (emailInput && passwordInput) {
      setEmail(emailInput);
      setLoggedIn(true);
    } else {
      setError("Please enter both email and password.");
    }
  };

  return (
    <div className="mainContainer">
      <div className="titleContainer">Login</div>
      <div className="inputContainer">
        <input
          type="email"
          placeholder="Email"
          className="inputBox"
          value={emailInput}
          onChange={(e) => setEmailInput(e.target.value)}
        />
      </div>
      <div className="inputContainer">
        <input
          type="password"
          placeholder="Password"
          className="inputBox"
          value={passwordInput}
          onChange={(e) => setPasswordInput(e.target.value)}
        />
      </div>
      {error && <div className="errorLabel">{error}</div>}
      <button className="loginButton" onClick={handleLogin}>
        Login
      </button>
    </div>
  );
}

export default Login;
