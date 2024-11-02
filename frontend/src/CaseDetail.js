import React from "react";
import { useParams } from "react-router-dom";
import Layout from "./Layout";
import "./CaseDetail.css";

function CaseDetail({ email, setLoggedIn }) {
  const { id } = useParams();

  return (
    <Layout email={email} setLoggedIn={setLoggedIn}>
      <h2>Case Detail</h2>
      <p>You are viewing details for case {id}.</p>
      {/* Add main content here */}
    </Layout>
  );
}

export default CaseDetail;
