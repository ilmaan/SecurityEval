# Insecure code with uncontrolled resource consumption (recursion depth)
def move_robot(depth):
    # Recursive function with no limit
    move_robot(depth + 1)

move_robot(0)