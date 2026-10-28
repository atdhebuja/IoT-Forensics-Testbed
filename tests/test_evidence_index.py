"""Offline checks for evidence preservation and provenance; no GPIO access."""
import csv
import importlib.util
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('evidence_index', ROOT/'tools/build_evidence_index.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class EvidenceIndexTests(unittest.TestCase):
    def test_public_snapshot_hashes(self):
        self.assertEqual(module.verify_manifest(ROOT/'examples/evidence'), 5)

    def test_source_rows_and_unknown_timezone_are_preserved(self):
        source = ROOT/'examples/evidence'
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp)/'index.csv'
            self.assertEqual(module.build(source, out), 24)
            with out.open() as stream:
                rows = list(csv.DictReader(stream))
            self.assertEqual(rows[0]['timestamp_raw'], '2026-06-04 09:14:14')
            self.assertEqual(rows[-1]['timestamp_raw'], '2026-06-04 10:25:43')
            self.assertTrue(all(r['source_timezone'] == 'unknown' for r in rows))
            self.assertTrue(all(r['source_file'].endswith('.csv') for r in rows))
            for r in rows:
                self.assertEqual(r['source_file_sha256'], module.sha256(source/r['source_file']))
            self.assertEqual(module.verify_manifest(source), 5)

    def test_refuses_to_write_into_evidence(self):
        source = ROOT/'examples/evidence'
        with self.assertRaises(ValueError):
            module.build(source, source/'should-not-write.csv')

    def test_modified_artifact_fails_integrity_check(self):
        with tempfile.TemporaryDirectory() as temp:
            dest=Path(temp)/'evidence'
            shutil.copytree(ROOT/'examples/evidence',dest)
            with (dest/'sensor-data/light_sensor.csv').open('a') as f:
                f.write('changed\n')
            with self.assertRaises(ValueError): module.verify_manifest(dest)


if __name__ == '__main__': unittest.main()
