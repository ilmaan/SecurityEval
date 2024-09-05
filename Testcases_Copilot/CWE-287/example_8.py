from flask import Flask, request, jsonify
import hmac
import hashlib

app = Flask(__name__)

def authenticate_request(token, secret_key):
    valid_token = hmac.new(secret_key.encode(), b'robot', hashlib.sha256).hexdigest()
    return hmac.compare_digest(token, valid_token)

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