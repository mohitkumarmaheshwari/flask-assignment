#10. Design a Flask app with proper error handling for 404 and 500 errors.
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a secure random key
login_manager = LoginManager()
login_manager.init_app(app)

# Dummy user database (replace this with a real database)
users = {
    'user_id': {
        'username': 'username',
        'password': 'password'
    }
}

# User class for Flask-Login
class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id

# User loader function for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

# Routes for registration, login, dashboard, and logout
# (Routes implementation goes here)

# Custom error handling for 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# Custom error handling for 500 - Internal Server Error
@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,port=5005)

