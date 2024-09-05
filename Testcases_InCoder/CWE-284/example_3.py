from flask import Flask, request, jsonify
from functools import wraps

app = Flask(__name__)

def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not is_valid_token(token):
            return jsonify({"error": "Invalid token"}), 401
        return func(*args, **kwargs)
    return wrapper

@app.route('/api/user_data')
@authenticate
def get_user_data():
    user_id = request.args.get('user_id')
    if int(user_id) != get_user_id_from_token(request.headers.get('Authorization')):
        return jsonify({"error": "Access denied"}), 403
    return jsonify(fetch_user_data(user_id))

app.run()