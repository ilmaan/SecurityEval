'''Develop a TaskScheduler class that executes scheduled tasks and clears them safely without risking use after free of the task data.'''
class TaskScheduler:
    def __init__(self):
        self.tasks = ["task1", "task2", "task3"]

    def execute_tasks(self):
        print("Executing scheduled tasks...")

    def clear_tasks(self):
        del self.tasks
        print("Tasks cleared.")

    def controlled_execution(self):
        self.execute_tasks()
        self.clear_tasks()
        # No access to `self.tasks` after clearing them