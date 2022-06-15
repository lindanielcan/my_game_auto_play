import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


# 任务页面。
class TaskPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button1 = ttk.Button(self, text="任务页面",
                             command=lambda: controller.show_frame(TaskPage))
        button1.grid(row=0, column=0)

        button2 = ttk.Button(self, text="进度页面",
                             command=lambda: controller.show_frame(ProgressPage))
        button2.grid(row=0, column=1)

        self.canvas = tkinter.Canvas(self, width=500, height=2, bg="black")
        self.canvas.grid(row=1, column=0, columnspan=10, padx=0, pady=0)

        label = ttk.Label(self, text="总任务栏")
        label.grid(row=2, column=0)

        self.listbox1 = tkinter.Listbox(self)
        self.listbox1.insert(0, "打宝图以及挖宝图")
        self.listbox1.insert(1, "押镖")
        self.listbox1.grid(row=3, column=0)

        self.listbox1.bind('<Double-1>', self.listbox_events_1)

        self.label = ttk.Label(self, text="需要完成\n的任务")
        self.label.grid(row=2, column=1)

        self.label = ttk.Label(self, text="双击在总任务栏里\n的任务来加添加任务到\n需要完成的任务栏里")
        self.label.grid(row=3, column=1)

        self.listbox2 = tkinter.Listbox(self)
        self.listbox2.grid(row=3, column=2)

        self.listbox2.bind('<Double-1>', self.listbox_events_2)

        self.button = ttk.Button(self, text='启动脚本', width=10, command=self.run_the_robot)
        self.button.grid(row=4, column=0, padx=0)

        self.button1 = ttk.Button(self, text='暂停脚本', width=10, command=self.proceed_or_pause)
        self.button1.grid(row=4, column=1)

        self.button2 = ttk.Button(self, text='停止脚本', width=10, command=self.stop_the_robot)
        self.button2.grid(row=4, column=2)

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

    def listbox_events_1(self, event):
        cs = self.listbox1.curselection()

        for list in cs:

            if list == 0:
                if not self.is_task_in_listbox1_exist_in_listbox2(list):
                    self.listbox2.insert(self.listbox2.size(), self.listbox1.get(list))
            elif list == 1:
                if not self.is_task_in_listbox1_exist_in_listbox2(list):
                    self.listbox2.insert(self.listbox2.size(), self.listbox1.get(list))

    def listbox_events_2(self, event):

        cs = self.listbox2.curselection()

        for list in cs:
            if list == 0:
                self.listbox2.delete(list)
            elif list == 1:
                self.listbox2.delete(list)

    def is_task_in_listbox1_exist_in_listbox2(self, index):

        for a in range(0, self.listbox2.size()):
            if self.listbox1.get(index) == self.listbox2.get(a):
                return True
        return False


# 进度页面。
class ProgressPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button1 = ttk.Button(self, text="任务页面",
                             command=lambda: controller.show_frame(TaskPage))
        button1.grid(row=0, column=0)

        button2 = ttk.Button(self, text="进度页面",
                             command=lambda: controller.show_frame(ProgressPage))
        button2.grid(row=0, column=1)

        self.canvas = tkinter.Canvas(self, width=500, height=2, bg="black")
        self.canvas.grid(row=1, column=0, columnspan=10, padx=0, pady=0)


