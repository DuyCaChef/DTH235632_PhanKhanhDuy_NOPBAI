import time
import os

# 4 hình mẫu (có thể thay bằng các hình từ đề)
hinh1 = """
    *
   * *
  *****
 *     *
*       *
"""

hinh2 = """
*****
*   *
*****
*   *
*****
"""

hinh3 = """
  ***
 *   *
*     *
 *   *
  ***
"""

hinh4 = """
*   *
 * *
  *
 * *
*   *
"""

# Danh sách các hình
ds_hinh = [hinh1, hinh2, hinh3, hinh4]

# Hiển thị từng hình, mỗi hình cách 5 giây
for hinh in ds_hinh:
    os.system("cls" if os.name == "nt" else "clear")  # xóa màn hình (Windows/Linux)
    print(hinh)
    time.sleep(5)
