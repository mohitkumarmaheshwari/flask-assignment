#6. Build a Flask app that allows users to upload files and display them on the website.
from flask import Flask, request, render_template
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'  # Folder where uploaded files will be stored

# Ensure the 'uploads' directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if the post request has a file part
        if 'file' not in request.files:
            return render_template('index.html', error='No file part')
        
        file = request.files['file']
        
        # If the user does not select a file, browser also submits an empty file
        if file.filename == '':
            return render_template('index.html', error='No selected file')
        
        if file:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)
            return render_template('index.html', success='File uploaded successfully', filename=file.filename)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,port=8080)
