import os
import shutil
import tkinter as tk
from tkinter import messagebox


def move_file(selected_path, output_folder, file_name):
    # انتقال فایل بدون نمایش پیام
    shutil.move(selected_path, os.path.join(output_folder, file_name))


def prompt_user(folder1, folder2, output_folder):
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

            # ساخت پنجره برای انتخاب فایل
            root = tk.Tk()
            root.title("انتخاب فایل برای انتقال")

            # تنظیم پنجره به حالت فول‌اسکرین
            root.attributes('-fullscreen', True)

            # تنظیم رنگ پس‌زمینه پنجره به ذغالی
            root.configure(bg='#333333')

            # تغییر فونت و اندازه پنجره
            font = ("Arial", 24)  # تغییر اندازه فونت به 24
            tk.Label(root, text=f"فایل تکراری: {file}", font=font, fg='white', bg='#333333').pack(pady=20)

            # دکمه برای انتخاب مسیر فایل اول
            tk.Button(
                root,
                text=f"{path1}",
                bg="#D56B7A",  # رنگ پس‌زمینه صورتی
                font=font,
                fg="white",  # رنگ متن سفید
                command=lambda: [move_file(path1, output_folder, file), root.destroy()],
                wraplength=0,  # جلوگیری از تقسیم متن به چند خط
                anchor="w",  # تنظیم متن به سمت چپ
                padx=20  # فاصله داخلی از سمت چپ
            ).pack(pady=10, padx=10, fill='x')

            # دکمه برای انتخاب مسیر فایل دوم
            tk.Button(
                root,
                text=f"{path2}",
                bg="#A8D8A8",  # رنگ پس‌زمینه سبز روشن
                font=font,
                fg="white",  # رنگ متن سفید
                command=lambda: [move_file(path2, output_folder, file), root.destroy()],
                wraplength=0,  # جلوگیری از تقسیم متن به چند خط
                anchor="w",  # تنظیم متن به سمت چپ
                padx=20  # فاصله داخلی از سمت چپ
            ).pack(pady=10, padx=10, fill='x')

            # دکمه برای صرف‌نظر کردن
            tk.Button(
                root,
                text="هیچ‌کدام را منتقل نکن",
                font=font,
                fg="white",
                bg="#666666",  # رنگ پس‌زمینه خاکی برای دکمه
                command=root.destroy
            ).pack(pady=20)

            root.mainloop()

    # پیام پایان عملیات
    messagebox.showinfo("اتمام عملیات", "تمام فایل‌های تکراری پردازش شدند.")


if __name__ == "__main__":
    folder1 = r"C:\Users\HP\Music\muzic"
    folder2 = r"C:\Users\HP\Music\music"
    output_folder = r"C:\Users\HP\Music\gadimi"
    prompt_user(folder1, folder2, output_folder)
