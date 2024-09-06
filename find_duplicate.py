import os
import shutil
import hashlib
from concurrent.futures import ThreadPoolExecutor

def calculate_file_hash(file_path):
    BLOCK_SIZE = 65536  # 64 KB
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        buffer = f.read(BLOCK_SIZE)
        while len(buffer) > 0:
            hasher.update(buffer)
            buffer = f.read(BLOCK_SIZE)
    return hasher.hexdigest()

def find_and_remove_duplicates(source_folder, destination_folder):
    seen_files = set()
    transferred_files = set()  

    total_files = sum(len(files) for _, _, files in os.walk(source_folder))
    files_processed = 0

    def process_file(file_path):
        nonlocal files_processed
        file_hash = calculate_file_hash(file_path)
        if file_hash in seen_files:
            duplicate_destination = os.path.join(destination_folder, os.path.basename(file_path))
            if file_path not in transferred_files:
                try:
                    shutil.copy2(file_path, duplicate_destination)
                    transferred_files.add(file_path)
                    print(f"Duplicate file transferred: {file_path} -> {duplicate_destination}")
                except PermissionError as e:
                    print(f"Unable to copy file: {e}")
        else:
            seen_files.add(file_hash)
        files_processed += 1
        progress = (files_processed / total_files) * 100
        print(f"Progress: {progress:.2f}% ({files_processed}/{total_files} files processed)", end='\r')

    with ThreadPoolExecutor() as executor:
        for root, dirs, files in os.walk(source_folder):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                executor.submit(process_file, file_path)



if __name__ == "__main__":
    source_folder = r"F:\New folder (2)\New folder"
    destination_folder = r"F:\New folder (2)\New folder\dup"
    find_and_remove_duplicates(source_folder, destination_folder)

