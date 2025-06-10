import tkinter as tk

import add_tab
import globals

def load_task(parent, name, time):
    task_frame = tk.Frame(parent, bg="white", bd=1, relief="solid")
    task_frame.pack(fill="x", padx=5, pady=5)

    name_label = tk.Label(task_frame, text=name, anchor="w", bg="white", font=("Segoe UI", 11))
    name_label.pack(side="left", fill="x", expand=True, padx=(10, 5), pady=10)

    time_label = tk.Label(task_frame, anchor="center", text= time, bg="white", font=("Segoe UI", 11))
    time_label.pack(side="left", padx=(5, 5), pady=10)

    edit_btn = tk.Button(task_frame, text="Edit", font=("Segoe UI", 10), command=lambda: add_tab.open_modify_window(parent, name))
    edit_btn.pack(side="right", padx=(5, 10), pady=10)

    del_btn = tk.Button(task_frame, text="Remove", font=("Segoe UI", 10))
    del_btn.pack(side="right", padx=(5,10), pady=10)

    globals.task_names_dct[name] = [task_frame, time]
    return task_frame