# Evidence provenance and interpretation

## Included artifacts

| Artifact | Provenance | Treatment |
| --- | --- | --- |
| Three sensor CSVs | Uploaded `sensor-data.zip` | Copied unchanged |
| `logs/event.log` | Uploaded `logs.zip` | Copied unchanged; already a derived timeline |
| `usb_event_log.csv` | Uploaded `usb-events.zip` | Serial field and nonempty mount-point identifiers replaced for public distribution |
| `manifest.json` | Generated during repository assembly | SHA-256 hashes of the public sample files, not of unseen original acquisitions |
| `tools/build_evidence_index.py` | Newly prepared repository utility | Offline indexing; not the missing live timeline generator |

The original raw kernel/journal exports contain hardware serial-related records, MAC addresses, and filesystem identifiers. They are not included in this public package. They remain in the supplied archives outside this repository. If released later, create explicitly labeled redacted copies and document each transformation. Runtime wrapper logs contain limited start/stop information and are omitted here.

## Time and completeness

All provided CSV timestamps are naive local strings without an offset. Their timezone and clock synchronization cannot be recovered from the data alone. Preserve them as `timestamp_raw`; do not silently convert them to UTC. Cross-node correlation needs the timezone, incident window, and measured/documented clock relationship for both nodes.

The sensor CSV capture is approximately 09:14–09:15 on June 4, 2026; `event.log` is approximately 10:03–10:04; the USB CSV is approximately 10:25. These are separate uploaded windows. This package does not establish they form one incident or align with the three exercise scenarios.

USB samples include both a disk and its partition. Four rows do not necessarily mean four physical USB interactions. Insertion does not prove file copying, HID execution, authorization, or malicious intent.

PIR indicates a sensor state, not an identified person. A button event indicates activation of the configured circuit, not proof of malicious tampering. Light values are uncalibrated RC timing counts, not lux. Claims about log deletion need independent evidence of deletion; gaps alone are insufficient.

## Integrity workflow

Preserve original exports outside the public repository, record incident scope and collection time, hash exported files, analyze working copies, and link findings to the specific artifact and row. Hashes demonstrate later byte consistency with a recorded snapshot; they do not establish authenticity or chain of custody by themselves. Freeze/export a copy before hashing actively written files.

The offline index preserves filename and row references and includes the SHA-256 hash of each input CSV. It sorts comparable-looking raw local timestamps only for browsing; it cannot prove clock agreement or an incident sequence across captures. No Node 1 data is fabricated.
