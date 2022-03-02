import ctypes
from PySide6.QtCore import QRect, QPropertyAnimation, QPoint, QSize, QSequentialAnimationGroup
from PySide6.QtGui import QImage, QBrush, QPainter, QWindow, QPixmap, Qt, QAction, QIcon
from PySide6.QtWidgets import QLabel, QWidget, QApplication, QSlider, QGroupBox, QMainWindow, QMenuBar, QMenu, QStatusBar, QToolBar
import sys

from rebotines import Ui_MainWindow
def mask_image(imgdata, imgtype ='jpg', size = 100): 
  
        image = QImage.fromData(imgdata, imgtype) 
        image.convertToFormat(QImage.Format_ARGB32) 
    
        imgsize = min(image.width(), image.height()) 
        rect = QRect( 
            (image.width() - imgsize) / 2, 
            (image.height() - imgsize) / 2, 
            imgsize, 
            imgsize, 
        ) 
        
        image = image.copy(rect) 
    
        out_img = QImage(imgsize, imgsize, QImage.Format_ARGB32) 
        out_img.fill(Qt.transparent) 
    
        brush = QBrush(image) 
    
        painter = QPainter(out_img) 
        painter.setBrush(brush) 
    
        painter.setPen(Qt.NoPen) 
    
        painter.drawEllipse(0, 0, imgsize, imgsize) 
        
        painter.end() 
    
        pr = QWindow().devicePixelRatio() 
        pm = QPixmap.fromImage(out_img) 
        pm.setDevicePixelRatio(pr) 
        size *= pr 
        pm = pm.scaled(size, size, Qt.KeepAspectRatio,  
                                Qt.SmoothTransformation) 
        return pm 
class Rebotes(QWidget, Ui_MainWindow):
    
   
    def patata(self): 
        # self.setupUi(self)
        # if not self.objectName():
        #     self.setObjectName(u"MainWindow")
        # self.resize(500, 335)    
        # self.setGeometry(100, 100, 600, 400) 


        # ancho = 1080
        # altura = 720
        self.tamaño = 100

        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()
        ancho, alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        anchura= (ancho*10)/(15*2)
        altura=(alto*10)/(15*2)
        #El valor lo multiplico por 100 y lo divido por 150 por la relación que hay en la ampliación de pantalla 
        # que trae por defecto haciendo que si la pantalla está con zoom se vea entera y si no tiene se ve con 
        # una resolucion menos.
        #La multiplicacion por 2 en las dos variables son para dividir la ventana en cuatro y así que ocupe un cuarto
        #de pantalla.

        self.setFixedWidth(anchura)
        self.setFixedHeight(altura)
        
        imgpath = "amsiedad.jpg"
        
        imgdata = open(imgpath, 'rb').read() 
        
        pixmap = mask_image(imgdata) 
        
        self.bola = QLabel(self) 
        
        self.bola.setPixmap(pixmap) 
        
        self.bola.move(0, altura/2)

        self.horizontalSlider.setValue(500)

        self.velocidad = self.horizontalSlider.value()

        self.anim = QPropertyAnimation(self.bola, b"pos")
        self.anim.setEndValue(QPoint(anchura/4, altura-74))
        self.anim.setDuration(self.velocidad)

        self.anim_2 = QPropertyAnimation(self.bola, b"pos")
        self.anim_2.setEndValue(QPoint(anchura-100, altura*2/5))
        self.anim_2.setDuration(self.velocidad)

        self.anim_3 = QPropertyAnimation(self.bola, b"pos")
        self.anim_3.setEndValue(QPoint(anchura*2/5, 54)) #Ahora hay que añadir 54 pixeles por la toolbar y la actionBar
        self.anim_3.setDuration(self.velocidad)

        self.anim_4 = QPropertyAnimation(self.bola, b"pos")
        self.anim_4.setEndValue(QPoint(0, altura/2))
        self.anim_4.setDuration(self.velocidad)

        self.anim_5 = QPropertyAnimation(self.bola, b"pos")
        self.anim_5.setEndValue(QPoint(200, 200))
        self.anim_5.setDuration(self.velocidad)

        self.anim_group = QSequentialAnimationGroup()
        # Grupo de animación paralela
        # self.anim_group = QParallelAnimationGroup()
        self.anim_group.addAnimation(self.anim)
        self.anim_group.addAnimation(self.anim_2)
        self.anim_group.addAnimation(self.anim_3)
        self.anim_group.addAnimation(self.anim_4)
        # self.anim_group.addAnimation(self.anim_5)
        # self.anim_group.start()

        # while True:
        
        self.anim_group.start()
        self.anim_group.pause()
        self.anim_group.resume()
        self.anim_group.stop() # Lo para por completo
        self.anim_group.start()
        self.anim_group.setLoopCount(5)
        if(self.anim_group.loopCount()==3):
            self.anim_group.pause()
        print(self.anim_group.loopCount())

        self.horizontalSlider.setGeometry(QRect(50, altura-100, anchura-100, 16))
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(10000)


        self.actionPlay_Resume
        # self.actionStop.triggered.connect(self.anim_group.stop())
        self.actionAdvance_velocity.triggered.connect(self.aumentarVelocidad)
        self.actionRewind_velocity.triggered.connect(self.disminuirVelocidad)
        

class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Rebotes.patata(self)
        self.tamaño = 100

        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()
        ancho, alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        anchura= (ancho*10)/(15*2)
        altura=(alto*10)/(15*2)
        #El valor lo multiplico por 100 y lo divido por 150 por la relación que hay en la ampliación de pantalla 
        # que trae por defecto haciendo que si la pantalla está con zoom se vea entera y si no tiene se ve con 
        # una resolucion menos.
        #La multiplicacion por 2 en las dos variables son para dividir la ventana en cuatro y así que ocupe un cuarto
        #de pantalla.

        self.setFixedWidth(anchura)
        self.setFixedHeight(altura)
        
        imgpath = "amsiedad.jpg"
        
        imgdata = open(imgpath, 'rb').read() 
        
        pixmap = mask_image(imgdata) 
        
        self.bola = QLabel(self) 
        
        self.bola.setPixmap(pixmap) 
        
        self.bola.move(0, altura/2)

        self.horizontalSlider.setValue(1500)
        


        self.anim = QPropertyAnimation(self.bola, b"pos")
        self.anim.setEndValue(QPoint(anchura/4, altura-74))
        self.anim.setDuration(self.gestorVelocidad(self.velocidad))

        self.anim_2 = QPropertyAnimation(self.bola, b"pos")
        self.anim_2.setEndValue(QPoint(anchura-100, altura*2/5))
        self.anim_2.setDuration(self.gestorVelocidad(self.velocidad))

        self.anim_3 = QPropertyAnimation(self.bola, b"pos")
        self.anim_3.setEndValue(QPoint(anchura*2/5, 54)) #Ahora hay que añadir 54 pixeles por la toolbar y la actionBar
        self.anim_3.setDuration(self.gestorVelocidad(self.velocidad))

        self.anim_4 = QPropertyAnimation(self.bola, b"pos")
        self.anim_4.setEndValue(QPoint(0, altura/2))
        self.anim_4.setDuration(self.gestorVelocidad(self.velocidad))

        self.anim_5 = QPropertyAnimation(self.bola, b"pos")
        self.anim_5.setEndValue(QPoint(200, 200))
        self.anim_5.setDuration(self.gestorVelocidad(self.velocidad))

        self.anim_group = QSequentialAnimationGroup()
        # Grupo de animación paralela
        # self.anim_group = QParallelAnimationGroup()
        self.anim_group.addAnimation(self.anim)
        self.anim_group.addAnimation(self.anim_2)
        self.anim_group.addAnimation(self.anim_3)
        self.anim_group.addAnimation(self.anim_4)
        # self.anim_group.addAnimation(self.anim_5)
        # self.anim_group.start()

        # while True:
        
        self.anim_group.start()
        self.anim_group.pause()
        self.anim_group.resume()
        self.anim_group.stop() # Lo para por completo
        self.anim_group.start()
        self.anim_group.setLoopCount(5)
        if(self.anim_group.loopCount()==3):
            self.anim_group.pause()
        print(self.anim_group.loopCount())

        self.horizontalSlider.setGeometry(QRect(50, altura-100, anchura-100, 16))
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(10000)


        self.actionPlay_Resume
        # self.actionStop.triggered.connect(self.anim_group.stop())
        self.actionAdvance_velocity.triggered.connect(self.aumentarVelocidad)
        self.actionRewind_velocity.triggered.connect(self.disminuirVelocidad)

        


        self.horizontalSlider.valueChanged.connect(self.gestorVelocidad)
    def gestorVelocidad(self, velocidad):
        print(self.horizontalSlider.value())
        velocidad = self.horizontalSlider.value()
        print(self.velocidad)
        return velocidad

    def aumentarVelocidad(self):
        self.velocidad += 500
        print(self.velocidad)
    
    def disminuirVelocidad(self):
        self.velocidad -= 500
        print(self.velocidad)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()