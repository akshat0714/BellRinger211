from datetime import datetime

def hours():
    now = datetime.now()
    feb14 = datetime(now.year, 2, 14, 0, 0, 0)

    if now >= feb14:
        feb14 = datetime(now.year + 1, 2, 14, 0, 0, 0)

    time_difference = feb14 - now
    hours_remaining = time_difference.total_seconds() / 3600

    return round(hours_remaining, 2)

print(f"{hours()} hours")
