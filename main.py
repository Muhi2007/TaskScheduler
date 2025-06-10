import tkinter as tk
from plyer import notification
import datetime as dt
import sys

import globals
import add_tab
import modify_tab

sys.stdout.reconfigure(encoding="utf-8")


root = tk.Tk()
root.title("Task Scheduler")
root.geometry("800x600")

top_frame = tk.Frame(root, height=120, bg="lightgrey")
top_frame.pack(side="top", fill="x", padx=10, pady=(10, 5))


task_entry = tk.Entry(top_frame, width=60, font=("Segoe UI", 12))
task_entry.pack(side="left", padx=(10, 5), pady=20)


bottom_frame = tk.Frame(root)
bottom_frame.pack(side="bottom", fill="both", expand=True, padx=10, pady=(0, 10))


task_canvas = tk.Canvas(bottom_frame, bg="white")
task_scroll = tk.Scrollbar(bottom_frame, orient="vertical", command=task_canvas.yview)

task_holder = tk.Frame(task_canvas, bg="white")

task_holder_window = task_canvas.create_window((0, 0), window=task_holder, anchor="nw")

def resize_holder(event):
    task_canvas.itemconfig(task_holder_window, width=event.width)

task_canvas.bind("<Configure>", resize_holder)
task_holder.bind("<Configure>", lambda e: task_canvas.configure(scrollregion=task_canvas.bbox("all")))

task_canvas.configure(yscrollcommand=task_scroll.set)
task_canvas.pack(side="left", fill="both", expand=True)
task_scroll.pack(side="right", fill="y")


def handler():
    text = task_entry.get()

    if text in globals.task_names_dct:
        add_tab.open_modify_window(root, text)
    else:
        add_tab.add_task(task_holder, text)


add_button = tk.Button(top_frame, text="Add Task", font=("Segoe UI", 11), command=handler)
add_button.pack(side="left", padx=10)

modify_tab.load_tabs(task_holder)

root.mainloop()