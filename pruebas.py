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
   
class MainWindow(QWidget): 
   
    def __init__(self): 
        super().__init__()
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

        self.anim = QPropertyAnimation(self.bola, b"pos")
        self.anim.setEndValue(QPoint(anchura/4, altura-100))
        self.anim.setDuration(750)

        self.anim_2 = QPropertyAnimation(self.bola, b"pos")
        self.anim_2.setEndValue(QPoint(anchura-100, altura*2/5))
        self.anim_2.setDuration(750)

        self.anim_3 = QPropertyAnimation(self.bola, b"pos")
        self.anim_3.setEndValue(QPoint(anchura*2/5, 0))
        self.anim_3.setDuration(750)

        self.anim_4 = QPropertyAnimation(self.bola, b"pos")
        self.anim_4.setEndValue(QPoint(0, altura/2))
        self.anim_4.setDuration(750)

        self.anim_5 = QPropertyAnimation(self.bola, b"pos")
        self.anim_5.setEndValue(QPoint(200, 200))
        self.anim_5.setDuration(750)

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
        
        

        # self.actionComenzar = QAction(MainWindow)
        # self.actionComenzar.setObjectName(u"actionComenzar")
        # icon = QIcon()
        # icon.addFile("boton-de-play.png", QSize(), QIcon.Normal, QIcon.Off)
        # self.actionComenzar.setIcon(icon)
        # self.actionPausar = QAction(MainWindow)
        # self.actionPausar.setObjectName(u"actionPausar")
        # icon1 = QIcon()
        # icon1.addFile(u":/botones/boton-de-pausa.png", QSize(), QIcon.Normal, QIcon.Off)
        # self.actionPausar.setIcon(icon1)
        # self.centralwidget = QWidget(MainWindow)
        # self.centralwidget.setObjectName(u"centralwidget")
        # self.horizontalSlider = QSlider(self.centralwidget)
        # self.horizontalSlider.setObjectName(u"horizontalSlider")
        # self.horizontalSlider.setGeometry(QRect(10, 500, 781, 16))
        # self.horizontalSlider.setOrientation(Qt.Horizontal)
        # MainWindow.setCentralWidget(self.centralwidget)
        # self.menubar = QMenuBar(MainWindow)
        # self.menubar.setObjectName(u"menubar")
        # self.menubar.setGeometry(QRect(0, 0, 800, 22))
        # self.menuAcciones = QMenu(self.menubar)
        # self.menuAcciones.setObjectName(u"menuAcciones")
        # MainWindow.setMenuBar(self.menubar)
        # self.statusbar = QStatusBar(MainWindow)
        # self.statusbar.setObjectName(u"statusbar")
        # MainWindow.setStatusBar(self.statusbar)
        # self.toolBar = QToolBar(MainWindow)
        # self.toolBar.setObjectName(u"toolBar")
        # MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        # self.menubar.addAction(self.menuAcciones.menuAction())
        # self.menuAcciones.addAction(self.actionComenzar)
        # self.menuAcciones.addAction(self.actionPausar)
        # self.toolBar.addAction(self.actionComenzar)
        # self.toolBar.addAction(self.actionPausar)
  
if __name__ == '__main__':   
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle('Rebotines')
    window.show()
    app.exec()