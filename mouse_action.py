import pyautogui
import time
from random import randint


class MouseAction:
    def __init__(self):
        self.mouse_position = 0
        pass

    def move_mouse_to_and_click(self, x, y, number_of_clicks):
        """

        :param x: 图片x坐标
        :param y: 图片y坐标
        :param number_of_clicks: 点击次数
        :return:
        """

        pyautogui.moveTo(x, y)
        time.sleep(randint(1000, 2000) / randint(1000, 2000))
        for a in range(0, number_of_clicks):
            pyautogui.click()
