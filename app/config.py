import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

TASKS_FILE = os.path.join(DATA_DIR, "tasks.json")
SESSIONS_FILE = os.path.join(DATA_DIR, "sessions.json")
HABITS_FILE = os.path.join(DATA_DIR, "habits.json")

DATE_FORMAT = "%Y-%m-%d"
APP_NAME = "Study Tracker"
