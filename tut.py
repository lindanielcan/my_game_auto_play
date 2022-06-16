import pyautogui
import time
from random import randint
from datetime import datetime

#
# time.sleep(2)
# while True:
#     pos = pyautogui.locateOnScreen('images/17.png', confidence=0.8)
#     if pos is not None:
#         time.sleep(0.5)
#         pyautogui.moveTo(pos[0], pos[1])
#         pyautogui.click()

time.sleep(3)

while datetime.now().strftime("%Y-%m-%d %H:%M:%S  ") != '2022-06-16 11:22:27  ':

    pos1 = pyautogui.locateOnScreen('images/18.png', confidence=0.8)
    pos2 = pyautogui.locateOnScreen('images/19.png', confidence=0.8)
    pos6 = pyautogui.locateOnScreen('images/22.png', confidence=0.8)

    if pos1 is not None and pos2 is not None:
        time.sleep(randint(1000, 2000) / randint(1000, 2000))

        pyautogui.moveTo(pos2[0], pos2[1])

        time.sleep(randint(1000, 2000) / randint(1000, 2000))

        pyautogui.click()

        time.sleep((randint(1000, 2000) / randint(1000, 2000)) + randint(5, 7))

        pos3 = pyautogui.locateOnScreen('images/20.png', confidence=0.8)

        pyautogui.moveTo(pos3[0], pos3[1])

        time.sleep(randint(1000, 2000) / randint(1000, 2000))

        pyautogui.click()

        time.sleep((randint(1000, 2000) / 2000) + randint(1, 3))

        pyautogui.click()

        pos4 = pyautogui.locateOnScreen('images/21.png', confidence=0.8)

        pyautogui.moveTo(pos4[0], pos4[1])

        time.sleep(randint(1000, 2000) / randint(1000, 2000))

        pyautogui.click()


    elif pos1 is None and pos2 is None and pos6 is not None:
        pyautogui.moveTo(pos6[0], pos6[1])

        time.sleep(randint(1000, 2000) / randint(1000, 2000))

        pyautogui.click()
