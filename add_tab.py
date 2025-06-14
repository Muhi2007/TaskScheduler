import tkinter as tk
from tkinter import messagebox

import modify_tab
import globals

def open_modify_window(parent, name):
    print(list(globals.task_names_dct.keys()))
    
    label = globals.task_names_dct[name][0]

    win = tk.Toplevel(parent)
    win.title("Modify Task")
    win.geometry("400x200")

    info = [w.cget("text") for w in label.winfo_children() if isinstance(w, tk.Label)]
    coulmn = [w for w in label.winfo_children() if isinstance(w, tk.Label)]
    button = [w for w in label.winfo_children() if isinstance(w, tk.Button)]

    tk.Label(win, text="Edit your task:").pack(pady=10)
    
    entry = tk.Entry(win, width=40)
    entry.insert(0, info[0])
    entry.pack(pady=5)
    entry.bind("<Return>", lambda e: save_changes())

    entry_time = tk.Entry(win, width=40)
    entry_time.insert(0, info[1])
    entry_time.pack(pady=5)
    entry_time.bind("<Return>", lambda e: save_changes())

    def save_changes():
        namesLst = globals.task_names_dct.keys()
        new_text = entry.get()
        new_time = entry_time.get()

        
        if name == new_text:
            coulmn[0].config(text= new_text)
            coulmn[1].config(text= new_time)
            modify_tab.save_tab(label, new_text, new_time)

        elif new_text not in list(namesLst):
            coulmn[0].config(text= new_text)
            coulmn[1].config(text= new_time)
            button[0].config(command=lambda: open_modify_window(parent, new_text))
            button[1].config(command= lambda: del_or_not(label, new_text))
            modify_tab.save_tab(label, new_text, new_time)
            modify_tab.del_csv(name)

        elif new_text in list(namesLst) and info[1] != new_time:
            coulmn[1].config(text= new_time)
            globals.task_names_dct[new_text] = [label, new_time]

        else:
            print("This name is already taken!")

        
        win.destroy()

    tk.Button(win, text="Save", command=save_changes).pack(pady=10)


def del_or_not(parent, name):
    message = messagebox.askyesno("REMOVING TASK", f"You are sure to delete {name}?")
    if message:
        parent.destroy()
        modify_tab.del_csv(name)
    else:
        print("As you wish")




def add_task(parent, name):
    task_frame = tk.Frame(parent, bg="white", bd=1, relief="solid")
    task_frame.pack(fill="x", padx=5, pady=5)

    name_label = tk.Label(task_frame, text=name, anchor="w", bg="white", font=("Segoe UI", 11))
    name_label.pack(side="left", fill="x", expand=True, padx=(10, 5), pady=10)

    time_label = tk.Label(task_frame, anchor="center", bg="white", font=("Segoe UI", 11))
    time_label.pack(side="left", padx=(5, 5), pady=10)

    edit_btn = tk.Button(task_frame, text="Edit", font=("Segoe UI", 10), command=lambda: open_modify_window(parent, name))
    edit_btn.pack(side="right", padx=(5, 10), pady=10)

    del_btn = tk.Button(task_frame, text="Remove", font=("Segoe UI", 10), command= lambda: del_or_not(task_frame, name))
    del_btn.pack(side="right", padx=(5,10), pady=10)

    modify_tab.save_tab(task_frame, name, "Time")    

    return task_frame