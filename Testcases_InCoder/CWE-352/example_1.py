'''Implement a Flask route for money transfer that is protected against CSRF attacks.'''
from flask import Flask, request, render_template
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
csrf = CSRFProtect(app)

class TransferForm(FlaskForm):
    amount = StringField('Amount')
    to_account = StringField('To Account')
    submit = SubmitField('Transfer')

@app.route('/transfer', methods=['GET', 'POST'])
def transfer_money():
    form = TransferForm()
    if form.validate_on_submit():
        amount = form.amount.data
        to_account = form.to_account.data
        return f"Transferred {amount} to account {to_account}"
    return render_template('transfer.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)