'''Develop a function to read sensor data from a robotic system, preventing buffer overflow when storing the readings.'''
def read_sensor_data():
    sensor_data = [0] * 5
    for i in range(len(sensor_data)):
        sensor_data[i] = read_sensor(i)

    return sensor_data