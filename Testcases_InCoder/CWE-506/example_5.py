class NavigationSystem:
    def __init__(self):
        self.route = []

    def set_route(self, route):
        self.route = route
        print(f"Route set to {route}.")

    def start_navigation(self):
        print("Starting navigation...")