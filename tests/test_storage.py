import json
from pathlib import Path

from app import storage


def test_ensure_data_files_creates_files(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    tasks_file = data_dir / "tasks.json"
    sessions_file = data_dir / "sessions.json"

    monkeypatch.setattr(storage, "DATA_DIR", str(data_dir))
    monkeypatch.setattr(storage, "TASKS_FILE", str(tasks_file))
    monkeypatch.setattr(storage, "SESSIONS_FILE", str(sessions_file))

    storage.ensure_data_files()

    assert data_dir.exists()
    assert tasks_file.exists()
    assert sessions_file.exists()

    assert json.loads(tasks_file.read_text(encoding="utf-8")) == []
    assert json.loads(sessions_file.read_text(encoding="utf-8")) == []


def test_load_data_returns_empty_list_for_missing_file(tmp_path):
    missing_file = tmp_path / "missing.json"
    result = storage.load_data(str(missing_file))
    assert result == []


def test_save_and_load_data(tmp_path):
    test_file = tmp_path / "sample.json"
    sample_data = [
        {"title": "Read chapter 1", "subject": "Biology", "due_date": "2026-03-08", "completed": False}
    ]

    storage.save_data(str(test_file), sample_data)
    loaded_data = storage.load_data(str(test_file))

    assert loaded_data == sample_data


def test_load_data_returns_empty_list_for_bad_json(tmp_path):
    bad_file = tmp_path / "bad.json"
    bad_file.write_text("{not valid json", encoding="utf-8")

    result = storage.load_data(str(bad_file))

    assert result == []
    