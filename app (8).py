#6. Build a Flask app that allows users to upload files and display them on the website.
import os
from flask import Flask, render_template, request

app = Flask(__name__)

# Set the upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to check if the file has an allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Define a route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if the POST request has a file part
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        
        # If the user does not select a file, browser submits an empty file without a filename
        if file.filename == '':
            return redirect(request.url)

        # If the file is allowed, save it and redirect to the home page
        if file and allowed_file(file.filename):
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)
            return redirect('/')
    
    # List the files in the uploads folder
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    
    # Render the template with the list of uploaded files
    return render_template('index.html', files=files)

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,port=8088)
