import os
import sqlite3
import tkinter as tk
from tkinter import ttk

# Hàm để load databases hoặc tables vào treeview
def load_to_treeview(db_name=None, table_name=None):
    tree.delete(*tree.get_children())  # Xóa dữ liệu cũ trong treeview
    if db_name and table_name:
        # Kết nối tới cơ sở dữ liệu
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        # Thực hiện truy vấn để lấy tất cả dữ liệu từ bảng
        cursor.execute(f'SELECT * FROM {table_name};')
        
        # Lấy tên cột và cấu hình các cột cho treeview
        columns = ['ID'] + [description[0] for description in cursor.description]
        tree['columns'] = columns
        # Định nghĩa lại các cột để không có khoảng trắng
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor='w')
        
        # Thêm dữ liệu từ mỗi hàng vào treeview
        for idx, row in enumerate(cursor.fetchall(), start=1):
            tree.insert('', 'end', values=(idx,) + row)
        
        # Đóng kết nối cơ sở dữ liệu
        conn.close()
    elif db_name:
        # Load và hiển thị các bảng trong cơ sở dữ liệu được chỉ định
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        tree['columns'] = ['ID', 'Table Name']
        for col in ['ID', 'Table Name']:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor='w')
        for idx, table in enumerate(tables, start=1):
            tree.insert("", "end", values=(idx, table[0]))
        conn.close()
    else:
        # Load và hiển thị tất cả cơ sở dữ liệu trong thư mục hiện tại
        databases = [filename for filename in os.listdir() if filename.endswith(".db")]
        tree['columns'] = ['ID', 'Database Name']
        for col in ['ID', 'Database Name']:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor='w')
        for idx, db in enumerate(databases, start=1):
            tree.insert("", "end", values=(idx, db))

# Hàm được gọi khi nhấn button "GET"
def on_get_click():
    db_name = db_entry.get()
    table_name = table_entry.get()
    load_to_treeview(db_name, table_name)

# Tạo GUI cho nhập liệu và treeview
input_window = tk.Tk()
input_window.title("Database and Table Viewer")

# Tạo frame cho treeview
frame = ttk.Frame(input_window)
frame.pack(expand=True, fill='both')

# Tạo treeview trong frame
tree = ttk.Treeview(frame, show='headings')  # Đảm bảo rằng 'show' chỉ định 'headings' để không hiển thị cột trống
tree.pack(expand=True, fill='both')

# Tạo frame cho input
input_frame = ttk.Frame(input_window)
input_frame.pack(side="bottom", fill="x", expand=False)

tk.Label(input_frame, text="Database Name:").pack(side="left")
db_entry = tk.Entry(input_frame)
db_entry.pack(side="left")

tk.Label(input_frame, text="Table Name:").pack(side="left")
table_entry = tk.Entry(input_frame)
table_entry.pack(side="left")

get_button = tk.Button(input_frame, text="GET", command=on_get_click)
get_button.pack(side="left")

# Hiển thị cửa sổ
input_window.mainloop()
