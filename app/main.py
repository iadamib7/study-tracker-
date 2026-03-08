from datetime import datetime

from app.storage import ensure_data_files
from app.tracker import (
    add_task,
    view_tasks,
    complete_task,
    add_study_session,
    view_study_sessions
)
from app.reports import print_report


def show_menu() -> None:
    print("\n===== STUDY TRACKER =====")
    print("1. Add task")
    print("2. View tasks")
    print("3. Complete task")
    print("4. Add study session")
    print("5. View study sessions")
    print("6. View report")
    print("7. Exit")


def get_valid_date(prompt: str) -> str:
    while True:
        user_input = input(prompt).strip()
        try:
            datetime.strptime(user_input, "%Y-%m-%d")
            return user_input
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")


def get_valid_number(prompt: str) -> int:
    while True:
        user_input = input(prompt).strip()
        if user_input.isdigit() and int(user_input) > 0:
            return int(user_input)
        print("Please enter a valid positive number.")


def handle_add_task() -> None:
    print("\n--- Add Task ---")
    title = input("Enter task title: ").strip()
    subject = input("Enter subject: ").strip()
    due_date = get_valid_date("Enter due date (YYYY-MM-DD): ")

    add_task(title, subject, due_date)
    print("Task added successfully.")


def handle_view_tasks() -> None:
    print("\n--- Task List ---")
    tasks = view_tasks()

    if not tasks:
        print("No tasks found.")
        return

    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{index}. {task['title']} | {task['subject']} | Due: {task['due_date']} | {status}")


def handle_complete_task() -> None:
    print("\n--- Complete Task ---")
    tasks = view_tasks()

    if not tasks:
        print("No tasks available.")
        return

    handle_view_tasks()
    task_number = get_valid_number("Enter task number to mark complete: ")

    if complete_task(task_number - 1):
        print("Task marked as complete.")
    else:
        print("Invalid task number.")


def handle_add_study_session() -> None:
    print("\n--- Add Study Session ---")
    subject = input("Enter subject: ").strip()
    duration = get_valid_number("Enter duration in minutes: ")
    session_date = get_valid_date("Enter session date (YYYY-MM-DD): ")

    add_study_session(subject, duration, session_date)
    print("Study session added successfully.")


def handle_view_study_sessions() -> None:
    print("\n--- Study Sessions ---")
    sessions = view_study_sessions()

    if not sessions:
        print("No study sessions found.")
        return

    for index, session in enumerate(sessions, start=1):
        print(
            f"{index}. {session['subject']} | "
            f"{session['duration_minutes']} minutes | "
            f"{session['session_date']}"
        )


def main() -> None:
    ensure_data_files()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            handle_add_task()
        elif choice == "2":
            handle_view_tasks()
        elif choice == "3":
            handle_complete_task()
        elif choice == "4":
            handle_add_study_session()
        elif choice == "5":
            handle_view_study_sessions()
        elif choice == "6":
            print_report()
        elif choice == "7":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please select from 1 to 7.")


if __name__ == "__main__":
    main()