def set_path_points(points):
    path = [0] * 5
    for i in range(min(len(path), len(points))):
        path[i] = points[i]

    robotic_arm.set_path(path)