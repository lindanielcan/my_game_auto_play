import time
from random import randint
import pyautogui


# from mouse_action import MouseAction


class ImageAction:
    def __init__(self):
        # self.mouse_actions = MouseAction()
        pass

    def image_does_exist(self, image, error_message='image does not exist'):
        """Finding the image on the screen, click if the image is found."""

        time.sleep(randint(1000, 2000) / randint(1000, 2000))

        position = pyautogui.locateOnScreen(image, confidence=0.9)
        # if we find the image on the screen, then it will return a list.
        if position is not None:

            return position
        # if we don't find the image on the screen, then it will print error message and return False.
        else:
            print(error_message)
            return False
