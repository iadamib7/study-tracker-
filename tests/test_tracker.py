from app import tracker


def test_add_task(tmp_path, monkeypatch):
    tasks_file = tmp_path / "tasks.json"
    sessions_file = tmp_path / "sessions.json"

    tracker.save_data(str(tasks_file), [])
    tracker.save_data(str(sessions_file), [])

    monkeypatch.setattr(tracker, "TASKS_FILE", str(tasks_file))
    monkeypatch.setattr(tracker, "SESSIONS_FILE", str(sessions_file))

    tracker.add_task("Complete lab", "Chemistry", "2026-03-12")
    tasks = tracker.view_tasks()

    assert len(tasks) == 1
    assert tasks[0]["title"] == "Complete lab"
    assert tasks[0]["subject"] == "Chemistry"
    assert tasks[0]["due_date"] == "2026-03-12"
    assert tasks[0]["completed"] is False


def test_complete_task_valid_index(tmp_path, monkeypatch):
    tasks_file = tmp_path / "tasks.json"
    sessions_file = tmp_path / "sessions.json"

    sample_tasks = [
        {
            "title": "Assignment 1",
            "subject": "CS",
            "due_date": "2026-03-15",
            "completed": False
        }
    ]

    tracker.save_data(str(tasks_file), sample_tasks)
    tracker.save_data(str(sessions_file), [])

    monkeypatch.setattr(tracker, "TASKS_FILE", str(tasks_file))
    monkeypatch.setattr(tracker, "SESSIONS_FILE", str(sessions_file))

    result = tracker.complete_task(0)
    tasks = tracker.view_tasks()

    assert result is True
    assert tasks[0]["completed"] is True


def test_complete_task_invalid_index(tmp_path, monkeypatch):
    tasks_file = tmp_path / "tasks.json"
    sessions_file = tmp_path / "sessions.json"

    tracker.save_data(str(tasks_file), [])
    tracker.save_data(str(sessions_file), [])

    monkeypatch.setattr(tracker, "TASKS_FILE", str(tasks_file))
    monkeypatch.setattr(tracker, "SESSIONS_FILE", str(sessions_file))

    result = tracker.complete_task(3)

    assert result is False


def test_add_study_session(tmp_path, monkeypatch):
    tasks_file = tmp_path / "tasks.json"
    sessions_file = tmp_path / "sessions.json"

    tracker.save_data(str(tasks_file), [])
    tracker.save_data(str(sessions_file), [])

    monkeypatch.setattr(tracker, "TASKS_FILE", str(tasks_file))
    monkeypatch.setattr(tracker, "SESSIONS_FILE", str(sessions_file))

    tracker.add_study_session("Math", 60, "2026-03-07")
    sessions = tracker.view_study_sessions()

    assert len(sessions) == 1
    assert sessions[0]["subject"] == "Math"
    assert sessions[0]["duration_minutes"] == 60
    assert sessions[0]["session_date"] == "2026-03-07"