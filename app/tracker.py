from app.models import Task, StudySession
from app.storage import load_data, save_data
from app.config import TASKS_FILE, SESSIONS_FILE


def add_task(title: str, subject: str, due_date: str) -> None:
    tasks = load_data(TASKS_FILE)
    new_task = Task(title=title, subject=subject, due_date=due_date)
    tasks.append(new_task.to_dict())
    save_data(TASKS_FILE, tasks)


def view_tasks() -> list:
    return load_data(TASKS_FILE)


def complete_task(task_index: int) -> bool:
    tasks = load_data(TASKS_FILE)

    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        save_data(TASKS_FILE, tasks)
        return True

    return False


def add_study_session(subject: str, duration_minutes: int, session_date: str) -> None:
    sessions = load_data(SESSIONS_FILE)
    new_session = StudySession(
        subject=subject,
        duration_minutes=duration_minutes,
        session_date=session_date
    )
    sessions.append(new_session.to_dict())
    save_data(SESSIONS_FILE, sessions)


def view_study_sessions() -> list:
    return load_data(SESSIONS_FILE)
