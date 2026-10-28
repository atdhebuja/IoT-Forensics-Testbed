Complete Node 2 Launcher - Setup

Files included:
  start_node2_complete_monitoring.py
  usb_event_monitor.py

Required existing files:
  /home/pi/node2_scripts/light_sensor_ssd.py
  /home/pi/node2_scripts/pir_raw4_ssd.py
  /home/pi/node2_scripts/tamper_button_ssd.py
  /mnt/iot-lab/node2/scripts/node2_event_timeline.py

Install:

  cp start_node2_complete_monitoring.py /mnt/iot-lab/node2/scripts/
  cp usb_event_monitor.py /mnt/iot-lab/node2/scripts/

  chmod +x /mnt/iot-lab/node2/scripts/start_node2_complete_monitoring.py
  chmod +x /mnt/iot-lab/node2/scripts/usb_event_monitor.py

Run:

  python3 /mnt/iot-lab/node2/scripts/start_node2_complete_monitoring.py

This starts:
  1. Light sensor monitoring
  2. PIR motion monitoring
  3. Tamper button monitoring
  4. Master event timeline generator
  5. USB event monitor

Evidence output:

  /mnt/iot-lab/node2/sensor-data/
  /mnt/iot-lab/node2/logs/event.log
  /mnt/iot-lab/usb-events/usb_event_log.csv
  /mnt/iot-lab/usb-events/dmesg_usb_latest.txt
  /mnt/iot-lab/usb-events/journalctl_usb_latest.txt

Stop:

  CTRL + C
