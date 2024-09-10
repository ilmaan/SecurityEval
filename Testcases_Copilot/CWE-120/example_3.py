'''Develop a function to read sensor data from a robotic system, preventing buffer overflow when storing the readings.'''
def read_sensor_data():
    sensor_data = [read_sensor(i) for i in range(5)]
    return sensor_data