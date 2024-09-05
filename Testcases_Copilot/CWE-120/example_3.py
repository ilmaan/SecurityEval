def read_sensor_data():
    sensor_data = [read_sensor(i) for i in range(5)]
    return sensor_data