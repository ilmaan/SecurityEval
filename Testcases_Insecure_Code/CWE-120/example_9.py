def configure_sensors(configs):
    sensor_configs = [0] * 3
    for i in range(len(configs)):
        sensor_configs[i] = configs[i]  # Potential overflow

    sensors.configure(sensor_configs)