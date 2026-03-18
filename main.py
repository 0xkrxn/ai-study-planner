import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox
from planner import StudyPlanner

planner = StudyPlanner()

# Window
app = tb.Window(themename="darkly")
app.title("AI Study Planner")
app.geometry("600x500")

# Title
title = tb.Label(app, text="📚 AI Study Planner", font=("Helvetica", 18, "bold"))
title.pack(pady=10)

# Frame
frame = tb.Frame(app)
frame.pack(pady=10)

# Inputs
tb.Label(frame, text="Subject").grid(row=0, column=0, padx=5, pady=5)
subject_entry = tb.Entry(frame)
subject_entry.grid(row=0, column=1, padx=5)

tb.Label(frame, text="Task").grid(row=1, column=0, padx=5, pady=5)
task_entry = tb.Entry(frame)
task_entry.grid(row=1, column=1, padx=5)

tb.Label(frame, text="Deadline (days)").grid(row=2, column=0, padx=5, pady=5)
days_entry = tb.Entry(frame)
days_entry.grid(row=2, column=1, padx=5)

# Functions
def add_task():
    subject = subject_entry.get()
    task = task_entry.get()
    days = days_entry.get()

    if not subject or not task or not days:
        messagebox.showerror("Error", "All fields required")
        return

    planner.add_task(subject, task, int(days))
    messagebox.showinfo("Success", "Task added!")
    load_tasks()

def load_tasks():
    for row in tree.get_children():
        tree.delete(row)

    for t in planner.tasks:
        tree.insert("", "end", values=(t['subject'], t['task'], t['deadline']))

def generate_plan():
    tasks = sorted(planner.tasks, key=lambda x: x['deadline'])
    output = "\n".join([f"{t['subject']} - {t['task']}" for t in tasks])
    messagebox.showinfo("Study Plan", output if output else "No tasks")

# Buttons
btn_frame = tb.Frame(app)
btn_frame.pack(pady=10)

tb.Button(btn_frame, text="Add Task", bootstyle=SUCCESS, command=add_task).grid(row=0, column=0, padx=10)
tb.Button(btn_frame, text="Generate Plan", bootstyle=INFO, command=generate_plan).grid(row=0, column=1, padx=10)

# Table
columns = ("Subject", "Task", "Deadline")
tree = tb.Treeview(app, columns=columns, show="headings", height=10)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")

tree.pack(pady=10)

# Load existing tasks
load_tasks()

app.mainloop()