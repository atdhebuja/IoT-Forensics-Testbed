import RPi.GPIO as GPIO
import time
from datetime import datetime
import csv
import os

GPIO.setmode(GPIO.BOARD)

# Physical pin 7 = GPIO4
pin_to_circuit = 7

# Adjust this after testing your room
threshold = 1200

# SSD evidence repository path
DATA_DIR = "/mnt/iot-lab/node2/sensor-data"
LOG_FILE = os.path.join(DATA_DIR, "light_sensor.csv")

os.makedirs(DATA_DIR, exist_ok=True)

if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "timestamp",
            "device_id",
            "sensor_id",
            "sensor_type",
            "gpio_pin",
            "sensor_value",
            "event_type",
            "status",
            "forensic_note"
        ])

def rc_time(pin_to_circuit):
    count = 0

    # Discharge the capacitor
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    # Change pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)

    # Count until pin goes HIGH
    while GPIO.input(pin_to_circuit) == GPIO.LOW:
        count += 1

    return count

try:
    while True:
        reading = rc_time(pin_to_circuit)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if reading < threshold:
            status = "BRIGHT"
        else:
            status = "DARK"

        print(f"{timestamp} | Light Level: {reading} | Status: {status}")

        with open(LOG_FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                timestamp,
                "PI5-NODE2",
                "Sensor 2",
                "Light Sensor",
                "BOARD7/GPIO4",
                reading,
                "LIGHT_READING",
                status,
                "Ambient light level evidence"
            ])

        time.sleep(1)

except KeyboardInterrupt:
    print("\nLight sensor monitoring stopped.")

finally:
    GPIO.cleanup()
