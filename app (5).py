#3. Develop a Flask app that uses URL parameters to display dynamic content.
from flask import Flask, render_template

app = Flask(__name__)

# Define a route that accepts a parameter in the URL
@app.route('/greet/<name>')
def greet(name):
    # Render the dynamic_page.html template with the provided name parameter
    return render_template('dynamic_page.html', name=name)

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,port=8083)
