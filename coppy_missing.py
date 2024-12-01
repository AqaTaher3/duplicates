# coppy_missing.py
import os
from compare_move import compare_and_move_files

def coppy_missing_files(folder1, folder2, output_folder):
    """
    بررسی فایل‌های تکراری در دو فولدر و انتقال یا کپی آنها پس از تأیید کاربر.
    """
    # اطمینان از اینکه فولدر مقصد وجود دارد
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # دریافت فایل‌های فولدر اول و دوم
    files1 = os.listdir(folder1)
    files2 = os.listdir(folder2)

    # بررسی فایل‌های تکراری
    for file in files1:
        if file in files2:
            path1 = os.path.join(folder1, file)
            path2 = os.path.join(folder2, file)

            # بررسی مسیر نسبی از ریشه فولدرها
            rel_path1 = os.path.relpath(path1, folder1)
            rel_path2 = os.path.relpath(path2, folder2)

            # اگر مسیر نسبی یکسان باشد (با توجه به اینکه در همان دایرکتوری هستند)، پردازش نشوند
            if rel_path1 == rel_path2:
                continue

            # فراخوانی تابع مقایسه و انتقال فایل
            compare_and_move_files(path1, path2, output_folder)
