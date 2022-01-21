import sys
from turtle import window_height, window_width
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QParallelAnimationGroup, QPropertyAnimation, QPoint, QSequentialAnimationGroup, QSize
import ctypes

from pruebas import imprimir_informacion

class Window(QWidget):
    def __init__(self):
        super().__init__()

        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()
        ancho, alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        print(ancho, alto)

        self.resize(600, 600)
        self.child = QWidget(self)
        self.child.setStyleSheet("background-color:red;border-radius:15px;")
        self.child.resize(0, 0)

        self.anim = QPropertyAnimation(self.child, b"pos")
        self.anim.setEndValue(QPoint(0, 0))
        self.anim.setDuration(2500)

        self.anim_2 = QPropertyAnimation(self.child, b"size")
        self.anim_2.setEndValue(QSize(10, 10))
        self.anim_2.setDuration(500)

        self.anim_3 = QPropertyAnimation(self.child, b"pos")
        self.anim_3.setEndValue(QPoint(ancho-10, alto-73))
        self.anim_3.setDuration(2500)

        self.anim_4 = QPropertyAnimation(self.child, b"pos")
        self.anim_4.setEndValue(QPoint(ancho-10, 0))
        self.anim_4.setDuration(2500)

        self.anim_5 = QPropertyAnimation(self.child, b"pos")
        self.anim_5.setEndValue(QPoint(0, alto-73))
        self.anim_5.setDuration(2500)

        # Grupo de animación secuencial
        self.anim_group = QSequentialAnimationGroup()
        # Grupo de animación paralela
        # self.anim_group = QParallelAnimationGroup()
        self.anim_group.addAnimation(self.anim)
        self.anim_group.addAnimation(self.anim_2)
        self.anim_group.addAnimation(self.anim_3)
        self.anim_group.addAnimation(self.anim_4)
        self.anim_group.addAnimation(self.anim_5)
        self.anim_group.start()

        print(window_height)
        print(window_width)

        

        

app = QApplication(sys.argv)
w = Window()
w.show()
app.exec()