from flask import Flask, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

users = ['zvia', 'zac', 'jessie']

@app.route("/api/users", methods=['GET'])
def get_users():
    return jsonify(users=users)

@socketio.on('connect')
def handle_connect():
    emit('users', users)

@socketio.on('add_user')
def handle_add_user(username):
    users.append(username)
    emit('users', users, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True, port=8080)