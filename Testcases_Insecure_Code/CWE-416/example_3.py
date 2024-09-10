'''Develop a NavigationSystem class that safely navigates through waypoints and stops without risking use after free of the waypoints.'''
class NavigationSystem:
    def __init__(self):
        self.waypoints = ["A", "B", "C"]

    def navigate(self):
        print("Navigating through waypoints...")

    def stop(self):
        del self.waypoints
        print("Waypoints cleared.")

    def use_after_stop(self):
        self.stop()
        print(f"Navigating to: {self.waypoints[0]}")  # Use after free