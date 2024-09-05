class CommandQueue:
    def __init__(self):
        self.commands = ["cmd1", "cmd2", "cmd3"]

    def execute_commands(self):
        print("Executing commands...")

    def clear_queue(self):
        del self.commands
        print("Command queue cleared.")

    def controlled_execution(self):
        self.execute_commands()
        self.clear_queue()
        # Avoid using `self.commands` after clearing the queue