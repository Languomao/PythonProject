import threading
import time

exitFlag = 0


class MyThread(threading.Thread):
    def __init__(self, threadName, threadID, counter):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.threadID = threadID
        self.counter = counter

    def run(self):
        print("开始线程：" + self.threadName)
        print_time(self.threadName, self.counter, 5)
        print("退出线程：" + self.threadName)


def print_time(threadName, counter, delay):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


mythread1 = MyThread("Thread-1", 1, 5)
mythread2 = MyThread("Thread-2", 2, 4)

mythread1.start()
mythread2.start()
mythread1.join()
mythread2.join()
