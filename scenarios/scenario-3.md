# Scenario 3

Markdown transcription of the supplied DGFR 471 handout. The original Word file is [available here](original-documents/scenario-3.docx). These are exercise instructions; sample evidence in this repository is not a complete answer set.

Scenario 3: Distributed IoT Event Correlation

Distributed IoT Forensics Testbed Investigation

DGFR 471 IoT Forensics | Extra Project | Fall 2026 | Prepared by Prof. Dr. Atdhe Buja



| Scenario type | Distributed IoT Event Correlation |

| --- | --- |

| In-class time | 50 minutes |

| Work mode | Group investigation (3-4 students) |

| Report | Email the report to the instructor at abuja@commonwealthu.edu including the group name and the names of the students in the group. |

| Primary question | Can events from two independent IoT nodes be correlated to reconstruct a larger incident? |



Scenario Brief

Northstar Components uses two independent IoT nodes in the same demonstration area. Node 1 monitors environmental conditions, while Node 2 monitors physical activity around the equipment. A facilities alert showed an unusual environmental change during the same general period that Node 2 recorded physical-security events. Management wants to know whether the two evidence streams describe one larger incident or merely unrelated activity.

Your Mission

Correlate the instructor-provided Node 1 environmental evidence with Node 2 physical-security evidence. Construct a unified timeline, identify meaningful temporal relationships, and explain whether the evidence supports correlation. Distinguish correlation from causation.

Expected Evidence Sources

Node 1 environmental evidence exported by the instructor from the existing MySQL database for the assigned incident window.

Node 2 light, PIR motion, and tamper CSV evidence.

Node 2 master timeline: /mnt/iot-lab/node2/logs/event.log

Instructor-provided incident window and Node 1/Node 2 time-reference information.

50-Minute Testbed Workflow

Record the incident window and verify that the timestamps used by Node 1 and Node 2 can be compared. Ask the instructor if any time-zone/time-reference note applies.

Collect the instructor-provided Node 1 environmental export and document it in the evidence worksheet.

Locate and copy the relevant Node 2 sensor CSVs and event.log for the same incident window. Preserve originals and record hashes when practical.

Identify notable Node 1 temperature/humidity changes and their timestamps.

Identify relevant Node 2 light, motion, and tamper events and their timestamps.

Build one merged timeline containing evidence from both nodes. Clearly label the source of every entry.

Analyze which events are temporally related and whether the available evidence supports a reasonable relationship between them.

Capture 2-4 screenshots of the most important evidence and explicitly identify any claim that cannot be proven from the available artifacts.

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

Scenario-specific finding: provide a unified Node 1 + Node 2 timeline and explain whether the evidence supports a correlated incident, while clearly separating temporal correlation from causal claims.

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

What environmental change is visible in Node 1 evidence?

Which Node 2 physical events occur before, during, or after that change?

Are the timestamps directly comparable?

What alternative explanations could account for the apparent correlation?

Can the evidence prove that a physical action caused the environmental change?

Testbed Rules

The instructor operates and maintains the testbed. Do not disconnect sensors, power cables, storage, or networking equipment unless explicitly instructed.

Work from evidence copies/exports. Do not edit, delete, truncate, or overwrite original evidence files.

Record the assigned incident window before beginning analysis. The testbed may contain events from other groups or prior activity.

Do not assume that an event is malicious simply because it appears unusual. State what the evidence demonstrates and what remains uncertain.

Do not execute unknown USB payloads or attempt to modify the Raspberry Pi configuration.
