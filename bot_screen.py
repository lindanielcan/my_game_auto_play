import tkinter
from tkinter import messagebox


class BotScreen:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.geometry("750x250")

        self.button = tkinter.Button(text='启动脚本', width=10, command=self.run_the_robot)
        self.button.grid(row=0, column=0)

        self.button1 = tkinter.Button(text='暂停脚本', width=10, command=self.proceed_or_pause)
        self.button1.grid(row=0, column=1)

        self.button2 = tkinter.Button(text='停止脚本', width=10, command=self.stop_the_robot)
        self.button2.grid(row=0, column=2)

        self.pause_or_proceed = False
        self.robot_on = False

    def proceed_or_pause(self):

        """pause or proceed the robot."""

        if self.robot_on:
            if not self.pause_or_proceed:
                self.button1['text'] = '继续脚本'
                print('The robot is proceeded.'
                      '继续运行脚本')
                self.pause_or_proceed = True
            else:
                self.button1['text'] = '暂停脚本'
                print('The robot is paused.'
                      '已暂停脚本')
                self.pause_or_proceed = False
        else:
            print('The robot is not running.'
                  '无法暂停脚本因为脚本已经停止或还没有启动.')

    def run_the_robot(self):

        """Start the robot"""

        if not self.robot_on:

            warning_box = messagebox.askquestion(title=None, message='你确定要启动脚本吗?')
            if warning_box == 'yes':
                self.robot_on = True
                print('脚本正在启动。')

            # print(self.robot_on)

    def stop_the_robot(self):

        """Stop the robot"""

        if self.robot_on:

            warning_box = messagebox.askquestion(title=None, message='你确定要停止脚本吗?')

            if warning_box == 'yes':
                self.robot_on = False
                self.button1['text'] = '暂停脚本'
                self.pause_or_proceed = False
                print('脚本已停止。')

        # print(self.robot_on)
