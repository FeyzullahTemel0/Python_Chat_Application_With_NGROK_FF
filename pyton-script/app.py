from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Scret Key Buraya!!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    message = data['message']
    sender = data['sender']
    emit('message', {'message': message, 'sender': sender}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
