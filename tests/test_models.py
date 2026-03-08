from app.models import Task, StudySession


def test_task_to_dict():
    task = Task(
        title="Finish homework",
        subject="Math",
        due_date="2026-03-10",
        completed=False
    )

    result = task.to_dict()

    assert result["title"] == "Finish homework"
    assert result["subject"] == "Math"
    assert result["due_date"] == "2026-03-10"
    assert result["completed"] is False


def test_study_session_to_dict():
    session = StudySession(
        subject="Physics",
        duration_minutes=45,
        session_date="2026-03-07"
    )

    result = session.to_dict()

    assert result["subject"] == "Physics"
    assert result["duration_minutes"] == 45
    assert result["session_date"] == "2026-03-07"