from flask import Flask, request, jsonify
import os
import requests
import PyPDF2

app = Flask(__name__)

# Ensure the uploads directory exists
UPLOAD_FOLDER = "./uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/process', methods=['POST'])
def process():
    # Get the location field from the form data
    location = request.form.get("location")
    if not location:
        return jsonify({"error": "Location is required"}), 400

    # Define required files with their corresponding field names
    required_files = ["caseStatement", "complaint", "answer"]
    saved_files = {}
    text_data = {}

    # Process each required file
    for file_key in required_files:
        file = request.files.get(file_key)
        if file and file.filename:  # Check if the file exists and has a filename
            # Save the file to the uploads directory
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(file_path)
            saved_files[file_key] = file_path

            # Convert PDF to text
            with open(file_path, "rb") as pdf_file:
                reader = PyPDF2.PdfReader(pdf_file)  # Change this line
                text = ""
                for page_num in range(len(reader.pages)):  # Update this line as well
                    text += reader.pages[page_num].extract_text()  # Update this line as well
                text_data[file_key] = text
                print(f"Translated text for {file_key}:\n{text}\n")  # Print the translated text
        else:
            return jsonify({"error": f"{file_key} file is missing"}), 400

    # Send the data to the Python backend server
    python_server_url = os.getenv("PYTHON_BACKEND_URL", "http://localhost:5000/process")
    formDataToSend = {
        "location": location,
        "caseStatement": text_data.get("caseStatement"),
        "complaint": text_data.get("complaint"),
        "answer": text_data.get("answer")
    }

    response = requests.post(python_server_url, json=formDataToSend)

    if response.ok:
        return jsonify({
            "message": "Files and data sent to Python server successfully.",
            "location": location,
            "files": saved_files
        }), 200
    else:
        return jsonify({
            "error": "Failed to send data to Python server."
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
