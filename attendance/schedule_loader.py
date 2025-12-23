import json
from datetime import datetime


def get_current_class(schedule_path="attendance/schedule.json"):
    now = datetime.now()
    today = now.strftime("%A")
    current_time = now.strftime("%H:%M")

    with open(schedule_path, "r") as f:
        schedule = json.load(f)

    if today not in schedule:
        return None

    for cls in schedule[today]:
        if cls["start_time"] <= current_time <= cls["end_time"]:
            return cls

    return None
