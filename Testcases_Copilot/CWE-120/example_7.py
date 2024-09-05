def set_path_points(points):
    path = points[:]
    robotic_arm.set_path(path)