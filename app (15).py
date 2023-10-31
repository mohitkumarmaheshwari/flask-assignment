#12. Build a Flask app that updates data in real-time using WebSocket connections.
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Change this to a secure random key
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('update_data')
def handle_update(data):
    socketio.emit('update_data', data)  # Broadcast the updated data to all connected clients

if __name__ == '__main__':
    socketio.run(app,host="0.0.0.0" ,debug=True,port=5005)
