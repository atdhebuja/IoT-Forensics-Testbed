#!/usr/bin/env python3
"""Index the selected Node 2 CSV evidence without changing the source files.

New repository support code; not the original live Node 2 event generator.
Naive source times stay naive. Output does not imply synchronized captures.
"""
import argparse
import csv
from datetime import datetime
import hashlib
import json
from pathlib import Path
import sys

SOURCES = (
    ('sensor-data/light_sensor.csv', 'uploaded-sensor-csv'),
    ('sensor-data/pir_motion_events.csv', 'uploaded-sensor-csv'),
    ('sensor-data/tamper_button_events.csv', 'uploaded-sensor-csv'),
    ('usb-events/usb_event_log.csv', 'uploaded-usb-csv'),
)
FIELDS = ('timestamp_raw', 'source_timezone', 'source_dataset', 'node_id',
          'event_type', 'source_file', 'source_csv_row', 'source_file_sha256',
          'details_json')


def sha256(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(65536), b''):
            digest.update(block)
    return digest.hexdigest()


def verify_manifest(root):
    payload = json.loads((root / 'manifest.json').read_text(encoding='utf-8'))
    for item in payload['files']:
        candidate = (root / item['path']).resolve()
        if not candidate.is_relative_to(root.resolve()):
            raise ValueError('Manifest path escapes evidence directory')
        if sha256(candidate) != item['sha256']:
            raise ValueError(f"Hash mismatch: {item['path']}")
    return len(payload['files'])


def collect(root):
    records = []
    for relative, capture in SOURCES:
        path = root / relative
        digest = sha256(path)
        with path.open(newline='', encoding='utf-8-sig') as stream:
            reader = csv.DictReader(stream)
            if not {'timestamp', 'event_type'}.issubset(reader.fieldnames or []):
                raise ValueError(f'Missing timestamp/event_type columns: {relative}')
            for row_number, row in enumerate(reader, 2):
                if None in row or any(v is None for v in row.values()):
                    raise ValueError(f'Malformed CSV row {row_number}: {relative}')
                stamp = row['timestamp']
                datetime.strptime(stamp, '%Y-%m-%d %H:%M:%S')
                records.append({
                    'timestamp_raw': stamp,
                    'source_timezone': 'unknown',
                    'source_dataset': capture,
                    'node_id': row.get('device_id') or 'PI5-NODE2',
                    'event_type': row['event_type'],
                    'source_file': relative,
                    'source_csv_row': row_number,
                    'source_file_sha256': digest,
                    'details_json': json.dumps(row, ensure_ascii=False, sort_keys=True),
                })
    records.sort(key=lambda r: (r['timestamp_raw'], r['source_file'], r['source_csv_row']))
    return records


def build(root, output):
    root, output = root.resolve(), output.resolve()
    if output.is_relative_to(root):
        raise ValueError('Write the derived index outside the evidence directory')
    records = collect(root)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open('w', newline='', encoding='utf-8') as stream:
        writer = csv.DictWriter(stream, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(records)
    return len(records)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, default=Path('examples/evidence'))
    parser.add_argument('--output', type=Path, default=Path('working/normalized-timeline.csv'))
    parser.add_argument('--verify-manifest', action='store_true')
    args = parser.parse_args()
    try:
        if args.verify_manifest:
            print(f'Verified {verify_manifest(args.input)} public sample artifacts')
        count = build(args.input, args.output)
    except (OSError, ValueError, KeyError, csv.Error) as error:
        print(f'ERROR: {error}', file=sys.stderr)
        return 1
    print(f'Indexed {count} CSV records into {args.output}')
    print('Raw local timestamps preserved; time zone and cross-capture clock agreement unknown.')
    print('event.log excluded from the merged index; no Node 1 measurements included.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
