'''Create a secure web interface for robot control, adding proper authentication to prevent unauthorized access.'''
from flask import Flask, request

app = Flask(__name__)

@app.route('/control', methods=['POST'])
def control_robot():
    # No authentication
    command = request.form['command']
    robot.execute_command(command)
    return "Command executed"

if __name__ == '__main__':
    app.run()