def read_sensor_data():
    sensor_data = [0] * 5
    for i in range(10):  # Reading more data than the buffer can hold
        sensor_data[i] = read_sensor(i)  # Buffer overflow

    return sensor_data