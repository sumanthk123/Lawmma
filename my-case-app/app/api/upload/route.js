import { NextResponse } from "next/server";

export async function POST(request) {
  const formData = await request.formData();

  const location = formData.get("location");
  const caseStatement = formData.get("caseStatement");
  const complaint = formData.get("complaint");
  const answer = formData.get("answer");

  const pythonServerUrl =
    process.env.PYTHON_BACKEND_URL || "http://127.0.0.1:5000/process";
  const formDataToSend = new FormData();
  formDataToSend.append("location", location);
  formDataToSend.append("caseStatement", caseStatement);
  formDataToSend.append("complaint", complaint);
  formDataToSend.append("answer", answer);

  const response = await fetch(pythonServerUrl, {
    method: "POST",
    body: formDataToSend,
  });

  if (response.ok) {
    return NextResponse.json({
      message: "Files and data sent to Python server successfully.",
    });
  } else {
    return NextResponse.json(
      { message: "Failed to send data to Python server." },
      { status: 500 }
    );
  }
}
