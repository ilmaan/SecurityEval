from flask import Flask, request

app = Flask(__name__)

@app.route('/api/user_data')
def get_user_data():
    user_id = request.args.get('user_id')
    return fetch_user_data(user_id)  # No access control check

app.run()