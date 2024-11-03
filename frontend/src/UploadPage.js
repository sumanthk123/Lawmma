import React, { useState } from "react";
import Layout from "./Layout";
import "./UploadPage.css";

function UploadPage({ email, setLoggedIn }) {
  const [location, setLocation] = useState("");
  const [caseStatement, setCaseStatement] = useState(null);
  const [complaint, setComplaint] = useState(null);
  const [answer, setAnswer] = useState(null);

  const handleFileChange = (e, setFile) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Prepare the form data
    const formData = new FormData();
    formData.append("location", location);
    formData.append("caseStatement", caseStatement);
    formData.append("complaint", complaint);
    formData.append("answer", answer);

    try {
      const response = await fetch("http://127.0.0.1:5001/process", {
        method: "POST",
        body: formData,
      });

      const result = await response.json();

      if (response.ok) {
        alert(result.message);
        // Optionally reset the form
        setLocation("");
        setCaseStatement(null);
        setComplaint(null);
        setAnswer(null);
      } else {
        alert(`Upload failed: ${result.error || "Unknown error"}`);
      }
    } catch (error) {
      console.error("Error uploading files:", error);
    }

    const pythonResponse = await fetch(
      "http://127.0.0.1:5001/run_python_file",
      {
        method: "POST",
      }
    );

    const pythonResult = await pythonResponse.json();

    if (pythonResponse.ok) {
      alert(pythonResult.message);
    } else {
      alert(
        `Failed to run Python file: ${pythonResult.error || "Unknown error"}`
      );
    }
  };

  return (
    <Layout email={email} setLoggedIn={setLoggedIn}>
      <div className="upload-container">
        <h1 className="upload-heading">Upload Case Documents</h1>
        <form onSubmit={handleSubmit} className="upload-form">
          <label className="upload-label">
            Location:
            <input
              type="text"
              value={location}
              onChange={(e) => setLocation(e.target.value)}
              required
              className="upload-input"
            />
          </label>

          <label className="upload-label">
            Upload Case Statement:
            <input
              type="file"
              onChange={(e) => handleFileChange(e, setCaseStatement)}
              accept=".pdf,.doc,.docx,.txt"
              required
              className="upload-file-input"
            />
          </label>

          <label className="upload-label">
            Upload Complaint:
            <input
              type="file"
              onChange={(e) => handleFileChange(e, setComplaint)}
              accept=".pdf,.doc,.docx,.txt"
              required
              className="upload-file-input"
            />
          </label>

          <label className="upload-label">
            Upload Answer:
            <input
              type="file"
              onChange={(e) => handleFileChange(e, setAnswer)}
              accept=".pdf,.doc,.docx,.txt"
              required
              className="upload-file-input"
            />
          </label>

          <button type="submit" className="upload-button">
            Submit
          </button>
        </form>
      </div>
    </Layout>
  );
}

export default UploadPage;
