# Scenario 2

Markdown transcription of the supplied DGFR 471 handout. The original Word file is [available here](original-documents/scenario-2.docx). These are exercise instructions; sample evidence in this repository is not a complete answer set.

Scenario 2: Unauthorized USB / Removable Media Activity

Distributed IoT Forensics Testbed Investigation

DGFR 471 IoT Forensics | Extra Project | Fall 2026 | Prepared by Prof. Dr. Atdhe Buja



| Scenario type | Unauthorized USB / Removable Media Activity |

| --- | --- |

| In-class time | 50 minutes |

| Work mode | Group investigation (3-4 students) |

| Report | Email the report to the instructor at abuja@commonwealthu.edu including the group name and the names of the students in the group. |

| Primary question | Was an unauthorized USB device connected, when, and what evidence supports that conclusion? |



Scenario Brief

A maintenance contractor visited the Northstar Components IoT demonstration cell. After the visit, the operations team noticed that a removable storage device may have been connected to the physical-security monitoring node. The contractor says the device was only used for legitimate maintenance, but the security team has no approved work order documenting the connection. Your group must determine what the Raspberry Pi can actually prove about the removable-media activity.

Your Mission

Establish whether removable USB storage was connected to Node 2, identify the available characteristics of the device, reconstruct insertion/removal activity, and correlate the USB evidence with any relevant physical-access events. Do not claim file copying or malicious execution unless the available evidence supports it.

Expected Evidence Sources

USB event CSV: /mnt/iot-lab/usb-events/usb_event_log.csv

Kernel evidence export: /mnt/iot-lab/usb-events/dmesg_usb_latest.txt

Journal kernel export: /mnt/iot-lab/usb-events/journalctl_usb_latest.txt

USB monitor runtime log: /mnt/iot-lab/usb-events/usb_monitor_runtime.log

Node 2 master timeline and PIR/tamper evidence when relevant to the assigned incident window.

50-Minute Testbed Workflow

Record the incident window provided by the instructor and assign group roles.

Identify the USB/removable-media evidence directory. Do not insert or remove any device unless the instructor tells you to do so.

Locate usb_event_log.csv, dmesg_usb_latest.txt, journalctl_usb_latest.txt, and the USB monitor runtime log. Note file metadata before copying.

Copy the relevant artifacts to your group evidence location and document them in the evidence worksheet. Calculate/record SHA-256 hashes when practical.

Search the evidence within the assigned time window for USB insertion, storage-device discovery, block-device assignment, vendor/product information, and disconnection/removal.

If instructed, compare the USB timestamps with Node 2 PIR/tamper/master-timeline evidence to determine whether physical activity occurred near the connection event.

Build a preliminary timeline that distinguishes detection, device assignment, and removal/disconnect events.

Capture 2-4 screenshots showing the strongest evidence and record what the artifacts cannot establish (for example, file-copy activity if no supporting evidence exists).

Your group should leave the testbed session with enough preserved evidence and notes to complete the remaining analysis outside class.

Evidence Collection Worksheet

Complete this during the 50-minute testbed session. Use one row per evidence item or artifact copied/recorded.



| Evidence ID | Source / Node | Artifact / File | Relevant Time | SHA-256 / Integrity Note | Why Relevant |

| --- | --- | --- | --- | --- | --- |

|  |  |  |  |  |  |

|  |  |  |  |  |  |

|  |  |  |  |  |  |

|  |  |  |  |  |  |

|  |  |  |  |  |  |

|  |  |  |  |  |  |



Required Deliverables

Group forensic report (recommended 3-5 pages, excluding appendices) describing the incident, evidence examined, analysis, findings, and limitations.

Completed evidence collection worksheet identifying each artifact used in the investigation.

Incident timeline showing the relevant events in chronological order and citing the evidence source for each event.

Evidence package containing copies/exports of the artifacts your group relied upon. Do not modify the original evidence.

At least 2-4 clearly labeled screenshots or photographs supporting your analysis.

Scenario-specific finding: identify the removable device as precisely as the evidence permits and explain the supported insertion/removal timeline without overstating what occurred on the device.

Short conclusion that separates what the evidence supports from what cannot be determined from the available evidence.

Evaluation Guide (100 points)



| Category | Points | What is evaluated |

| --- | --- | --- |

| Evidence collection & preservation | 20 | Relevant artifacts collected; originals preserved; integrity documented. |

| Timeline reconstruction | 20 | Accurate chronology with evidence source references. |

| Forensic analysis | 25 | Reasoned interpretation supported by artifacts rather than assumptions. |

| Scenario-specific findings | 20 | Correctly addresses the primary forensic question for the assigned scenario. |

| Conclusion & limitations | 10 | Clear conclusion and appropriate statement of uncertainty/limitations. |

| Professional presentation | 5 | Organization, readability, screenshots, labeling, and submission quality. |



Questions to Guide Your Analysis

What device identifiers or characteristics are available?

What block device was assigned (for example, /dev/sdb or /dev/sdc)?

Can you establish insertion and removal times from more than one artifact?

What does the evidence not tell you about the contents or actions performed using the USB device?

Testbed Rules

The instructor operates and maintains the testbed. Do not disconnect sensors, power cables, storage, or networking equipment unless explicitly instructed.

Work from evidence copies/exports. Do not edit, delete, truncate, or overwrite original evidence files.

Record the assigned incident window before beginning analysis. The testbed may contain events from other groups or prior activity.

Do not assume that an event is malicious simply because it appears unusual. State what the evidence demonstrates and what remains uncertain.

Do not execute unknown USB payloads or attempt to modify the Raspberry Pi configuration.
