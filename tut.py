import pyautogui
import time

time.sleep(2)
print(pyautogui.position())

pyautogui.scroll(-200)
time.sleep(1)
pyautogui.scroll(-200)
time.sleep(1)

# Point(x=660, y=296)
# Point(x=1362, y=603)

print()