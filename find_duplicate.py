import os
import shutil
import hashlib
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm  # For progress bar


def calculate_file_hash(file_path):
    """Calculate the SHA-256 hash of a file."""
    BLOCK_SIZE = 65536  # 64 KB
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        buffer = f.read(BLOCK_SIZE)
        while len(buffer) > 0:
            hasher.update(buffer)
            buffer = f.read(BLOCK_SIZE)
    return hasher.hexdigest()


def ensure_directory_exists(directory):
    """Ensure the destination directory exists, create it if necessary."""
    os.makedirs(directory, exist_ok=True)


def find_and_remove_duplicates(source_folder, destination_folder):
    """Find and move duplicate files to the destination folder."""
    ensure_directory_exists(destination_folder)
    seen_files = set()
    transferred_files = set()

    # Collect all files
    files = [os.path.join(root, file) for root, _, files in os.walk(source_folder) for file in files]
    total_files = len(files)

    def process_file(file_path):
        """Process a single file: check for duplicates and move if needed."""
        file_hash = calculate_file_hash(file_path)
        if file_hash in seen_files:
            base_name, extension = os.path.splitext(os.path.basename(file_path))
            duplicate_destination = os.path.join(destination_folder, f"{base_name}_{file_hash[:6]}{extension}")
            if file_path not in transferred_files:
                try:
                    shutil.move(file_path, duplicate_destination)
                    print(f"File moved: {file_path} -> {duplicate_destination}")
                    transferred_files.add(file_path)
                except PermissionError as e:
                    print(f"Unable to move file {file_path}: {e}")
        else:
            seen_files.add(file_hash)

    # Process files with progress bar
    with ThreadPoolExecutor() as executor, tqdm(total=total_files, desc="Processing files") as pbar:
        for file_path in files:
            executor.submit(process_file, file_path)
            pbar.update(1)


if __name__ == "__main__":
    source_folder = r"C:\Users\HP\Music\muzic"
    destination_folder = r"C:\Users\HP\Music\duplicate"
    find_and_remove_duplicates(source_folder, destination_folder)
