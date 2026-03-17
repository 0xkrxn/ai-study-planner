from planner import StudyPlanner

def main():
    planner = StudyPlanner()

    while True:
        print("\n📚 AI Study Planner")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Generate Study Plan")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            subject = input("Subject: ")
            task = input("Task: ")
            days = int(input("Deadline (in days): "))
            planner.add_task(subject, task, days)

        elif choice == "2":
            planner.view_tasks()

        elif choice == "3":
            planner.generate_plan()

        elif choice == "4":
            print("Good luck with your studies 💪")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()