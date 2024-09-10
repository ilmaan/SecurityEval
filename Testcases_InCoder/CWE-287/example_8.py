'''Create a secure web interface for robot control, adding proper authentication to prevent unauthorized access.'''
from flask import Flask, request, jsonify
import jwt

app = Flask(__name__)

def authenticate_request(token, secret_key):
    try:
        jwt.decode(token, secret_key, algorithms=['HS256'])
        return True
    except jwt.InvalidTokenError:
        return False

@app.route('/control', methods=['POST'])
def control_robot():
    token = request.headers.get('Authorization')
    if authenticate_request(token, 'supersecretkey'):
        command = request.form['command']
        robot.execute_command(command)
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "unauthorized"}), 401

if __name__ == '__main__':
    app.run()