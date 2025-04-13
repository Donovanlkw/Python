import pyautogui
import time

print("Starting in 5 seconds... switch to your browser!")
time.sleep(5)

for i in range(100):
    pyautogui.press('f5')  # Simulates pressing F5
    print(f"Refreshed {i + 1} times")
    time.sleep(3)  # Wait 3 seconds between refreshes
