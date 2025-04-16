import pyautogui
import time
from datetime import datetime, timedelta

def wait_until_6am():
    now = datetime.now()
    target = now.replace(hour=6, minute=0, second=0, microsecond=0)

    # If it's already past 6am today, schedule for tomorrow
    if now >= target:
        target += timedelta(days=1)

    time_to_wait = (target - now).total_seconds()
    print(f"Waiting until 6:00 AM... ({int(time_to_wait)} seconds)")
    time.sleep(time_to_wait)

def perform_click():
    print("Performing mouse click!")
    pyautogui.click()

if __name__ == "__main__":
    wait_until_6am()
    perform_click()
