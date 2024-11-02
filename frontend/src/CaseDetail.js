import React from "react";
import { useParams } from "react-router-dom";
import Layout from "./Layout";
import "./CaseDetail.css";

function CaseDetail({ email, setLoggedIn }) {
  const { id } = useParams();

  const responses = [
    {id: 1, title: "Response 1", url: "/documents/responses/example1"},
    {id: 2, title: "Response 2", url: "/documents/responses/example2"},
    {id: 3, title: "Response 3", url: "/documents/responses/example3"},
    // Add more responses here
  ];
  const [selectedResponse, setSelectedResponse] = React.useState(null);

  const handleResponseChange = (event) => {
    setSelectedResponse(event.target.value);
  };

  return (
    <Layout email={email} setLoggedIn={setLoggedIn}>
      <h2>Case Details for {id} </h2>
      <p>You are viewing details for case {id}.</p>
      <div className="response-select"> 
        <label> Select a response: </label>
        <select defualtValue="" onChange={handleResponseChange}>
          
          <option value="">
            Select a response
          </option>

          {responses.map((response) => (

            <option key={response.id} value={response.url}>
              {response.title}
            </option>

          ))}
        </select>
      </div>

      <div className="pdf-viewer">
        {selectedResponse && (
          <iframe
            title="Response PDF"
            src={selectedResponse + ".pdf"}
            width="100%"
            height="600px"
          />
        )}
      </div>
    </Layout>
  );
}

export default CaseDetail;
