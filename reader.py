
import pandas as pd
import json
import hashlib
import logging
from pathlib import Path

# --------------------------------------------------
# 1. Project paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
DATASET_DIR = BASE_DIR / "olist_dataset"
MANIFEST_FILE = BASE_DIR / "manifest.json"

# --------------------------------------------------
# 2. Logging configuration
# --------------------------------------------------

LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(
            LOG_DIR / "pipeline.log",
            encoding="utf-8"
        ),
        logging.StreamHandler()
    ],
    force=True
)

logger = logging.getLogger("OlistPipeline")


# --------------------------------------------------
# 3. Generate SHA-256 file hash
# --------------------------------------------------

def calculate_file_hash(file_path):

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:

        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


# --------------------------------------------------
# 4. Load manifest
# --------------------------------------------------

def load_manifest():

    if not MANIFEST_FILE.exists():
        return {}

    try:
        with open(MANIFEST_FILE, "r", encoding="utf-8") as file:
            manifest = json.load(file)

        if not isinstance(manifest, dict):
            logger.warning("Invalid manifest format. Starting fresh.")
            return {}

        return manifest

    except json.JSONDecodeError:
        logger.warning("Manifest contains invalid JSON. Starting fresh.")
        return {}

    except OSError as error:
        logger.error(f"Could not read manifest: {error}")
        return {}


# --------------------------------------------------
# 5. Save manifest
# --------------------------------------------------

def save_manifest(manifest):

    try:
        with open(MANIFEST_FILE, "w", encoding="utf-8") as file:
            json.dump(manifest, file, indent=4)

        logger.info("Manifest updated successfully.")

    except OSError as error:
        logger.error(f"Could not save manifest: {error}")
        raise


# --------------------------------------------------
# 6. Read CSV files with idempotent processing
# --------------------------------------------------

def read_all_csvs():

    logger.info("Starting idempotent processing.")

    if not DATASET_DIR.exists():
        logger.error(f"Dataset folder not found: {DATASET_DIR}")
        return {}

    manifest = load_manifest()

    datasets = {}
    manifest_updated = False

    csv_files = sorted(DATASET_DIR.glob("*.csv"))

    if not csv_files:
        logger.warning("No CSV files found in the dataset folder.")
        return {}

    for file_path in csv_files:

        filename = file_path.name

        try:
            # Generate current file hash
            current_hash = calculate_file_hash(file_path)

            # Check whether file was already processed
            previous_record = manifest.get(filename, {})

            if (
                isinstance(previous_record, dict)
                and previous_record.get("status") == "processed"
                and previous_record.get("file_hash") == current_hash
            ):
                logger.info(f"Skipping unchanged file: {filename}")
                continue

            # Read CSV file
            logger.info(f"Processing file: {filename}")

            df = pd.read_csv(
                file_path,
                sep=None,
                engine="python",
                encoding="utf-8-sig"
            )

            # Store newly processed dataset
            datasets[file_path.stem] = df

            # Update manifest
            manifest[filename] = {
                "status": "processed",
                "file_hash": current_hash,
                "rows": len(df)
            }

            manifest_updated = True

            logger.info(
                f"Successfully processed {filename} "
                f"| Rows: {len(df)}"
            )

        except pd.errors.EmptyDataError:
            logger.error(f"Empty CSV file: {filename}")

        except pd.errors.ParserError:
            logger.exception(f"CSV parsing failed: {filename}")

        except UnicodeDecodeError:
            logger.exception(f"Encoding error in file: {filename}")

        except OSError:
            logger.exception(f"File access error: {filename}")

        except Exception:
            logger.exception(f"Unexpected error processing {filename}")

    # Save manifest after processing
    if manifest_updated:
        save_manifest(manifest)

    logger.info("CSV processing completed.")

    return datasets


# --------------------------------------------------
# 7. Main execution
# --------------------------------------------------

if __name__ == "__main__":

    datasets = read_all_csvs()

    print("\n---------- PROCESSING SUMMARY ----------")

    if datasets:
        for name, df in datasets.items():
            print(f"{name}: {len(df)} rows")

    else:
        print("No new or modified CSV files to process.")

    print("-----------------------------------------")
