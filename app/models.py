from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class Task:
    title: str
    subject: str
    due_date: str
    completed: bool = False

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class StudySession:
    subject: str
    duration_minutes: int
    session_date: str

    def to_dict(self) -> dict:
        return asdict(self)
    