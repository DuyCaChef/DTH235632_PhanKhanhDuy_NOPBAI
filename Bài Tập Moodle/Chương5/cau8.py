import os

def lay_file(day_path):
    """Trả về tên file kèm phần mở rộng"""
    return os.path.basename(day_path)

def lay_ten_bai_hat(day_path):
    """Trả về tên file không có đuôi mở rộng"""
    return os.path.splitext(os.path.basename(day_path))[0]


# --- Chạy thử ---
path = r"d:\music\muabui.mp3"
print("File đầy đủ :", lay_file(path))        # muabui.mp3
print("Tên bài hát:", lay_ten_bai_hat(path))  # muabui
