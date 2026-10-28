#!/usr/bin/env python3
"""
Start complete Node 2 IoT Forensics monitoring environment.

This launcher is intended to be stored at:
  /mnt/iot-lab/node2/scripts/start_node2_complete_monitoring.py

It starts the three sensor scripts located in:
  /home/pi/node2_scripts/

It also starts:
  /mnt/iot-lab/node2/scripts/node2_event_timeline.py
  /mnt/iot-lab/node2/scripts/usb_event_monitor.py

Sensor CSV output:
  /mnt/iot-lab/node2/sensor-data/

Master event timeline:
  /mnt/iot-lab/node2/logs/event.log

USB evidence:
  /mnt/iot-lab/usb-events/

Runtime logs:
  /mnt/iot-lab/node2/logs/

Stop:
  CTRL + C
"""

import os
import signal
import subprocess
import sys
import time
from pathlib import Path

HOME_SCRIPT_DIR = Path("/home/pi/node2_scripts")
SSD_SCRIPT_DIR = Path("/mnt/iot-lab/node2/scripts")
LOG_DIR = Path("/mnt/iot-lab/node2/logs")
USB_EVENTS_DIR = Path("/mnt/iot-lab/usb-events")

PROGRAMS = [
    {
        "name": "light_sensor",
        "path": HOME_SCRIPT_DIR / "light_sensor_ssd.py",
        "log": LOG_DIR / "light_sensor_runtime.log",
        "cwd": Path.home(),
    },
    {
        "name": "pir_motion",
        "path": HOME_SCRIPT_DIR / "pir_raw4_ssd.py",
        "log": LOG_DIR / "pir_motion_runtime.log",
        "cwd": Path.home(),
    },
    {
        "name": "tamper_button",
        "path": HOME_SCRIPT_DIR / "tamper_button_ssd.py",
        "log": LOG_DIR / "tamper_button_runtime.log",
        "cwd": Path.home(),
    },
    {
        "name": "master_event_timeline",
        "path": SSD_SCRIPT_DIR / "node2_event_timeline.py",
        "log": LOG_DIR / "master_event_timeline_runtime.log",
        "cwd": Path.home(),
    },
    {
        "name": "usb_event_monitor",
        "path": SSD_SCRIPT_DIR / "usb_event_monitor.py",
        "log": LOG_DIR / "usb_event_monitor_runtime.log",
        "cwd": Path.home(),
    },
]


def ensure_directories() -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    USB_EVENTS_DIR.mkdir(parents=True, exist_ok=True)


def check_files() -> bool:
    missing = []
    for program in PROGRAMS:
        if not program["path"].exists():
            missing.append(str(program["path"]))

    if missing:
        print("ERROR: These required script files were not found:")
        for item in missing:
            print(f"  - {item}")
        print("\nFix:")
        print("  1. Make sure sensor scripts are in: /home/pi/node2_scripts/")
        print("  2. Make sure node2_event_timeline.py is in: /mnt/iot-lab/node2/scripts/")
        print("  3. Make sure usb_event_monitor.py is in: /mnt/iot-lab/node2/scripts/")
        return False

    return True


def start_program(program: dict) -> subprocess.Popen:
    log_file = open(program["log"], "a", buffering=1)
    log_file.write(
        f"\n\n===== Starting {program['name']} at "
        f"{time.strftime('%Y-%m-%d %H:%M:%S')} =====\n"
    )

    process = subprocess.Popen(
        [sys.executable, str(program["path"])],
        cwd=str(program["cwd"]),
        stdout=log_file,
        stderr=subprocess.STDOUT,
        text=True,
        preexec_fn=os.setsid,
    )

    process._node2_log_file = log_file
    return process


def stop_programs(processes: list) -> None:
    print("\nStopping complete Node 2 monitoring environment...")

    for name, process in processes:
        if process.poll() is None:
            try:
                os.killpg(os.getpgid(process.pid), signal.SIGTERM)
                print(f"Stopped: {name}")
            except ProcessLookupError:
                pass

    time.sleep(2)

    for name, process in processes:
        if process.poll() is None:
            try:
                os.killpg(os.getpgid(process.pid), signal.SIGKILL)
                print(f"Force stopped: {name}")
            except ProcessLookupError:
                pass

        log_file = getattr(process, "_node2_log_file", None)
        if log_file:
            log_file.write(
                f"===== Stopped {name} at "
                f"{time.strftime('%Y-%m-%d %H:%M:%S')} =====\n"
            )
            log_file.close()


def print_summary() -> None:
    print("Complete Node 2 IoT Forensics monitoring environment is starting...\n")
    print("Sensor CSV evidence:")
    print("  /mnt/iot-lab/node2/sensor-data/")
    print("\nMaster timeline:")
    print("  /mnt/iot-lab/node2/logs/event.log")
    print("\nUSB evidence:")
    print("  /mnt/iot-lab/usb-events/usb_event_log.csv")
    print("  /mnt/iot-lab/usb-events/dmesg_usb_latest.txt")
    print("  /mnt/iot-lab/usb-events/journalctl_usb_latest.txt")
    print("\nRuntime logs:")
    print("  /mnt/iot-lab/node2/logs/")
    print("\nPress CTRL+C to stop all processes.\n")


def main() -> None:
    ensure_directories()

    if not check_files():
        sys.exit(1)

    print_summary()

    processes = []

    try:
        for program in PROGRAMS:
            process = start_program(program)
            processes.append((program["name"], process))
            print(f"Started {program['name']} | PID={process.pid}")
            time.sleep(1)

        while True:
            for name, process in processes:
                if process.poll() is not None:
                    print(
                        f"WARNING: {name} stopped unexpectedly "
                        f"with exit code {process.returncode}."
                    )
            time.sleep(5)

    except KeyboardInterrupt:
        stop_programs(processes)


if __name__ == "__main__":
    main()
