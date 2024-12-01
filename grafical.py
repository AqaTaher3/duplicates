# grafical.py
import tkinter as tk
from tkinter import messagebox
import shutil
import os

def move_file(selected_path, output_folder, file_name):
    """انتقال فایل به پوشه مقصد."""
    shutil.move(selected_path, os.path.join(output_folder, file_name))

def show_prompt(file, path1, path2, output_folder):
    """
    نمایش پنجره گرافیکی برای انتخاب فایل و انتقال آن.
    """
    root = tk.Tk()
    root.title("انتخاب فایل برای انتقال")

    # تنظیم پنجره به حالت فول‌اسکرین
    root.attributes('-fullscreen', True)

    # تنظیم رنگ پس‌زمینه پنجره به ذغالی
    root.configure(bg='#333333')

    # تغییر فونت و اندازه پنجره
    font = ("Arial", 24)
    tk.Label(root, text=f"فایل تکراری: {os.path.basename(file)}", font=font, fg='white', bg='#333333').pack(pady=20)

    # دکمه برای انتخاب مسیر فایل اصلی
    tk.Button(
        root,
        text=f"{path1}",
        bg="#D56B7A",  # رنگ پس‌زمینه صورتی
        font=font,
        fg="white",  # رنگ متن سفید
        command=lambda: [move_file(path1, output_folder, os.path.basename(path1)), root.destroy()],
        wraplength=0,
        anchor="w",
        padx=20
    ).pack(pady=10, padx=10, fill='x')

    # دکمه برای انتخاب مسیر فایل تکراری
    tk.Button(
        root,
        text=f"{path2}",
        bg="#A8D8A8",  # رنگ پس‌زمینه سبز روشن
        font=font,
        fg="white",  # رنگ متن سفید
        command=lambda: [move_file(path2, output_folder, os.path.basename(path2)), root.destroy()],
        wraplength=0,
        anchor="w",
        padx=20
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

def show_end_message():
    """نمایش پیام پایان عملیات"""
    messagebox.showinfo("اتمام عملیات", "تمام فایل‌های تکراری پردازش شدند.")
