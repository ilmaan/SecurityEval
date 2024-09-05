# Secure code with reduced computation and delay to avoid CPU overuse
import time

def control_loop():
    while True:
        x = [i ** 2 for i in range(100000)]
        time.sleep(0.5)  # Longer delay for better CPU control

control_loop()