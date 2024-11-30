import os
import shutil
import hashlib
import tkinter as tk
from tkinter import messagebox
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm  # For progress bar

def calculate_file_hash(file_path):
    """Calculate the SHA-256 hash of a file."""
    BLOCK_SIZE = 65536  # 64 KB
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        buffer = f.read(BLOCK_SIZE)
        while len(buffer) > 0:
            hasher.update(buffer)
            buffer = f.read(BLOCK_SIZE)
    return hasher.hexdigest()


def ensure_directory_exists(directory):
    """Ensure the destination directory exists, create it if necessary."""
    os.makedirs(directory, exist_ok=True)


def move_file(selected_path, output_folder, file_name):
    """Move the selected file to the destination folder."""
    shutil.move(selected_path, os.path.join(output_folder, file_name))


def find_and_prompt_duplicates(source_folder, output_folder):
    """Find and prompt user to move duplicate files to the destination folder."""
    ensure_directory_exists(output_folder)
    seen_files = {}
    transferred_files = set()

    # Collect all files
    files = [os.path.join(root, file) for root, _, files in os.walk(source_folder) for file in files]
    total_files = len(files)

    def process_file(file_path):
        """Process a single file: check for duplicates and prompt user."""
        file_hash = calculate_file_hash(file_path)
        if file_hash in seen_files:
            base_name, extension = os.path.splitext(os.path.basename(file_path))
            # Get duplicate files
            original_file = seen_files[file_hash]
            duplicate_file = file_path

            # Create the Tkinter window to prompt the user
            root = tk.Tk()
            root.title("انتخاب فایل برای انتقال")

            # تنظیم پنجره به حالت فول‌اسکرین
            root.attributes('-fullscreen', True)

            # تنظیم رنگ پس‌زمینه پنجره به ذغالی
            root.configure(bg='#333333')

            # تغییر فونت و اندازه پنجره
            font = ("Arial", 24)  # تغییر اندازه فونت به 24
            tk.Label(root, text=f"فایل تکراری: {os.path.basename(duplicate_file)}", font=font, fg='white', bg='#333333').pack(pady=20)

            # دکمه برای انتخاب مسیر فایل اصلی
            tk.Button(
                root,
                text=f"{original_file}",
                bg="#D56B7A",  # رنگ پس‌زمینه صورتی
                font=font,
                fg="white",  # رنگ متن سفید
                command=lambda: [move_file(original_file, output_folder, os.path.basename(original_file)), root.destroy()],
                wraplength=0,  # جلوگیری از تقسیم متن به چند خط
                anchor="w",  # تنظیم متن به سمت چپ
                padx=20  # فاصله داخلی از سمت چپ
            ).pack(pady=10, padx=10, fill='x')

            # دکمه برای انتخاب مسیر فایل تکراری
            tk.Button(
                root,
                text=f"{duplicate_file}",
                bg="#A8D8A8",  # رنگ پس‌زمینه سبز روشن
                font=font,
                fg="white",  # رنگ متن سفید
                command=lambda: [move_file(duplicate_file, output_folder, os.path.basename(duplicate_file)), root.destroy()],
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

        else:
            seen_files[file_hash] = file_path

    # Process files with progress bar
    with ThreadPoolExecutor() as executor, tqdm(total=total_files, desc="Processing files") as pbar:
        for file_path in files:
            executor.submit(process_file, file_path)
            pbar.update(1)

    # پیام پایان عملیات
    messagebox.showinfo("اتمام عملیات", "تمام فایل‌های تکراری پردازش شدند.")


if __name__ == "__main__":
    folder = r"C:\Users\HP\Music\muzic"
    output_folder = r"C:\Users\HP\Music\gadimi"  # پوشه مقصد
    find_and_prompt_duplicates(folder, output_folder)
