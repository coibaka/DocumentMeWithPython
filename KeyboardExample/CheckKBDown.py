# Kiểm tra sự kiện nhấn phím với trường hợp phím `down`
import keyboard

def on_key_event(event):
    if event.event_type == 'down':
        print(f"Phím {event.name} đã được nhấn")

# Bắt đầu nghe sự kiện
keyboard.hook(on_key_event)
keyboard.wait('esc')  # Chờ đến khi nhấn phím 'esc' để thoát
