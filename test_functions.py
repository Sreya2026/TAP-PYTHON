
import unittest
import tempfile
import json
from pathlib import Path
from unittest.mock import patch

import reader


class TestOlistPipeline(unittest.TestCase):

    # Test 1: Same file content should generate the same hash
    def test_same_file_hash(self):

        with tempfile.TemporaryDirectory() as temp_dir:

            file_path = Path(temp_dir) / "test.csv"
            file_path.write_text("id,name\n1,Ana\n", encoding="utf-8")

            hash1 = reader.calculate_file_hash(file_path)
            hash2 = reader.calculate_file_hash(file_path)

            self.assertEqual(hash1, hash2)

    # Test 2: Different file content should generate different hashes
    def test_different_file_hash(self):

        with tempfile.TemporaryDirectory() as temp_dir:

            file1 = Path(temp_dir) / "file1.csv"
            file2 = Path(temp_dir) / "file2.csv"

            file1.write_text("id,name\n1,Ana\n", encoding="utf-8")
            file2.write_text("id,name\n2,John\n", encoding="utf-8")

            hash1 = reader.calculate_file_hash(file1)
            hash2 = reader.calculate_file_hash(file2)

            self.assertNotEqual(hash1, hash2)

    # Test 3: Missing manifest should return an empty dictionary
    def test_load_missing_manifest(self):

        with tempfile.TemporaryDirectory() as temp_dir:

            manifest_path = Path(temp_dir) / "manifest.json"

            with patch.object(reader, "MANIFEST_FILE", manifest_path):

                result = reader.load_manifest()

                self.assertEqual(result, {})

    # Test 4: Manifest should save and load correctly
    def test_save_and_load_manifest(self):

        with tempfile.TemporaryDirectory() as temp_dir:

            manifest_path = Path(temp_dir) / "manifest.json"

            sample_manifest = {
                "customers.csv": {
                    "status": "processed",
                    "file_hash": "abc123",
                    "rows": 500
                }
            }

            with patch.object(reader, "MANIFEST_FILE", manifest_path):

                reader.save_manifest(sample_manifest)
                result = reader.load_manifest()

                self.assertEqual(result, sample_manifest)

    # Test 5: Invalid JSON should return an empty dictionary
    def test_invalid_manifest(self):

        with tempfile.TemporaryDirectory() as temp_dir:

            manifest_path = Path(temp_dir) / "manifest.json"
            manifest_path.write_text("{invalid json", encoding="utf-8")

            with patch.object(reader, "MANIFEST_FILE", manifest_path):

                result = reader.load_manifest()

                self.assertEqual(result, {})

    # Test 6: CSV should be processed once and skipped when unchanged
    def test_idempotent_csv_processing(self):

        with tempfile.TemporaryDirectory() as temp_dir:

            dataset_dir = Path(temp_dir) / "olist_dataset"
            dataset_dir.mkdir()

            manifest_path = Path(temp_dir) / "manifest.json"

            csv_path = dataset_dir / "customers.csv"

            csv_path.write_text(
                "customer_id,customer_city\n"
                "1,Palakkad\n"
                "2,Coimbatore\n",
                encoding="utf-8"
            )

            with patch.object(reader, "DATASET_DIR", dataset_dir), \
                 patch.object(reader, "MANIFEST_FILE", manifest_path):

                # First run: CSV should be processed
                first_result = reader.read_all_csvs()

                self.assertIn("customers", first_result)
                self.assertEqual(len(first_result["customers"]), 2)

                # Check manifest was created
                self.assertTrue(manifest_path.exists())

                # Second run: unchanged CSV should be skipped
                second_result = reader.read_all_csvs()

                self.assertEqual(second_result, {})


if __name__ == "__main__":
    unittest.main(verbosity=2)
