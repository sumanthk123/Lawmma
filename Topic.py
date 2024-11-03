import os
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


BASE_DOCUMENTS_PATH = os.path.join(os.getcwd(), "frontend", "public", "documents", "responses")

@app.route("/api/case/<int:case_id>/responses", methods=["GET"])
def get_case_responses(case_id):

    case_folder = os.path.join(BASE_DOCUMENTS_PATH, f"case{case_id}")
    
    # Check if the folder exists
    if not os.path.exists(case_folder):
        return jsonify({"error": f"Case folder case{case_id} does not exist"}), 404

    # List all PDF files in the case folder
    response_files = []
    for index, filename in enumerate(sorted(os.listdir(case_folder))):  # Sort for consistent order
        if filename.endswith(".pdf"):
            response_files.append({
                "id": index + 1,
                "title": f"Response {index + 1}",
                "url": f"/documents/responses/case{case_id}/{filename}"
            })

    # Check if we have exactly 10 responses as expected
    # if len(response_files) != 10:
    #     return jsonify({"error": "Expected exactly 10 PDF files in the case folder."}), 400

    return jsonify(response_files)

# Serve static files from the frontend/public directory
@app.route("/documents/responses/<path:filepath>")
def serve_document(filepath):
    # Serve files from the BASE_DOCUMENTS_PATH
    return send_from_directory(BASE_DOCUMENTS_PATH, filepath)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
