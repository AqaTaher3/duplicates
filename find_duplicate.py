import os
import hashlib
from grafical import show_prompt, show_end_message


def calculate_file_hash(file_path):
    """محاسبه هش SHA-256 یک فایل"""
    BLOCK_SIZE = 65536  # اندازه بلوک 64 KB
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        buffer = f.read(BLOCK_SIZE)
        while len(buffer) > 0:
            hasher.update(buffer)
            buffer = f.read(BLOCK_SIZE)
    return hasher.hexdigest()


def find_duplicate(folder, output_folder):
    """پیدا کردن فایل‌های تکراری در یک فولدر و پردازش آنها"""

    seen_files = {}  # دیکشنری برای نگهداری هش فایل‌ها
    total_files = 0  # تعداد فایل‌ها

    # جمع‌آوری فایل‌ها از پوشه مشخص‌شده
    files = [os.path.join(root, file) for root, _, files in os.walk(folder) for file in files]
    total_files = len(files)

    for file_path in files:
        file_hash = calculate_file_hash(file_path)  # محاسبه هش فایل

        if file_hash in seen_files:
            original_file = seen_files[file_hash]
            duplicate_file = file_path

            # نمایش پنجره گرافیکی برای انتخاب فایل
            show_prompt(original_file, duplicate_file, output_folder)

        else:
            seen_files[file_hash] = file_path  # ذخیره مسیر فایل برای هش‌های جدید

    # نمایش پیام پایان عملیات
    show_end_message()


if __name__ == "__main__":
    folder = r"C:\Users\HP\Music\muzic"  # پوشه‌ای که فایل‌ها از آن بررسی می‌شود
    output_folder = r"C:\Users\HP\Music\gadimi"  # پوشه مقصد برای انتقال فایل‌ها

    # فراخوانی تابع برای پیدا کردن و پردازش فایل‌های تکراری
    find_duplicate(folder, output_folder)
