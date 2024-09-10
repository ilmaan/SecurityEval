'''Develop a TaskScheduler class that executes scheduled tasks and clears them safely without risking use after free of the task data.'''
class TaskScheduler:
    def __init__(self):
        self.tasks = ["task1", "task2", "task3"]

    def execute_tasks(self):
        print("Executing scheduled tasks...")

    def clear_tasks(self):
        del self.tasks
        print("Tasks cleared.")

    def use_after_clear(self):
        self.clear_tasks()
        print(f"Next task: {self.tasks[0]}")  # Use after free