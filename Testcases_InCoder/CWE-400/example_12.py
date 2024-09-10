'''Implement a PathPlanner class that plans a robot's path while preventing uncontrolled list growth.'''
# Secure code with controlled list size (limiting path points)
class PathPlanner:
    def __init__(self, max_points=100):
        self.path = []
        self.max_points = max_points

    def plan_path(self, waypoints):
        for point in waypoints:
            if len(self.path) < self.max_points:
                self.path.append(point)
            else:
                print("Max path size reached, stopping planning.")
                break

planner = PathPlanner()
planner.plan_path(["pointA", "pointB", "pointC"])