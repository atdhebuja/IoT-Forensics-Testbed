# Browser dashboard plan

## Can the two-node data be viewed through a link?

Yes. Host a small read-only web application on a laboratory computer, VM, or Raspberry Pi reachable by the students. An example address would be `http://<dashboard-host>:8000` on the laboratory network; this is an example, not a deployed link. A local HDMI display could open the same URL in a browser. A public portfolio demonstration should use selected exported data and be hosted separately from live collection.

## Recommended integration

1. Preserve the existing acquisition scripts and original evidence.
2. Add a read-only Node 1 adapter for the confirmed MySQL schema, using a separate database account with SELECT-only access.
3. Add a Node 2 adapter that reads sensor CSVs, USB CSVs, and the Node 2 event log from snapshots or read-only paths. Treat derived timeline entries as derived, not independent events.
4. Normalize source node, event category, raw timestamp, timezone if known, evidence path, row/line number, and source hash. Retain the original record alongside normalized fields.
5. Serve a read-only API and browser interface from a shared laboratory host. A practical implementation choice is Python FastAPI with a small HTML/JavaScript frontend; these components are proposed and are not included as implemented code.
6. Restrict live access to the lab or authenticated university access. A public demo can show a curated snapshot without direct database or sensor access.

## Views

- Environmental measurements: temperature and humidity history with units.
- Physical events: motion, light-state readings, and tamper activity.
- USB activity: insertion/removal with disk/partition grouping.
- Combined timeline: filters by node, capture, evidence source, and incident window.
- Evidence details: original row/line, source file hash, collection context, and known limitations.
- Acquisition status: last observation and stale/missing feed indicators, separate from historical evidence.

## Acceptance criteria

- A browser on the intended student network can open the URL.
- Views read copied or read-only evidence and never modify source files.
- Unknown timezone remains visibly unknown; normalized UTC is used only when a source timezone is explicitly confirmed.
- Every event links to its source artifact and row/line reference.
- Disk and partition records are not automatically counted as separate physical devices.
- Node 1 fields, units, and time semantics are tested against a real export.
- A known controlled incident is reconstructed accurately before claiming cross-node correlation works.
- Public snapshot views are labeled with collection dates and never presented as live telemetry.

GitHub Pages can host an exported static demo, but cannot run a Python backend or directly connect to the live MySQL database. See https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site .
