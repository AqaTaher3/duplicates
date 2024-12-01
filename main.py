from compare_move import compare_and_move, coppy_missing_files  # Import the functions from file_operations
from find_duplicate import find_duplicates_in_folder
from coppy_missing import coppy_missing_files
from grafical import show_prompt, show_end_message  # Importing the graphical functions
import os


def main():
    folder1 = r"C:\Users\HP\Music\muzic"
    folder2 = r"C:\Users\HP\Music\music"
    output_folder = r"C:\Users\HP\Music\gadimi"

    # استفاده از تابع compare_and_move برای پردازش فایل‌ها
    compare_and_move(folder1, folder2, output_folder)

    # استفاده از تابع coppy_missing_files برای کپی فایل‌های گمشده
    coppy_missing_files(folder1, folder2, output_folder)

    find_duplicates_in_folder(folder1, output_folder)


if __name__ == "__main__":
    main()
