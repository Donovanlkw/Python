# https://www.youtube.com/watch?v=r3gxeX91izk
# start msedge --remote-debugging-port=9222 --user-data-dir="C:\tmp\edge-debug"

import pyautogui
import pyperclip
import winsound
import time
from playwright.sync_api import sync_playwright

keywords = ["2025", "driverpracticaltest"]      # Replace with your target keyword
refresh_delay = 5             # Seconds between refreshes
refresh_count = 0             # Counter for refreshes

while True:
    refresh_count += 1
    print(f"?? Refresh #{refresh_count}")

    # Refresh the page (F5)
    pyautogui.press('f5')

    # Wait for the page to load
    time.sleep(refresh_delay)

    # screen_width, screen_height = pyautogui.size()
    # pyautogui.click(screen_width // 2, screen_height // 2)  # Center click
    # time.sleep(0.5)

    # Select all and copy (Ctrl+A, Ctrl+C)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')

    # Read clipboard content
    text = pyperclip.paste()

    if any(keyword.lower() in text.lower() for keyword in keywords):
        print(f"✅ Found one of the keywords {keywords} after {refresh_count} refreshes!")
        print("🔔 Bee. bee... bee.")

        with sync_playwright() as p:
           # Connect to manually launched Edge (debug mode on port 9222)
           browser = p.chromium.connect_over_cdp("http://localhost:9222")

           # Use existing context and page (first tab)
           context = browser.contexts[0]
           page = context.pages[0]

           print(f"🖥️ Monitoring tab: {page.url}")

           # Wait for the link with text "abc" to appear (anchor tag <a>)
           print("🔍 Waiting for link with text 'Farnborough' to appear...")
           page.wait_for_selector("a:has-text('Farnborough')", timeout=0)

           # Click the link once it appears
           print("✅ Found link. Clicking it...")
           page.click("a:has-text('Farnborough')")
           winsound.Beep(1000, 200)
           winsound.Beep(800, 200)
           winsound.Beep(1000, 200)
           print("🖱️ Link clicked.")
           
              with sync_playwright() as p:
                 # Connect to manually launched Edge (debug mode on port 9222)
                 browser = p.chromium.connect_over_cdp("http://localhost:9222")
                 
                 # Use existing context and page (first tab)
                 context = browser.contexts[0]
                 page = context.pages[0]

           # break

