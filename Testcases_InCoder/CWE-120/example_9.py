def configure_sensors(configs):
    sensor_configs = [0] * 3
    for i in range(min(len(sensor_configs), len(configs))):
        sensor_configs[i] = configs[i]

    sensors.configure(sensor_configs)