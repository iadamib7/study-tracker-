from app import habits
from app.storage import save_data


def test_add_habit(tmp_path, monkeypatch):
    habits_file = tmp_path / "habits.json"
    save_data(str(habits_file), [])

    monkeypatch.setattr(habits, "HABITS_FILE", str(habits_file))

    habits.add_habit("Practice coding", 5)
    data = habits.view_habits()

    assert len(data) == 1
    assert data[0]["habit_name"] == "Practice coding"
    assert data[0]["target_days_per_week"] == 5
    assert data[0]["completed_dates"] == []


def test_mark_habit_complete(tmp_path, monkeypatch):
    habits_file = tmp_path / "habits.json"
    sample_data = [
        {
            "habit_name": "Practice coding",
            "target_days_per_week": 5,
            "completed_dates": []
        }
    ]

    save_data(str(habits_file), sample_data)
    monkeypatch.setattr(habits, "HABITS_FILE", str(habits_file))

    result = habits.mark_habit_complete(0, "2026-03-07")
    data = habits.view_habits()

    assert result is True
    assert "2026-03-07" in data[0]["completed_dates"]


def test_get_habit_summary(tmp_path, monkeypatch):
    habits_file = tmp_path / "habits.json"
    sample_data = [
        {
            "habit_name": "Practice coding",
            "target_days_per_week": 5,
            "completed_dates": ["2026-03-05", "2026-03-06"]
        }
    ]

    save_data(str(habits_file), sample_data)
    monkeypatch.setattr(habits, "HABITS_FILE", str(habits_file))

    summary = habits.get_habit_summary()

    assert len(summary) == 1
    assert summary[0]["habit_name"] == "Practice coding"
    assert summary[0]["completed_count"] == 2
    assert summary[0]["streak"] == 2