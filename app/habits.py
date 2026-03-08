from app.storage import load_data, save_data
from app.config import HABITS_FILE


def view_habits() -> list:
    return load_data(HABITS_FILE)


def add_habit(habit_name: str, target_days_per_week: int) -> None:
    habits = load_data(HABITS_FILE)

    new_habit = {
        "habit_name": habit_name,
        "target_days_per_week": target_days_per_week,
        "completed_dates": []
    }

    habits.append(new_habit)
    save_data(HABITS_FILE, habits)


def mark_habit_complete(habit_index: int, completion_date: str) -> bool:
    habits = load_data(HABITS_FILE)

    if 0 <= habit_index < len(habits):
        if completion_date not in habits[habit_index]["completed_dates"]:
            habits[habit_index]["completed_dates"].append(completion_date)
            save_data(HABITS_FILE, habits)
        return True

    return False


def get_habit_streak(habit: dict) -> int:
    completed_dates = sorted(habit["completed_dates"])
    if not completed_dates:
        return 0
    return len(completed_dates)


def get_habit_summary() -> list:
    habits = load_data(HABITS_FILE)
    summary = []

    for habit in habits:
        summary.append({
            "habit_name": habit["habit_name"],
            "target_days_per_week": habit["target_days_per_week"],
            "completed_count": len(habit["completed_dates"]),
            "streak": get_habit_streak(habit)
        })

    return summary