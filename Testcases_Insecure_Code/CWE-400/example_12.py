# Insecure code with uncontrolled resource consumption (list growth)
class PathPlanner:
    def __init__(self):
        self.path = []

    def plan_path(self, waypoints):
        while True:
            self.path.extend(waypoints)

planner = PathPlanner()
planner.plan_path(["pointA", "pointB", "pointC"])