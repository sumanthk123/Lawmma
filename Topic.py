import os
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# Ensure the uploads directory exists
UPLOAD_FOLDER = "./uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

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

@app.route('/run_python_file', methods=['POST'])
def run_python_file():
    os.system('python simulationPipeline.py')
    return jsonify({"message": "Python file executed successfully."}), 200



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
