import os
from grafical import show_prompt, show_end_message  # وارد کردن توابع گرافیکی از فایل گرافیکال


def copy_missing_files_to_source1(folder1, folder2, output_folder):
    """
    بررسی فایل‌های موجود در فولدر 2 که در فولدر 1 وجود ندارند و کپی آنها به فولدر 1
    """

    # اطمینان از اینکه فولدر مقصد وجود دارد
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # دریافت فایل‌ها از فولدر اول و دوم
    files2 = os.listdir(folder2)

    # بررسی فایل‌هایی که در فولدر 2 هستند اما در فولدر 1 وجود ندارند
    for file in files2:
        path2 = os.path.join(folder2, file)

        # اگر فایل یک پوشه است، باید در داخل آن گشت بزنیم
        if os.path.isdir(path2):
            # اگر فایل پوشه باشد، باید این پوشه و فایل‌های آن را بررسی کنیم
            for root, dirs, files in os.walk(path2):
                # مسیر نسبی به فولدر 2
                rel_path = os.path.relpath(root, folder2)
                # مسیری معادل در فولدر 1
                dest_path = os.path.join(folder1, rel_path)

                # اگر پوشه مقصد وجود نداشت، آن را بسازیم
                if not os.path.exists(dest_path):
                    os.makedirs(dest_path)

                # بررسی فایل‌های داخل این پوشه
                for file in files:
                    file_path2 = os.path.join(root, file)
                    file_dest = os.path.join(dest_path, file)

                    # اگر فایل در فولدر 1 موجود نباشد، از کاربر بخواهیم که آن را منتقل کند
                    if not os.path.exists(file_dest):
                        show_prompt(file, file_path2, file_dest, output_folder)

        else:
            # اگر فایل یک فایل معمولی باشد و در فولدر 1 وجود نداشته باشد، از کاربر بخواهیم که آن را منتقل کند
            file_path2 = os.path.join(folder2, file)
            file_dest = os.path.join(folder1, file)

            if not os.path.exists(file_dest):
                show_prompt(file, file_path2, file_dest, output_folder)

    # پیام پایان عملیات
    show_end_message()