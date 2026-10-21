import os
import csv
import hashlib
import time

INTEGRITY_TABLE = "integrity_table.csv"
BACKUP_FOLDER = "backup"
FOLDER = "files"


def append_integrity_file(file_path: str, hash_value: str, timestamp: str):
    file_exists = (
        os.path.exists(INTEGRITY_TABLE) and os.path.getsize(INTEGRITY_TABLE) > 0
    )
    with open(INTEGRITY_TABLE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["file_path", "sha256_digest", "timestamp"])
        writer.writerow([file_path, hash_value, timestamp])


def calculate_hash(file_path: str) -> str:
    with open(file_path, "rb") as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()
    return file_hash


def get_current_timestamp() -> str:
    return str(time.time())
