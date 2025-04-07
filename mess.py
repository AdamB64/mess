import time
import pyautogui

# Delay to allow the user to position the cursor
time.sleep(5)

# Text to be typed
typing_text="work"

# Loop 100 times

for _ in range(4000):
    pyautogui.press("enter")
    pyautogui.write(typing_text, interval=0.000000000000001)
    # Simulate Enter key
    pyautogui.press("enter")

pyautogui.press("enter")
pyautogui.write("sorry joel", interval=0.1)