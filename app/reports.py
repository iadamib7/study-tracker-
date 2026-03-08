from app.storage import load_data
from app.config import TASKS_FILE, SESSIONS_FILE


def get_task_summary() -> dict:
    tasks = load_data(TASKS_FILE)
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task["completed"])
    pending_tasks = total_tasks - completed_tasks

    return {
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks
    }


def get_study_summary() -> dict:
    sessions = load_data(SESSIONS_FILE)
    total_sessions = len(sessions)
    total_minutes = sum(session["duration_minutes"] for session in sessions)

    subject_totals: dict[str, int] = {}
    for session in sessions:
        subject = session["subject"]
        subject_totals[subject] = subject_totals.get(subject, 0) + session["duration_minutes"]

    return {
        "total_sessions": total_sessions,
        "total_minutes": total_minutes,
        "subject_totals": subject_totals
    }


def print_report() -> None:
    task_summary = get_task_summary()
    study_summary = get_study_summary()

    print("\n===== STUDY TRACKER REPORT =====")
    print(f"Total tasks: {task_summary['total_tasks']}")
    print(f"Completed tasks: {task_summary['completed_tasks']}")
    print(f"Pending tasks: {task_summary['pending_tasks']}")

    print(f"\nTotal study sessions: {study_summary['total_sessions']}")
    print(f"Total study time: {study_summary['total_minutes']} minutes")

    print("\nStudy time by subject:")
    if study_summary["subject_totals"]:
        for subject, minutes in study_summary["subject_totals"].items():
            print(f"- {subject}: {minutes} minutes")
    else:
        print("No study sessions recorded yet.")