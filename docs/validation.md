# Package validation

Prepared October 28, 2026.

- All local Markdown file/image links checked.
- All included Python sources parsed successfully.
- Supplied acquisition scripts preserved byte-for-byte against the source hashes.
- Five public evidence artifacts pass their SHA-256 manifest.
- Offline indexing yields 24 CSV records with original timestamps, source rows, and hashes.
- Four standard-library tests pass, including detection of modified evidence and refusal to write derived output into the evidence directory.
- Architecture PNG visually inspected; draw.io XML and SVG parse successfully.

No live Raspberry Pi GPIO, acquisition launcher, USB monitoring, MySQL connection, or web dashboard was tested. Two acquisition dependencies and Node 1 source are not in the release. The sample evidence is not a synchronized incident package.
