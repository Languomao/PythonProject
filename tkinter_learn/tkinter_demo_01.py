import tkinter as tk

app = tk.Tk()
app.title('languomao test.')
theLabel = tk.Label(app, text='Test Window')
#
theLabel.pack()

# 进入窗口的主事件循环
app.mainloop()