import tkinter as tk


class APP:
    def __init__(self, master):
        # 使用框架将组件分组
        frame = tk.Frame(master)
        frame.pack()

        self.hi_button = tk.Button(frame, text='say hello', fg='blue', command=self.say_hi)
        self.hi_button.pack()

    def say_hi(self):
        print('hello....')


# 创建一个tkinter的实例
root = tk.Tk()
app = APP(root)

root.mainloop()
