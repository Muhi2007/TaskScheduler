#global values
import json
import os

file = 'tasks.json'
task_names_dct = {}

if os.path.exists(file):
    try:
        with open(file, "r", encoding="utf-8") as file:
            task_names_dct = json.load(file)
        print("Tasks loaded successfully.")
    except Exception as e:
        print(f"Error loading tasks: {e}")
else:
    task_names_dct = {}
    print("No saved tasks found.")
