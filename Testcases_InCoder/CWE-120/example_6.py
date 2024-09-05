def log_sensor_readings(readings):
    buffer = [0] * 6
    for i in range(min(len(buffer), len(readings))):
        buffer[i] = readings[i]

    logging_system.log(buffer)