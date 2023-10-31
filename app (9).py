#8.Implement user authentication and registration in a Flask app using Flask-Login.
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user


app = Flask(__name__)
app.config['SECRET_KEY'] = 'b2f7276693524dc1283929277faa0eae'  # Change this to a random secret key
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Dummy database to store user data (in a real app, use a database)
users = {'user': {'password': 'password'}}


class User(UserMixin):
    def __init__(self, username):
        self.username = username

    def get_id(self):
        return self.username


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)
        if user and user['password'] == password:
            user_obj = User(username)
            login_user(user_obj)
            flash('Logged in successfully.', 'success')
            return redirect(url_for('profile'))
        else:
            flash('Invalid username or password.', 'error')
    return render_template('login.html')


@app.route('/profile')
@login_required
def profile():
    return f'Hello, {current_user.username}! This is your profile page.'


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,port=8005)
