import tkinter as tk
from tkinter import messagebox
import os

def show_entry_fields():
    print(f"Tên CSDL: {e1.get()}")
    print(f"Tên Table: {e2.get()}")
    print(f"Từ khoá tìm kiếm: {e3.get()}")

def get_database():
    db_name = e1.get()
    table_name = e2.get()
    # Giả sử rằng database là một file trong thư mục hiện tại
    if os.path.isfile(f"{db_name}.db"):
        print(f"Database {db_name} found.")
        # Thêm mã để load database và table ở đây
    else:
        messagebox.showerror("Error", f"Database {db_name} not found.")

master = tk.Tk()
tk.Label(master, text="Nhập tên CSDL").grid(row=0)
tk.Label(master, text="Nhập tên Table").grid(row=1)
tk.Label(master, text="Nhập để tìm kiếm từ khoá trong table").grid(row=2)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

tk.Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=tk.W, pady=4)
tk.Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=tk.W, pady=4)
tk.Button(master, text='Get Database', command=get_database).grid(row=3, column=2, sticky=tk.W, pady=4)

tk.mainloop()
