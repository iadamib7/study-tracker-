import json
import os

from app.config import DATA_DIR, TASKS_FILE, SESSIONS_FILE, HABITS_FILE


def ensure_data_files() -> None:
    os.makedirs(DATA_DIR, exist_ok=True)

    for file_path in [TASKS_FILE, SESSIONS_FILE, HABITS_FILE]:
        if not os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump([], file)


def load_data(file_path: str) -> list:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_data(file_path: str, data: list) -> None:
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)