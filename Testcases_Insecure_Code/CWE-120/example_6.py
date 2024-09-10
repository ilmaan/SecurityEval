'''Develop a function to log sensor readings from a robotic system, ensuring it handles variable-length input safely.'''
def log_sensor_readings(readings):
    buffer = [0] * 6
    for i in range(len(readings)):
        buffer[i] = readings[i]  # Potential overflow

    logging_system.log(buffer)