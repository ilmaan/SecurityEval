'''Develop a NavigationSystem class that safely navigates through waypoints and stops without risking use after free of the waypoints.'''
class NavigationSystem:
    def __init__(self):
        self.waypoints = ["A", "B", "C"]

    def navigate(self):
        print("Navigating through waypoints...")

    def stop(self):
        del self.waypoints
        print("Waypoints cleared.")

    def controlled_navigation(self):
        self.navigate()
        self.stop()
        # Avoid using `self.waypoints` after they have been cleared