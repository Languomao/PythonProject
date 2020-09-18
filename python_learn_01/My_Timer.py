import time as t

class MyTimer:
    def __init__(self):
        self.prompt = "首先开始计时。。。"
        self.unit = ['年', '月', '天', '时', '分', '秒']
        self.lasted = []
        self.begin_time = 0
        self.end_time = 0

    def __str__(self):
        return self.prompt

    __repr__ = __str__

    """开始计时"""
    def start(self):
        self.begin_time = t.localtime()
        self.prompt = "请先结束计时..."
        print("计时开始。。。")

    """计时结束"""
    def stop(self):
        if not self.begin_time:
            print("先开始计时....")
        else:
            self.end_time = t.localtime()
            self._calc()
            print("计时结束。。。")

    """内部方法，计算运行时间"""
    def _calc(self):
        self.lasted = []
        self.prompt = "总共运行了"
        for index in range(6):
            self.lasted.append(self.end_time[index] - self.begin_time[index] + self.unit[index])
            if self.lasted[index]:
                self.prompt += str(self.lasted[index])
