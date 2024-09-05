def store_command_history(commands):
    history = [0] * 4
    for i in range(min(len(history), len(commands))):
        history[i] = commands[i]

    save_history(history)