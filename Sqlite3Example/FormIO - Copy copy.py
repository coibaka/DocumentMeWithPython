import os
import sqlite3
import tkinter as tk
from tkinter import ttk

# Biến toàn cục để lưu trữ tên cơ sở dữ liệu hiện tại
current_db_name = ""

# Hàm để lấy danh sách cơ sở dữ liệu
def get_databases():
    return [file for file in os.listdir() if file.endswith('.db')]

# Hàm để hiển thị bảng khi nhấp đúp vào cơ sở dữ liệu
def on_db_click(event):
    global current_db_name
    selection = event.widget.curselection()
    current_db_name = event.widget.get(selection[0])
    conn = sqlite3.connect(current_db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    listbox_tables.delete(0, tk.END)
    for table in tables:
        listbox_tables.insert(tk.END, table[0])
    conn.close()

# Hàm để hiển thị hàng và cột khi nhấp đúp vào bảng
def on_table_click(event):
    global current_db_name
    selection = event.widget.curselection()
    table_name = event.widget.get(selection[0])
    conn = sqlite3.connect(current_db_name)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    columns = [description[0] for description in cursor.description]
    text_area.delete('1.0', tk.END)
    text_area.insert(tk.END, f"Columns: {columns}\n")
    for row in rows:
        text_area.insert(tk.END, f"{row}\n")
    conn.close()

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Database Viewer")

# Tạo Listbox để hiển thị cơ sở dữ liệu
listbox_dbs = tk.Listbox(root)
listbox_dbs.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
listbox_dbs.bind('<Double-1>', on_db_click)

# Tạo Listbox để hiển thị bảng
listbox_tables = tk.Listbox(root)
listbox_tables.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
listbox_tables.bind('<Double-1>', on_table_click)

# Tạo Text Area để hiển thị hàng và cột
text_area = tk.Text(root)
text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Điền danh sách cơ sở dữ liệu vào Listbox
for db in get_databases():
    listbox_dbs.insert(tk.END, db)

root.mainloop()
