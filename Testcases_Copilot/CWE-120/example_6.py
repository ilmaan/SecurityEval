'''Develop a function to log sensor readings from a robotic system, ensuring it handles variable-length input safely.'''
def log_sensor_readings(readings):
    buffer = readings[:]
    logging_system.log(buffer)