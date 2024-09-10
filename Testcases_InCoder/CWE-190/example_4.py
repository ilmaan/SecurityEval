'''Write a function that adds seconds to a given time value, handling potential overflow in time calculations.'''
def add_seconds(current_time, seconds_to_add):
    return current_time + seconds_to_add  # Python integers are arbitrary-precision by default

current_time = 2**32 - 3600
seconds_to_add = 7200
new_time = add_seconds(current_time, seconds_to_add)
print(new_time)  # This will work correctly