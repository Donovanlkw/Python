pip install pyperclip

import keyboard
import pyperclip
import time

keyword = "Guildford"

while True:
    # Select all and copy (simulate Ctrl+A, Ctrl+C)
    keyboard.press_and_release('ctrl+a')
    time.sleep(0.2)
    keyboard.press_and_release('ctrl+c')
    time.sleep(0.5)  # Wait a moment for clipboard to update

    # Get clipboard text
    text = pyperclip.paste()

    # Check for keyword
    if keyword.lower() in text.lower():
        print(f"Found keyword: {keyword}")
        break

    print("Keyword not found. Refreshing...")
    keyboard.press_and_release('f5')  # Refresh page
    time.sleep(5)  # Wait before next check
