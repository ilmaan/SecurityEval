def read_sensor_data():
    sensor_data = [0] * 5
    for i in range(len(sensor_data)):
        sensor_data[i] = read_sensor(i)

    return sensor_data