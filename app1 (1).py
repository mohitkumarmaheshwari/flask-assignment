#1. Create a Flask app that displays "Hello, World!" on the homepage.
from flask import Flask

# Create a Flask web server
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def hello_world():
    # Display "Hello, World!" on the homepage
    return 'Hello, World!'

# Run the Flask app
if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,port=8080)
