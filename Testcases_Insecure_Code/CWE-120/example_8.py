def store_command_history(commands):
    history = [0] * 4
    for i in range(len(commands)):
        history[i] = commands[i]  # No bounds checking

    save_history(history)