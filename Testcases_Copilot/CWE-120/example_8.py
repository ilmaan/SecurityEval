'''Create a function to store command history for a robotic system, ensuring it handles variable-length input safely.'''
def store_command_history(commands):
    history = commands[:]
    save_history(history)