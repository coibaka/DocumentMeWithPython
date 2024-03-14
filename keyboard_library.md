# Keyboard Library
Thư viện `keyboard` trong `Python` cho phép bạn **kiểm soát** và **theo dõi** các sự kiện `bàn phím`. Dưới đây là hướng dẫn cơ bản để sử dụng thư viện này:

Cài đặt Thư Viện: 
1. Đầu tiên, bạn cần cài đặt thư viện keyboard bằng cách chạy lệnh sau trong terminal hoặc command prompt của bạn:
```pip install keyboard```
Lưu ý rằng bạn có thể cần `quyền admin` để cài đặt thư viện này.
Nghe Sự Kiện Phím: Bạn có thể sử dụng `keyboard` để **nghe** các `sự kiện` **phím nhấn hoặc thả phím**. Dưới đây là một ví dụ đơn giản:
```Python

import keyboard

def on_key_event(event):
    if event.event_type == 'down':
        print(f"Phím {event.name} đã được nhấn")

# Bắt đầu nghe sự kiện
keyboard.hook(on_key_event)
keyboard.wait('esc')  # Chờ đến khi nhấn phím 'esc' để thoát
```
Ghi Lại Sự Kiện Phím: Để ghi lại các sự kiện phím, bạn có thể sử dụng keyboard.record và keyboard.play để ghi lại và phát lại các sự kiện:
```Python

import keyboard

# Ghi lại sự kiện cho đến khi nhấn 'esc'
recorded = keyboard.record(until='esc')

# Phát lại sự kiện đã ghi
keyboard.play(recorded)
```
Tạo Hotkey: Bạn cũng có thể tạo các hotkey (phím tắt) để thực hiện hành động khi nhấn tổ hợp phím nhất định:
```Python

import keyboard

# Hàm sẽ được gọi khi nhấn tổ hợp phím ctrl+shift
def print_msg():
    print("Hotkey ctrl+shift đã được nhấn")

# Đăng ký hotkey
keyboard.add_hotkey('ctrl+shift', print_msg)

# Chờ đến khi nhấn 'esc' để thoát
keyboard.wait('esc')
```
Kiểm Tra Phím Đang Được Nhấn: Bạn có thể kiểm tra xem một phím cụ thể có đang được nhấn hay không:
```Python

import keyboard

if keyboard.is_pressed('space'):
    print("Phím space đang được nhấn")
```
