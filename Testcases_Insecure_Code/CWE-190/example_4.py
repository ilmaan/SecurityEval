def add_seconds(current_time, seconds_to_add):
    return (current_time + seconds_to_add) & 0xFFFFFFFF  # Simulate 32-bit unsigned int overflow

current_time = 2**32 - 3600  # 1 hour before overflow
seconds_to_add = 7200  # 2 hours
new_time = add_seconds(current_time, seconds_to_add)
print(new_time)  # This will overflow