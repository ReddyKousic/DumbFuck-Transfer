import os
from flask import Flask, render_template, request, send_file

app = Flask(__name__)

# Define the upload folder where files will be stored temporarily.
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    # Get the list of uploaded files in the UPLOAD_FOLDER
    uploaded_files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index1.html', files=uploaded_files)

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']

    if file.filename == '':
        return "No selected file"

    # Save the uploaded file to the UPLOAD_FOLDER.
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

    return "File successfully uploaded"

@app.route('/download/<filename>', methods=['GET'])
def download(filename):
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), as_attachment=True)

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True, host="0.0.0.0", port="6798")

# import os
# from flask import Flask, render_template, request, send_file, jsonify, redirect

# app = Flask(__name__)

# # Define the upload folder where files will be stored temporarily.
# UPLOAD_FOLDER = 'uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# @app.route('/')
# def index():
#     # Get the list of uploaded files in the UPLOAD_FOLDER
#     uploaded_files = os.listdir(app.config['UPLOAD_FOLDER'])
#     return render_template('index1.html', files=uploaded_files)

# @app.route('/upload', methods=['POST'])
# def upload():
#     if 'file' not in request.files:
#         return "No file part"
    
#     file = request.files['file']

#     if file.filename == '':
#         return "No selected file"

#     # Get the file size for progress tracking
#     file_size = os.fstat(file.fileno()).st_size

#     # Save the uploaded file to the UPLOAD_FOLDER.
#     file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#     file.save(file_path)

#     # return jsonify({"message": "File successfully uploaded", "file_path": file_path, "file_size": file_size})
#     return redirect("/")

# @app.route('/download/<filename>', methods=['GET'])
# def download(filename):
#     file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#     if os.path.isfile(file_path):
#         return send_file(file_path, as_attachment=True)
#     else:
#         return "File not found"

# if __name__ == '__main__':
#     if not os.path.exists(UPLOAD_FOLDER):
#         os.makedirs(UPLOAD_FOLDER)
#     app.run(debug=True, host="0.0.0.0", port="6798")
