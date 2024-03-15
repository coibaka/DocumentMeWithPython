import os
import sqlite3
import tkinter as tk
from tkinter import ttk

def load_to_treeview(db_name=None, table_name=None):
    tree.delete(*tree.get_children())
    if db_name and table_name:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM {table_name};')
        columns = [description[0] for description in cursor.description]
        tree['columns'] = columns
        tree.heading('#0', text='Row ID', anchor='w')
        tree.column('#0', anchor='w')
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor='center')
        for row in cursor.fetchall():
            tree.insert('', 'end', text=row[0], values=row[1:])
        conn.close()
    elif db_name:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        tree['columns'] = ['Tables']
        tree.heading('#0', text='Database', anchor='w')
        tree.column('#0', anchor='w', width=100)
        tree.heading('Tables', text='Table Name')
        tree.column('Tables', anchor='center', width=200)
        for table in tables:
            tree.insert('', 'end', text=db_name, values=table)
        conn.close()
    else:
        databases = [filename for filename in os.listdir() if filename.endswith(".db")]
        tree['columns'] = ['Databases']
        tree.heading('#0', text='Index', anchor='w')
        tree.column('#0', anchor='w', width=100)
        tree.heading('Databases', text='Database Name')
        tree.column('Databases', anchor='center', width=200)
        for idx, db in enumerate(databases, start=1):
            tree.insert('', 'end', text=idx, values=db)


def on_item_double_click(event):
    selected_items = tree.selection()
    if selected_items:  # Check if the selection is not empty
        item = selected_items[0]
        item_text = tree.item(item, 'values')
        if tree.parent(item):
            db_name = tree.item(tree.parent(item), 'text')
            table_name = item_text[0]
            load_to_treeview(db_name=db_name, table_name=table_name)
        else:
            db_name = item_text[0]
            load_to_treeview(db_name=db_name)

def on_get_click():
    db_name = db_entry.get()
    table_name = table_entry.get()
    load_to_treeview(db_name, table_name)

input_window = tk.Tk()
input_window.title("Database and Table Viewer")

frame = ttk.Frame(input_window)
frame.pack(expand=True, fill='both')

tree = ttk.Treeview(frame, show='tree')
tree.pack(expand=True, fill='both')
tree.bind('<Double-1>', on_item_double_click)

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

input_window.mainloop()
