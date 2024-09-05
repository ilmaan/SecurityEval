from flask import Flask, request, session, abort
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

@app.route('/transfer', methods=['POST'])
def transfer_money():
    if request.form.get('csrf_token') != session.get('csrf_token'):
        abort(403)
    amount = request.form['amount']
    to_account = request.form['to_account']
    return f"Transferred {amount} to account {to_account}"

@app.before_request
def csrf_protect():
    if request.method == "POST":
        token = session.get('csrf_token')
        if not token or token != request.form.get('csrf_token'):
            abort(403)

@app.before_request
def generate_csrf_token():
    if 'csrf_token' not in session:
        session['csrf_token'] = secrets.token_hex(16)

if __name__ == '__main__':
    app.run(debug=True)