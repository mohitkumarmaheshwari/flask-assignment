#13. Implement notifications in a Flask app using websockets to notify users of updates.
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Change this to a secure random key
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('notify_user')
def handle_notification(data):
    user_id = data['user_id']
    message = data['message']
    socketio.emit(f'notification_{user_id}', message)  # Send the notification to the specific user

if __name__ == '__main__':
    socketio.run(app,host="0.0.0.0" ,debug=True,port=5005)
