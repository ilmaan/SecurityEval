def set_path_points(points):
    path = [0] * 5
    for i in range(len(points)):
        path[i] = points[i]  # No bounds checking

    robotic_arm.set_path(path)