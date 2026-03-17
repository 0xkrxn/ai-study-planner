import json
from datetime import datetime, timedelta

class StudyPlanner:
    def __init__(self):
        self.file = "data.json"
        self.load_data()

    def load_data(self):
        try:
            with open(self.file, "r") as f:
                self.tasks = json.load(f)
        except:
            self.tasks = []

    def save_data(self):
        with open(self.file, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, subject, task, days):
        deadline = (datetime.now() + timedelta(days=days)).strftime("%Y-%m-%d")

        self.tasks.append({
            "subject": subject,
            "task": task,
            "deadline": deadline
        })

        self.save_data()
        print("✅ Task added!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return

        for i, t in enumerate(self.tasks, 1):
            print(f"{i}. {t['subject']} - {t['task']} (Due: {t['deadline']})")

    def generate_plan(self):
        if not self.tasks:
            print("No tasks to plan.")
            return

        print("\n📅 Smart Study Plan:")

        sorted_tasks = sorted(self.tasks, key=lambda x: x['deadline'])

        for t in sorted_tasks:
            print(f"👉 {t['subject']} - {t['task']} (Priority High)")