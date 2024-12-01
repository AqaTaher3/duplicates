import os
from adbutils import adb


def copy_missing_files_from_android(android_dir, local_dir):
    """
    فایل‌هایی را که در گوشی اندرویدی موجود است اما در دایرکتوری ویندوز وجود ندارند، کپی می‌کند.
    :param android_dir: مسیر دایرکتوری در گوشی (مثلاً /sdcard/Download)
    :param local_dir: مسیر دایرکتوری مقصد در ویندوز
    """
    # اتصال به دستگاه اندروید
    device = adb.device()
    print(f"Connected to device: {device.serial}")

    # اطمینان از وجود مسیر محلی
    if not os.path.exists(local_dir):
        os.makedirs(local_dir)
        print(f"Created local directory: {local_dir}")

    # لیست فایل‌های موجود در گوشی
    android_files = device.shell(f"ls {android_dir}").splitlines()

    for file_name in android_files:
        android_file = f"{android_dir}/{file_name}"
        local_file = os.path.join(local_dir, file_name)

        if not os.path.exists(local_file):
            # انتقال فایل از گوشی به ویندوز
            device.pull(android_file, local_file)
            print(f"File copied: {android_file} -> {local_file}")
        else:
            print(f"File already exists: {file_name}")


if __name__ == "__main__":
    # مسیر دایرکتوری گوشی و ویندوز
    android_folder = "/sdcard/Download"
    local_folder = r"C:\Users\HP\Music\music"

    # کپی فایل‌های موجود در گوشی به ویندوز
    copy_missing_files_from_android(android_folder, local_folder)
