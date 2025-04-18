# data.txt #
'''
A=1
B=2
C=3
'''


import pyautogui
import time

# Read values from file
values = {}
with open('data.txt', 'r') as file:
    for line in file:
        key, val = line.strip().split('=')
        values[key.strip().upper()] = val.strip()

A = values.get('A', '')
B = values.get('B', '')

# Wait time to focus on the first field in the browser
print("Switch to the web form now. Starting in 5 seconds...")
time.sleep(2)

# Type and paste A
pyautogui.write(str(A))
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')

# Type and paste B
pyautogui.write(str(B))
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')
