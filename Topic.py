from flask import Flask, request, jsonify
import os
import shutil

app = Flask(__name__)

# Ensure the uploads directory exists
UPLOAD_FOLDER = "./uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

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

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
