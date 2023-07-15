import os
import hashlib

def calculate_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()

def scan_directory(directory):
    for root, _, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_hash = calculate_hash(file_path)
            print(f"File: {file_path} - Hash: {file_hash}")

directory_to_scan = "C:/Path/To/Directory"
scan_directory(directory_to_scan)
