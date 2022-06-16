import time

import pyautogui
from random import randint
from bot_screen import BotScreen
from mouse_action import MouseAction
from image_action import ImageAction
from keyboard_action import KeyboardAction


class Bot:
    def __init__(self):
        self.window = BotScreen()
        self.mouse_actions = MouseAction()
        self.image_actions = ImageAction()
        self.keyboard_actions = KeyboardAction()

    def find_and_click(self, image, error_message="Can't find the image", number_of_clicks=1):
        """find the image location and click"""
        self.mouse_actions.mouse_position = self.image_actions.image_does_exist(image, error_message)

        if self.mouse_actions.mouse_position is not None:

            self.mouse_actions.move_mouse_to_and_click(self.mouse_actions.mouse_position[0],
                                                       self.mouse_actions.mouse_position[1],
                                                       number_of_clicks)
            return True
        else:
            return False

    def read_each_screen(self, method=None):
        """iterate through each screen and perform a task."""

        for a in range(1, 6):
            if self.find_and_click('images/1.png', "Can't find the image. 无法找到该图片"):
                # **********************************
                screen_x_coordinates = [
                    (self.mouse_actions.mouse_position[0] - 350),
                    (self.mouse_actions.mouse_position[0] - 150),
                    (self.mouse_actions.mouse_position[0]),
                    (self.mouse_actions.mouse_position[0] + 200),
                    (self.mouse_actions.mouse_position[0] + 400)
                ]
                y = int(self.mouse_actions.mouse_position[1]) - 80
                # **********************************

                self.mouse_actions.move_mouse_to_and_click(screen_x_coordinates[a - 1], y, 1)

                # maximize each screen
                self.find_and_click("images/maximize.png", "can not find the image")

                # *************************************************************
                # add task code here.

                # method()

                # minimize each screen
                self.find_and_click('images/minimize.png', "can not find the image")

    def normalize_screens(self):
        """Normalizing all the screens after maximizing all the screens."""

        for a in range(1, 6):
            if self.find_and_click('images/1.png', "Can't find the image. 无法找到该图片"):
                # **********************************
                screen_x_coordinates = [
                    (self.mouse_actions.mouse_position[0] - 350),
                    (self.mouse_actions.mouse_position[0] - 150),
                    (self.mouse_actions.mouse_position[0]),
                    (self.mouse_actions.mouse_position[0] + 200),
                    (self.mouse_actions.mouse_position[0] + 400)
                ]
                y = int(self.mouse_actions.mouse_position[1]) - 80
                # **********************************

                self.mouse_actions.move_mouse_to_and_click(screen_x_coordinates[a - 1], y, 1)

                # maximize each screen
                self.find_and_click("images/regularize.png", "can not find the image")

                # *************************************************************
                # add task code here.

                # *************************************************************

        if self.find_and_click('images/multiple_screen_icon.png', "Can't find multiple_screen_icon.png on the screen."):
            self.find_and_click('images/8.png')
            self.find_and_click('images/9.png')

    def check_for_image_while_scrolling(self, mouse_move_to_this_position, image1='', image2=''):

        time.sleep(randint(1000, 2000) / randint(1000, 2000))

        pyautogui.moveTo(mouse_move_to_this_position[0], mouse_move_to_this_position[1])

        pyautogui.scroll(randint(400, 600))

        time.sleep(randint(1000, 2000) / randint(1000, 2000))

        pyautogui.scroll(randint(400, 600))

        time.sleep(randint(1000, 2000) / randint(1000, 2000))

        while True:
            time.sleep(randint(1000, 2000) / randint(1000, 2000))
            if self.find_and_click(image1):
                if image2 != '':
                    self.find_and_click(image2)
                return True
            pyautogui.scroll(-200)

    def get_wish_task(self):
        """祈福"""

        pass

# time.sleep(2)
# print(pyautogui.position())
#
# # Point(x=1054, y=1064)
#
# # 1. Point(x=745, y=980)
# # 2. Point(x=904, y=990)
# # 3. Point(x=1055, y=974)
# # 4.
# # 5.
# Point(x=663, y=367)
# Point(x=1197, y=714)
