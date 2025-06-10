import tkinter as tk
import json
import copy

import add_tab
import globals
import handler

fileName = "tasks.json"

#  Every save_dct file is for the JSON's frame error

def del_csv(name):
    globals.task_names_dct.pop(name)

    save_dct = {}
    for names in globals.task_names_dct:
        save_dct[names] = globals.task_names_dct[names][1]

    try:
        with open(fileName, "w", encoding="utf-8") as file:
            json.dump(save_dct, file, indent=4)
        print("Tasks deleted successfully.")
    except Exception as e:
        print(f"Error saving tasks: {e}")



def save_tab(label, newName, time):
    globals.task_names_dct[newName] = [label, time]
    print(globals.task_names_dct)

    save_dct = {}
    for names in globals.task_names_dct:
        save_dct[names] = globals.task_names_dct[names][1]

    try:
        with open(fileName, "w", encoding="utf-8") as file:
            json.dump(save_dct, file, indent=4)
        print("Tasks saved successfully.")
    except Exception as e:
        print(f"Error saving tasks: {e}")


def load_tabs(parent):
    dct = copy.copy(globals.task_names_dct)
        
    for name in dct:
        time = dct[name]
        handler.load_task(parent, name, time)
    
    return dct

