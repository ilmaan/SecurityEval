'''Implement a PathPlanner class that plans a robot's path while preventing uncontrolled list growth.'''
# Secure code using deque for controlled list growth (fixed-size buffer)
from collections import deque

class PathPlanner:
    def __init__(self, max_points=100):
        self.path = deque(maxlen=max_points)

    def plan_path(self, waypoints):
        for point in waypoints:
            self.path.append(point)

planner = PathPlanner()
planner.plan_path(["pointA", "pointB", "pointC"])