from flask import Flask, request, jsonify
from functools import wraps

app = Flask(__name__)

def role_required(role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            token = request.headers.get('Authorization')
            if not is_valid_token(token):
                return jsonify({"error": "Invalid token"}), 401
            if get_user_role(token) != role:
                return jsonify({"error": "Insufficient permissions"}), 403
            return func(*args, **kwargs)
        return wrapper
    return decorator

@app.route('/api/user_data')
@role_required('admin')
def get_user_data():
    user_id = request.args.get('user_id')
    return jsonify(fetch_user_data(user_id))

app.run()