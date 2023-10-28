#4. Create a Flask app with a form that accepts user input and displays it.
from flask import Flask, render_template, request

app = Flask(__name__)

# Define a route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    # Initialize message variable
    message = None

    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        # Get user input from the form
        user_input = request.form['user_input']
        # Process the user input (in this case, simply echoing it back)
        message = f'You entered: {user_input}'

    # Render the template with the form and the message
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,port=8081)
