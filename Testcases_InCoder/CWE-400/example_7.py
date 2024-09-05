# Secure code with recursion limit
def move_robot(depth, max_depth=1000):
    if depth >= max_depth:
        print("Max recursion depth reached")
        return
    move_robot(depth + 1, max_depth)

move_robot(0)