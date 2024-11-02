"use client";

import React, { useState } from "react";

export default function UploadPage() {
  const [location, setLocation] = useState("");
  const [caseStatement, setCaseStatement] = useState(null);
  const [complaint, setComplaint] = useState(null);
  const [answer, setAnswer] = useState(null);

  const handleFileChange = (e, setFile) => {
    const file = e.target.files[0];
    setFile(file);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append("location", location);
    formData.append("caseStatement", caseStatement);
    formData.append("complaint", complaint);
    formData.append("answer", answer);

    const response = await fetch("/api/upload", {
      method: "POST",
      body: formData,
    });

    if (response.ok) {
      alert("Files and location data uploaded successfully!");
    } else {
      alert("Upload failed. Please try again.");
    }
  };

  return (
    <div style={styles.container}>
      <h1 style={styles.heading}>Upload Case Documents</h1>
      <form onSubmit={handleSubmit} style={styles.form}>
        <label style={styles.label}>
          Location:
          <input
            type="text"
            value={location}
            onChange={(e) => setLocation(e.target.value)}
            required
            style={styles.input}
          />
        </label>

        <label style={styles.label}>
          Upload Case Statement:
          <input
            type="file"
            onChange={(e) => handleFileChange(e, setCaseStatement)}
            accept=".pdf,.doc,.docx,.txt"
            required
            style={styles.fileInput}
          />
        </label>

        <label style={styles.label}>
          Upload Complaint:
          <input
            type="file"
            onChange={(e) => handleFileChange(e, setComplaint)}
            accept=".pdf,.doc,.docx,.txt"
            required
            style={styles.fileInput}
          />
        </label>

        <label style={styles.label}>
          Upload Answer:
          <input
            type="file"
            onChange={(e) => handleFileChange(e, setAnswer)}
            accept=".pdf,.doc,.docx,.txt"
            required
            style={styles.fileInput}
          />
        </label>

        <button type="submit" style={styles.button}>
          Submit
        </button>
      </form>
    </div>
  );
}

const styles = {
  container: {
    padding: "20px",
    maxWidth: "600px",
    margin: "auto",
    fontFamily: "Arial, sans-serif",
  },
  heading: {
    fontSize: "24px",
    fontWeight: "bold",
    marginBottom: "20px",
    textAlign: "center",
  },
  form: {
    display: "flex",
    flexDirection: "column",
    gap: "15px",
  },
  label: {
    fontSize: "16px",
    fontWeight: "bold",
    marginBottom: "5px",
  },
  input: {
    padding: "8px",
    borderRadius: "4px",
    border: "1px solid #ccc",
    fontSize: "14px",
    width: "100%",
  },
  fileInput: {
    padding: "8px",
    border: "1px solid #ccc",
    borderRadius: "4px",
    fontSize: "14px",
    width: "100%",
  },
  button: {
    padding: "10px 15px",
    fontSize: "16px",
    fontWeight: "bold",
    color: "#fff",
    backgroundColor: "#0070f3",
    border: "none",
    borderRadius: "4px",
    cursor: "pointer",
    textAlign: "center",
  },
};
