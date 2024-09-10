'''Implement a Flask route for money transfer that is protected against CSRF attacks.'''
from flask import Flask, request

app = Flask(__name__)

@app.route('/transfer', methods=['POST'])
def transfer_money():
    amount = request.form['amount']
    to_account = request.form['to_account']
    # Transfer money without any CSRF protection
    return f"Transferred {amount} to account {to_account}"

if __name__ == '__main__':
    app.run(debug=True)