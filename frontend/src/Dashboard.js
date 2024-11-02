import React from "react";
import { useNavigate } from "react-router-dom";
import Layout from "./Layout";
import "./Dashboard.css";

function Dashboard({ email, setLoggedIn }) {
  const navigate = useNavigate();
  const cases = [
    { id: 1, name: "Case 1" },
    { id: 2, name: "Case 2" },
    { id: 3, name: "Case 3" },
    // Add more cases as needed
  ];

  const handleCaseClick = (id) => {
    navigate(`/case/${id}`);
  };

  return (
    <Layout email={email} setLoggedIn={setLoggedIn}>
      <h2>Conversations</h2>
      <div className="cases-list">
        {cases.map((caseItem) => (
          <div
            key={caseItem.id}
            className="case-item"
            onClick={() => handleCaseClick(caseItem.id)}
          >
            {caseItem.name}
          </div>
        ))}
      </div>
    </Layout>
  );
}

export default Dashboard;
