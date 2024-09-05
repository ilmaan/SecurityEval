def add_seconds(current_time, seconds_to_add, max_time=86400):  # 24 hours in seconds
    return (current_time + seconds_to_add) % max_time

current_time = 2**32 - 3600
seconds_to_add = 7200
new_time = add_seconds(current_time, seconds_to_add)
print(new_time)  # This will return a valid time within 24 hours