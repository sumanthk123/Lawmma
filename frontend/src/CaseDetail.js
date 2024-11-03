// import React, { useState, useEffect } from "react";
// import { useParams } from "react-router-dom";
// import Layout from "./Layout";
// import "./CaseDetail.css";

// function CaseDetail({ email, setLoggedIn }) {
//   const { id } = useParams();
//   const [responses, setResponses] = useState([]);
//   const [selectedResponse, setSelectedResponse] = useState(null);

//   useEffect(() => {
//     const fetchResponses = async () => {
//       try {
//         const response = await fetch(
//           `http://127.0.0.1:5001/api/case/${id}/responses`
//         );
//         if (!response.ok) {
//           throw new Error("Failed to load responses");
//         }
//         const data = await response.json();
//         setResponses(data);
//         setSelectedResponse(null);
//       } catch (error) {
//         console.error("Error fetching responses:", error);
//       }
//     };

//     fetchResponses();
//   }, [id]);

//   const handleResponseChange = (event) => {
//     setSelectedResponse(event.target.value);
//   };

//   return (
//     <Layout email={email} setLoggedIn={setLoggedIn}>
//       <div className="case-detail-container">
//         <h2 className="case-detail-title">Case Details for {id}</h2>

//         <div className="response-select">
//           <label>Select a response: </label>
//           <select
//             defaultValue=""
//             onChange={handleResponseChange}
//             className="dropdown"
//           >
//             <option value="" disabled>
//               Select a response
//             </option>
//             {responses.map((response) => (
//               <option key={response.id} value={response.url}>
//                 {response.title}
//               </option>
//             ))}
//           </select>
//         </div>

//         <div className="pdf-viewer">
//           {selectedResponse && (
//             <iframe
//               title="Response PDF"
//               src={selectedResponse}
//               width="100%"
//               height="600px"
//             />
//           )}
//         </div>
//       </div>
//     </Layout>
//   );
// }

// export default CaseDetail;

// import React, { useState, useEffect } from "react";
// import { useParams } from "react-router-dom";
// import Layout from "./Layout";
// import "./CaseDetail.css";

// function CaseDetail({ email, setLoggedIn }) {
//   const { id } = useParams();
//   const [responses, setResponses] = useState([]);
//   const [selectedResponse, setSelectedResponse] = useState(null);

//   useEffect(() => {
//     const fetchResponses = async () => {
//       try {
//         const response = await fetch(`http://127.0.0.1:5000/api/case/${id}/responses`);
//         if (!response.ok) {
//           throw new Error("Failed to load responses");
//         }
//         const data = await response.json();
//         setResponses(data);
//         setSelectedResponse(null);
//       } catch (error) {
//         console.error("Error fetching responses:", error);
//       }
//     };

//     fetchResponses();
//   }, [id]);

//   const handleResponseChange = (event) => {
//     setSelectedResponse(event.target.value);
//   };

//   return (
//     <Layout email={email} setLoggedIn={setLoggedIn}>
//       <div className="case-detail-container">
//         <h2 className="case-detail-title">Case Details for {id}</h2>

//         <div className="response-select">
//           <label>Select a response: </label>
//           <select defaultValue="" onChange={handleResponseChange} className="dropdown">
//             <option value="" disabled>
//               Select a response
//             </option>
//             {responses.map((response) => (
//               <option key={response.id} value={response.url}>
//                 {response.title}
//               </option>
//             ))}
//           </select>
//         </div>

//         <div className="pdf-viewer">
//           {selectedResponse && (
//             <iframe
//               title="Response PDF"
//               src={selectedResponse}
//               width="100%"
//               height="600px"
//             />
//           )}
//         </div>
//       </div>
//     </Layout>
//   );
// }

// export default CaseDetail;

import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import Layout from "./Layout";
import "./CaseDetail.css";

function CaseDetail({ email, setLoggedIn }) {
  const { id } = useParams();
  const [responses, setResponses] = useState([]);
  const [selectedResponse, setSelectedResponse] = useState(null);
  const [textContent, setTextContent] = useState("");

  // Fetch responses based on case ID
  useEffect(() => {
    const fetchResponses = async () => {
      try {
        const response = await fetch(
          `http://127.0.0.1:5001/api/case/1/responses`
        );
        if (!response.ok) {
          throw new Error("Failed to load responses");
        }
        const data = await response.json();

        const adjustedResponses = data.map((response) => ({
          ...response,
          url: `/api/case/1/response/${response.url.split("/").pop()}`, // Extract filename from the url
        }));

        setResponses(adjustedResponses);
        setSelectedResponse(null); // Reset selection when case changes
        setTextContent(""); // Clear text content
      } catch (error) {
        console.error("Error fetching responses:", error);
      }
    };

    fetchResponses();
  }, [id]);

  // Fetch and display the content of the selected response
  const handleResponseChange = async (event) => {
    const responseUrl = event.target.value;

    setSelectedResponse(responseUrl);

    try {
      const response = await fetch(`http://127.0.0.1:5001${responseUrl}`);

      console.log("Response status:", response.status); // Log response status

      if (!response.ok) {
        throw new Error("Failed to load response content");
      }
      const text = await response.text();
      setTextContent(text);
    } catch (error) {
      console.error("Error fetching response content:", error);
      setTextContent("Error loading content.");
    }
  };

  return (
    <Layout email={email} setLoggedIn={setLoggedIn}>
      <div className="case-detail-container">
        <h2 className="case-detail-title">Case Details for {id}</h2>

        <div className="response-select">
          <label>Select a response: </label>
          <select
            defaultValue=""
            onChange={handleResponseChange}
            className="dropdown"
          >
            <option value="" disabled>
              Select a response
            </option>
            {responses.map((response) => (
              <option key={response.id} value={response.url}>
                {response.title}
              </option>
            ))}
          </select>
        </div>

        <div className="text-viewer">
          {textContent && <pre>{textContent}</pre>}
        </div>
      </div>
    </Layout>
  );
}

export default CaseDetail;
