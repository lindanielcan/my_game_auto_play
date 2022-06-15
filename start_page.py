import tkinter as tk
from tkinter import ttk
from task_page import TaskPage



# 欢迎使用页面。

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text='欢迎使用梦幻西游手游脚本.')
        label.grid(row=0, column=0, padx=130, pady=(100, 0))

        button1 = ttk.Button(self, text="开始使用脚本",
                             command=lambda: controller.show_frame(TaskPage))
        button1.grid(row=1, column=0, padx=180, pady=10)

