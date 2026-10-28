# Remaining work

## Required to reproduce the existing acquisition stack

- [ ] Add original `node2_event_timeline.py`.
- [ ] Add original `usb_event_monitor.py`.
- [ ] Record actual Pi OS, Python, and GPIO backend/version.
- [ ] Add verified wiring and component values, including the light RC circuit and tamper LED resistor.
- [ ] Confirm Node 1 DHT11 configuration, acquisition script, MySQL host/schema, and export method.
- [ ] Document SSD filesystem, stable mounting, permissions, and launch behavior.
- [ ] Document timezones, clock synchronization, and incident windows.

## Evidence and teaching completeness

- [ ] Add one complete, matched Node 1/Node 2 evidence package for Scenario 3.
- [ ] Add scenario ground truth and an anonymized example report, keeping instructor answers separate if desired.
- [ ] Add screenshots of the actual collection process, wiring, and data views.
- [ ] Decide artifact-specific reuse terms for code, course materials, sample data, and photographs.

## Planned dashboard

- [ ] Confirm the Node 1 storage interface and choose a dashboard host.
- [ ] Implement read-only adapters and preserve provenance in the normalized schema.
- [ ] Implement local browser views and test known incidents.
- [ ] Prepare a separately hosted static/public demonstration using selected data if desired.

## Optional acquisition hardening

Mount verification; calibrated light thresholds; bounded RC measurement; button debounce; signal-aware GPIO cleanup; child-process failure handling; explicit timestamps with offsets; capture rotation; stable source identifiers.
