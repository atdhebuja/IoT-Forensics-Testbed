import RPi.GPIO as GPIO
import time
from datetime import datetime
import csv
import os

GPIO.setmode(GPIO.BCM)

PIR_PIN = 23

# SSD evidence repository path
DATA_DIR = "/mnt/iot-lab/node2/sensor-data"
LOG_FILE = os.path.join(DATA_DIR, "pir_motion_events.csv")

os.makedirs(DATA_DIR, exist_ok=True)

GPIO.setup(PIR_PIN, GPIO.IN)

if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "timestamp",
            "sensor_id",
            "sensor_type",
            "gpio_pin",
            "event_type",
            "raw_value",
            "forensic_note"
        ])

previous_state = None

print("PIR Motion Sensor Forensic Monitoring Started")
print("0 = No Motion | 1 = Motion Detected")

try:
    while True:
        current_state = GPIO.input(PIR_PIN)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if current_state != previous_state:
            if current_state == 1:
                event_type = "MOTION_DETECTED"
                note = "Possible physical presence near IoT device"
            else:
                event_type = "MOTION_CLEARED"
                note = "No motion currently detected"

            print(f"{timestamp} | Sensor 3 | PIR Motion | GPIO23={current_state} | {event_type}")

            with open(LOG_FILE, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([
                    timestamp,
                    "Sensor 3",
                    "PIR Motion Sensor",
                    "GPIO23",
                    event_type,
                    current_state,
                    note
                ])

            previous_state = current_state

        time.sleep(0.5)

except KeyboardInterrupt:
    print("\nMonitoring stopped.")

finally:
    GPIO.cleanup()
