# compare_move.py
import os
import shutil
from grafical import show_prompt

def compare_and_move_files(file1, file2, output_folder):
    """
    مقایسه دو فایل و انتقال یکی از آنها به پوشه مقصد
    """
    def calculate_file_hash(file_path):
        """محاسبه هش SHA-256 یک فایل"""
        import hashlib
        BLOCK_SIZE = 65536  # 64 KB
        hasher = hashlib.sha256()
        with open(file_path, 'rb') as f:
            buffer = f.read(BLOCK_SIZE)
            while len(buffer) > 0:
                hasher.update(buffer)
                buffer = f.read(BLOCK_SIZE)
        return hasher.hexdigest()

    file_hash1 = calculate_file_hash(file1)
    file_hash2 = calculate_file_hash(file2)

    # اگر هش‌ها برابر باشند، یعنی فایل‌ها مشابه هستند
    if file_hash1 == file_hash2:
        return

    # نمایش پنجره گرافیکی برای انتخاب فایل
    show_prompt(file1, file1, file2, output_folder)
