from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit


def handleCalc():
    print('开始处理..')


# 提供了整个图形界面程序的底层管理功能
app = QApplication([])

window = QMainWindow()
window.resize(500, 400)
window.move(300, 310)
window.setWindowTitle('薪资统计')

textEdit = QPlainTextEdit(window)
textEdit.setPlaceholderText("请输入薪资表")
textEdit.move(10, 25)
textEdit.resize(300, 350)

button = QPushButton('统计', window)
button.move(380, 80)
button.clicked.connect(handleCalc)

# 执行show方法将窗口展现
window.show()

# 进入事件处理循环，死循环，等待用户结束
app.exec_()
