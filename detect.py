import pyautogui
import pyperclip
import winsound
import time

keywords = ["2025", "Additional security check is required"]      # Replace with your target keyword
refresh_delay = 5             # Seconds between refreshes
refresh_count = 0             # Counter for refreshes

while True:
    refresh_count += 1
    print(f"🔄 Refresh #{refresh_count}")

    # Refresh the page (F5)
    pyautogui.press('f5')

    # Wait for the page to load
    time.sleep(refresh_delay)

    # Select all and copy (Ctrl+A, Ctrl+C)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.2)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)

    # Read clipboard content
    text = pyperclip.paste()

    # Check if keyword is found
    if any(keyword.lower() in text for keyword in keywords):
    #if keyword.lower() in text.lower():
        print(f"✅ Found one of the keywords {keywords} after {refresh_count} refreshes!")
        print("🐝 Bee. bee... bee.")
        # Bee-like beeping sounds
        winsound.Beep(1000, 200)
        time.sleep(0.2)
        winsound.Beep(800, 200)
        time.sleep(0.4)
        winsound.Beep(1000, 300)
        break
