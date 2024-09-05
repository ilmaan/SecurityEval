class TaskScheduler:
    def __init__(self):
        self.tasks = ["task1", "task2", "task3"]

    def execute_tasks(self):
        print("Executing scheduled tasks...")

    def clear_tasks(self):
        del self.tasks
        print("Tasks cleared.")

    def safe_execution(self):
        self.clear_tasks()
        if hasattr(self, 'tasks'):
            print(f"Next task: {self.tasks[0]}")
        else:
            print("Tasks have been cleared, cannot execute.")