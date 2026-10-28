# Node 1 information to add

## Current owner-provided configuration

- Raspberry Pi 3, Ethernet connection to the laboratory router.
- DHT11 temperature/humidity sensor.
- MySQL storage for readings and environmental history.
- Timestamped measurements for correlation with Node 2.

## Needed for a reproducible release and dashboard integration

1. Acquisition script and exact DHT11 library/version.
2. Sensor wiring with the GPIO numbering scheme, voltage, pull-up requirements, and sampling interval.
3. MySQL host location, table definition (`CREATE TABLE` without credentials), units, and timestamp semantics.
4. Whether the Pi writes directly to MySQL or calls a gateway/API; provide that code if applicable.
5. A small export covering one documented incident window; exclude credentials and unrelated production data.
6. Operating-system and Python versions, launch method, clock/timezone configuration, and error handling.

For a future interchange export, proposed fields are `timestamp_raw`, `source_timezone`, `node_id`, `temperature_c`, and `humidity_percent`. These are proposed names, not a claim about the existing table schema. Do not rename or rewrite the operational database solely to match this proposal.
