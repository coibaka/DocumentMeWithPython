import os
import tkinter as tk
from tkinter import ttk

def get_database_names(directory):
    # Lấy danh sách tất cả các tệp trong thư mục đã chỉ định
    files = os.listdir(directory)
    
    # Lọc ra chỉ các tệp có phần mở rộng ".db"
    db_files = [file for file in files if file.lower().endswith(".db")]
    
    return db_files

def display_database_names_in_treeview(treeview, directory):
    # Lấy danh sách tên cơ sở dữ liệu
    db_names = get_database_names(directory)
    
    # Xóa các mục hiện có trong treeview
    treeview.delete(*treeview.get_children())
    
    # Chèn từng tên cơ sở dữ liệu vào treeview
    for db_name in db_names:
        treeview.insert("", "end", text=db_name)

# Tạo một GUI đơn giản với một widget Treeview
root = tk.Tk()
root.title("Tên Cơ sở dữ liệu")

# Tạo một widget Treeview
treeview = ttk.Treeview(root, columns=("Name"))
treeview.heading("#1", text="Tên Cơ sở dữ liệu")
treeview.pack()

# Lấy thư mục làm việc hiện tại
current_directory = os.getcwd()

# Hiển thị tên cơ sở dữ liệu trong Treeview
display_database_names_in_treeview(treeview, current_directory)

# Bắt đầu vòng lặp sự kiện GUI
root.mainloop()
