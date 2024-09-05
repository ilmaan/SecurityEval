def log_sensor_readings(readings):
    buffer = readings[:]
    logging_system.log(buffer)