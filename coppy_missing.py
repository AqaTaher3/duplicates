import os
import shutil

def copy_missing_files(src_dir, dest_dir):
    for root, dirs, files in os.walk(src_dir):
        rel_path = os.path.relpath(root, src_dir)
        dest_root = os.path.join(dest_dir, rel_path)

        if not os.path.exists(dest_root):
            os.makedirs(dest_root)

        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_root, file)

            if not os.path.exists(dest_file):
                shutil.copy2(src_file, dest_file)
                print(f"File copied: {src_file} -> {dest_file}")
            else:
                print(f"File already exists: {file}")

if __name__ == "__main__":
    src_folder1 = r"C:\Users\HP\Music\muzic"
    src_folder2 = r"C:\Users\HP\Music\music"
    copy_missing_files(src_folder2, src_folder1)
