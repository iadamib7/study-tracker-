from app import reports
from app.storage import save_data


def test_get_task_summary(tmp_path, monkeypatch):
    tasks_file = tmp_path / "tasks.json"
    sessions_file = tmp_path / "sessions.json"

    task_data = [
        {"title": "Task 1", "subject": "Math", "due_date": "2026-03-08", "completed": True},
        {"title": "Task 2", "subject": "CS", "due_date": "2026-03-09", "completed": False},
    ]

    save_data(str(tasks_file), task_data)
    save_data(str(sessions_file), [])

    monkeypatch.setattr(reports, "TASKS_FILE", str(tasks_file))
    monkeypatch.setattr(reports, "SESSIONS_FILE", str(sessions_file))

    summary = reports.get_task_summary()

    assert summary["total_tasks"] == 2
    assert summary["completed_tasks"] == 1
    assert summary["pending_tasks"] == 1


def test_get_study_summary(tmp_path, monkeypatch):
    tasks_file = tmp_path / "tasks.json"
    sessions_file = tmp_path / "sessions.json"

    session_data = [
        {"subject": "Math", "duration_minutes": 30, "session_date": "2026-03-07"},
        {"subject": "Math", "duration_minutes": 45, "session_date": "2026-03-08"},
        {"subject": "Physics", "duration_minutes": 60, "session_date": "2026-03-08"},
    ]

    save_data(str(tasks_file), [])
    save_data(str(sessions_file), session_data)

    monkeypatch.setattr(reports, "TASKS_FILE", str(tasks_file))
    monkeypatch.setattr(reports, "SESSIONS_FILE", str(sessions_file))

    summary = reports.get_study_summary()

    assert summary["total_sessions"] == 3
    assert summary["total_minutes"] == 135
    assert summary["subject_totals"]["Math"] == 75
    assert summary["subject_totals"]["Physics"] == 60
    