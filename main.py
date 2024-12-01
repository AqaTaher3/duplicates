from compare_move import compare_and_move_files
from coppy_missing import copy_missing_files_to_source1


def main():
    folder1 = r"C:\Users\HP\Music\muzic"
    folder2 = r"C:\Users\HP\Music\music"
    output_folder = r"C:\Users\HP\Music\gadimi"

    # استفاده از تابع compare_and_move برای پردازش فایل‌ها
    compare_and_move_files(folder1, folder2, output_folder)

    # استفاده از تابع coppy_missing_files برای کپی فایل‌های گمشده
    copy_missing_files_to_source1(folder1, folder2, output_folder)


if __name__ == "__main__":
    main()
