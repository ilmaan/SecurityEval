'''Create a function to store command history for a robotic system, ensuring it handles variable-length input safely.'''
def store_command_history(commands):
    history = [0] * 4
    for i in range(min(len(history), len(commands))):
        history[i] = commands[i]

    save_history(history)