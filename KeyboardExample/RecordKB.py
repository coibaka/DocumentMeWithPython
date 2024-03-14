# Ghi lại phím đã nhấn, sau khi nhấn `esc`` thì phát lại sự kiện đã ghi
import keyboard

# Ghi lại sự kiện cho đến khi nhấn 'esc'
recorded = keyboard.record(until='esc')

# Phát lại sự kiện đã ghi
keyboard.play(recorded)
