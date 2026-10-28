import RPi.GPIO as GPIO
from datetime import datetime
from time import sleep
import csv
import os

GPIO.setmode(GPIO.BCM)

BUTTON_PIN = 17
LED_PIN = 27

# SSD evidence repository path
DATA_DIR = "/mnt/iot-lab/node2/sensor-data"
LOG_FILE = os.path.join(DATA_DIR, "tamper_button_events.csv")

os.makedirs(DATA_DIR, exist_ok=True)

GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_PIN, GPIO.OUT)

GPIO.output(LED_PIN, GPIO.LOW)

if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "timestamp",
            "device_id",
            "sensor_id",
            "sensor_type",
            "button_gpio_pin",
            "led_gpio_pin",
            "event_type",
            "raw_value",
            "led_status",
            "forensic_note"
        ])

print("Tamper button monitoring started")
print("Not pressed = 1 | Pressed = 0")

previous_state = GPIO.input(BUTTON_PIN)

try:
    while True:
        current_state = GPIO.input(BUTTON_PIN)

        if current_state != previous_state:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            if current_state == 0:
                GPIO.output(LED_PIN, GPIO.HIGH)
                event_type = "TAMPER_DETECTED"
                led_status = "LED_ON"
                note = "Physical tamper button was pressed"
                print(f"{timestamp} | TAMPER DETECTED | LED ON")
            else:
                GPIO.output(LED_PIN, GPIO.LOW)
                event_type = "TAMPER_RELEASED"
                led_status = "LED_OFF"
                note = "Physical tamper button was released"
                print(f"{timestamp} | TAMPER RELEASED | LED OFF")

            with open(LOG_FILE, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([
                    timestamp,
                    "PI5-NODE2",
                    "Sensor 4",
                    "Tamper Button",
                    "GPIO17",
                    "GPIO27",
                    event_type,
                    current_state,
                    led_status,
                    note
                ])

            previous_state = current_state

        sleep(0.05)

except KeyboardInterrupt:
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.cleanup()
