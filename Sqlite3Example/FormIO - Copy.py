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
        columns = [description[0] for description in cursor.description]
        tree['columns'] = columns
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor='w')
        
        # Thêm dữ liệu từ mỗi hàng vào treeview
        for row in cursor.fetchall():
            tree.insert('', 'end', values=row)
        
        # Đóng kết nối cơ sở dữ liệu
        conn.close()
    elif db_name:
        # Load và hiển thị các bảng trong cơ sở dữ liệu được chỉ định
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        for table in tables:
            tree.insert("", "end", values=(table[0],))
        conn.close()
    else:
        # Load và hiển thị tất cả cơ sở dữ liệu trong thư mục hiện tại
        databases = [filename for filename in os.listdir() if filename.endswith(".db")]
        for db in databases:
            tree.insert("", "end", values=(db,))

# Hàm được gọi khi nhấn button "GET"
def on_get_click():
    db_name = db_entry.get()
    table_name = table_entry.get()
    load_to_treeview(db_name, table_name)

# Tạo GUI cho nhập liệu
input_window = tk.Tk()
input_window.title("Database and Table Input")

tk.Label(input_window, text="Database Name:").pack(side="top", fill="x")
db_entry = tk.Entry(input_window)
db_entry.pack(side="top", fill="x")

tk.Label(input_window, text="Table Name:").pack(side="top", fill="x")
table_entry = tk.Entry(input_window)
table_entry.pack(side="top", fill="x")

get_button = tk.Button(input_window, text="GET", command=on_get_click)
get_button.pack(side="top")

# Tạo GUI cho treeview
treeview_window = tk.Toplevel()
treeview_window.title("Database Viewer")

tree = ttk.Treeview(treeview_window, columns=('Name',), show='headings')
tree.heading('Name', text='Name')
tree.pack(expand=True, fill='both')

# Hiển thị cửa sổ
input_window.mainloop()
