import os
from flask import Flask, jsonify, send_from_directory, send_file
from flask_cors import CORS
import shutil
from flask import request

app = Flask(__name__)
CORS(app)


# Ensure the uploads directory exists
UPLOAD_FOLDER = "./uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


BASE_DOCUMENTS_PATH = os.path.join(os.getcwd(), "frontend", "public", "documents", "responses")

@app.route("/api/case/1/responses", methods=["GET"])
def get_case_responses():

    case_folder = "/Users/main/Desktop/Lawma/Lawmma/agents/case1"
    
    # Check if the folder exists
    # if not os.path.exists(case_folder):
    #     return jsonify({"error": f"Case folder case{case_id} does not exist"}), 404

    # List all PDF files in the case folder
    print('hi')
    response_files = []
    for index, filename in enumerate(os.listdir(case_folder)):
        print(filename)  # Sort for consistent order
        if filename.endswith(".txt"):
            response_files.append({
                "id": index + 1,
                "title": f"Response {index + 1}",
                "url": f"/Users/main/Desktop/Lawma/Lawmma/agents/case1/{filename}"
            })
    return jsonify(response_files)

@app.route('/process', methods=['POST'])
def process():
    # Clear the uploads directory
    for filename in os.listdir(UPLOAD_FOLDER):
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            return jsonify({"error": f"Failed to delete {file_path}. Reason: {e}"}), 500
    # Define required files with their corresponding field names
    required_files = ["caseStatement", "complaint", "answer"]
    saved_files = {}
    # Process each required file
    for file_key in required_files:
        file = request.files.get(file_key)
        if file and file.filename:  # Check if the file exists and has a filename
            # Save the file to the uploads directory
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(file_path)
            saved_files[file_key] = file_path
        else:
            return jsonify({"error": f"{file_key} file is missing"}), 400
    return jsonify({
        "message": "Files saved successfully.",
        "files": saved_files
    }), 200

@app.route('/run_python_file', methods=['POST'])
def run_python_file():
    os.system('python agents/simulationPipeline.py')
    return jsonify({"message": "Python file executed successfully."}), 200

 #Serve static files from the frontend/public directory
@app.route("/api/case/<int:case_id>/response/<filename>", methods=["GET"])
def get_text_response(case_id, filename):
    case_folder = "/Users/main/Desktop/Lawma/Lawmma/agents/case1"
    # case_folder = os.path.join(BASE_DOCUMENTS_PATH, f"case{case_id}")
    file_path = os.path.join(case_folder, filename)

    if not os.path.exists(file_path) or not filename.endswith(".txt"):
        return jsonify({"Error: does not exist or unsupported file"}), 404
    return send_file(file_path, mimetype="text/plain")



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
