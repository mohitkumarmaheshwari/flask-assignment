#5. Implement user sessions in a Flask app to store and display user-specific data.
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

# Set the secret key to enable session cookies
app.secret_key = 'your_secret_key'

# Define a route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    # Check if 'username' key is in the session
    if 'username' in session:
        # If username is in session, welcome the user
        username = session['username']
        return f'Welcome, {username}! <a href="/logout">Logout</a>'
    else:
        # If username is not in session, show the login form
        if request.method == 'POST':
            # Get username from the form and store it in the session
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        return render_template('index.html')

# Define a route to logout the user
@app.route('/logout')
def logout():
    # Remove 'username' key from the session to logout the user
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,port=8085)
