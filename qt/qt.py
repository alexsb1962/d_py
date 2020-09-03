# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
import form
import sys


class App(QtWidgets.QMainWindow, form.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле form.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна


def StartGUI():
    app = QtWidgets.QApplication(sys.argv)
    win = App()
    win.show()
    app.exec()


# !/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, random
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QRect, QThread
import time


class common():
    rect_on = False

    mainrect = QRect()
    mainrect.setRect(300, 300, 800, 450)

    rect = QRect()
    rect.setRect(50, 50, 400, 250)
    radius = 30


class Example(QWidget):

    def __init__(self,common):
        super().__init__()
        self.initUI(common)

    def initUI(self,common):
        self.setGeometry(common.mainrect)
        self.setWindowTitle('Points')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.SomeDraw(qp)
        qp.end()

    def SomeDraw(self, qp):
        qp.setPen(Qt.red)
        size = self.size()

        if common.rect_on:
            qp.drawRect(common.rect)
        else:
            qp.drawRoundedRect(common.rect, common.radius, common.radius)

        for i in range(1000):
            x = random.randint(1, size.width() - 1)
            y = random.randint(1, size.height() - 1)
            qp.drawPoint(x, y)


class Worker(QThread):

    wid = None

    def __init__(self, Widget=None):
        super().__init__()
        self.wid = Widget

    def run(self):
        # здесь то и исполняется основной код
        st = time.time()
        while (True):
            common.rect_on = not common.rect_on
            self.wid.update()
            time.sleep(0.1)
            if (time.time() - st) > 5:
                break

        print('End of circle')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # common класс для хранения настроек геометрии
    ex = Example(common)

    # передаю ссылку на виджет через конструктор
    w = Worker(ex)
    # а можно и так
    w = Worker()
    w.wid=ex

    w.start()

    sys.exit(app.exec_())
