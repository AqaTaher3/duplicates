# find_duplicate.py
import os
from coppy_missing import coppy_missing_files


def find_duplicates_in_folder(folder, output_folder):
    """
    پیدا کردن فایل‌های تکراری در یک فولدر و ارسال برای پردازش.
    """
    files = os.listdir(folder)  # گرفتن لیست فایل‌ها در فولدر
    files_paths = [os.path.join(folder, file) for file in files]  # دریافت مسیر کامل هر فایل

    # بررسی هر فایل با سایر فایل‌ها
    for i, file1 in enumerate(files_paths):
        for file2 in files_paths[i+1:]:  # مقایسه هر فایل با فایل‌های بعدی
            if os.path.basename(file1) == os.path.basename(file2):  # اگر نام فایل‌ها مشابه باشند
                # فراخوانی تابع برای پردازش فایل‌های تکراری
                coppy_missing_files(file1, file2, output_folder)

if __name__ == "__main__":
    folder = r"C:\Users\HP\Music\muzic"  # فولدر مورد نظر
    output_folder = r"C:\Users\HP\Music\gadimi"  # پوشه مقصد برای فایل‌ها

    # استفاده از تابع برای پیدا کردن فایل‌های تکراری و پردازش آنها
    find_duplicates_in_folder(folder, output_folder)
