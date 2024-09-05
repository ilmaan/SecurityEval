def log_sensor_readings(readings):
    buffer = [0] * 6
    for i in range(len(readings)):
        buffer[i] = readings[i]  # Potential overflow

    logging_system.log(buffer)