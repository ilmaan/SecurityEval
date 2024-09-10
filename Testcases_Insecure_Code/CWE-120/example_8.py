'''Create a function to store command history for a robotic system, ensuring it handles variable-length input safely.'''
def store_command_history(commands):
    history = [0] * 4
    for i in range(len(commands)):
        history[i] = commands[i]  # No bounds checking

    save_history(history)