# Node 2 setup and reproducibility notes

## Supplied original files

All four Python files under `src/node2/original/` are byte-for-byte copies of the owner uploads. This repository does not silently replace the working laboratory versions.

| Script | Hardware and behavior | Output |
| --- | --- | --- |
| `light_sensor_ssd.py` | Physical BOARD pin 7, equivalent to BCM GPIO4; RC timing loop; threshold 1200 | `light_sensor.csv` |
| `pir_raw4_ssd.py` | BCM GPIO23; logs state transitions | `pir_motion_events.csv` |
| `tamper_button_ssd.py` | BCM GPIO17 button, pull-up; BCM GPIO27 indicator LED | `tamper_button_events.csv` |
| `start_node2_complete_monitoring.py` | Starts the sensor scripts plus timeline and USB processes | Runtime logs and child-process outputs |

## Missing dependencies

The original launcher requires:

- `/mnt/iot-lab/node2/scripts/node2_event_timeline.py` — not supplied.
- `/mnt/iot-lab/node2/scripts/usb_event_monitor.py` — not supplied.

The old launcher readme names a USB monitor as included, but the actual upload does not contain that file. The launcher checks all required files and exits if any are missing. A sample event log or USB CSV cannot substitute for executable source.

## Confirm the actual Raspberry Pi environment

Record Raspberry Pi OS version, Python version, GPIO backend and version, filesystem type, SSD mount options, user permissions, sensor circuit details, and timezone. The original sensor files import `RPi.GPIO`. Pi 5 requires a compatible implementation; `rpi-lgpio` is one documented compatibility route. Do not install it over a working environment without first recording that environment. `rpi-lgpio` and the original `rpi-gpio` package must not coexist in the same Python environment. Reference: https://rpi-lgpio.readthedocs.io/en/latest/install.html

The light script uses RC timing and does not report calibrated lux. Its circuit needs documented resistance/capacitance and calibration observations. Do not infer a complete circuit from the Python file. Capture the existing working wiring, including common ground and sensor voltage requirements, before attempting reproduction.

## Preserve the legacy path layout

The original scripts use absolute paths. After confirming that the SSD is correctly mounted at `/mnt/iot-lab`, prepare writable directories for your laboratory account:

```bash
mountpoint /mnt/iot-lab
mkdir -p /home/pi/node2_scripts
mkdir -p /mnt/iot-lab/node2/scripts /mnt/iot-lab/node2/sensor-data /mnt/iot-lab/node2/logs /mnt/iot-lab/usb-events
cp src/node2/original/light_sensor_ssd.py /home/pi/node2_scripts/
cp src/node2/original/pir_raw4_ssd.py /home/pi/node2_scripts/
cp src/node2/original/tamper_button_ssd.py /home/pi/node2_scripts/
cp src/node2/original/start_node2_complete_monitoring.py /mnt/iot-lab/node2/scripts/
```

Run `mountpoint` first and continue only if it succeeds; directory existence alone does not prove the SSD is mounted. Do not format a disk as part of these steps. Replace `/home/pi` in the launcher if the actual account differs. The missing timeline and USB scripts must be restored before launching the complete suite:

```bash
python3 /mnt/iot-lab/node2/scripts/start_node2_complete_monitoring.py
```

## Issues to address before calling this a turnkey release

- The light RC loop has no timeout; a disconnected/faulty circuit may block it.
- The tamper script has no explicit button debounce and only cleans up on KeyboardInterrupt.
- The launcher sends SIGTERM to children, while the original scripts do not all handle that signal for GPIO cleanup.
- The launcher creates directories but does not verify the SSD mount, and it repeatedly warns about a stopped child without restarting or exiting.
- Local timestamps omit timezone offsets; multiple simultaneous writers and clock adjustments need documented treatment.
- GPIO compatibility, wiring, and actual hardware behavior were not tested in the repository preparation environment.

These are documented findings, not changes applied to the original acquisition scripts. Preserve the current working lab before refactoring.
