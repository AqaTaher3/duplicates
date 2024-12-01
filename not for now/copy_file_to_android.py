from adbutils import adb


def copy_file_to_android(local_path, android_path):
    # اتصال به دستگاه اندروید
    device = adb.device()
    print(f"Connected to device: {device.serial}")


    # انتقال فایل به گوشی
    device.push(local_path, android_path)
    print(f"File pushed to: {android_path}")


def copy_file_to_windows(android_path, local_path):
    # اتصال به دستگاه اندروید
    device = adb.device()
    print(f"Connected to device: {device.serial}")

    # دریافت فایل از گوشی
    device.pull(android_path, local_path)
    print(f"File pulled to: {local_path}")


if __name__ == "__main__":
    local_file = r"C:\Users\YourUser\Desktop\file.txt"  # فایل مبدا در ویندوز
    android_file = "/sdcard/Download/file.txt"  # مسیر مقصد در گوشی

    # انتقال فایل به گوشی
    copy_file_to_android(local_file, android_file)

    # دریافت فایل از گوشی
    # copy_file_to_windows(android_file, local_file)
