from PySide6.QtCore import QRect, QPropertyAnimation, QPoint, QSize, QSequentialAnimationGroup
from PySide6.QtGui import QImage, QBrush, QPainter, QWindow, QPixmap, Qt
from PySide6.QtWidgets import QLabel, QWidget, QApplication, QSlider, QGroupBox, QMainWindow
import sys

from rebotines import Ui_MainWindow
  
def mask_image(imgdata, imgtype ='png', size = 64): 
  
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
   
class MainWindow(Ui_MainWindow,QWidget): 
    
    def __init__(self): 
        super().__init__()
        self.setupUi(self)
        # if not self.objectName():
        #     self.setObjectName(u"MainWindow")
        # self.resize(500, 335)
        # self.centralwidget = QWidget(self)
        # self.centralwidget.setObjectName(u"centralwidget")
        # self.verticalLayout = self(self.centralwidget)
        # self.verticalLayout.setObjectName(u"verticalLayout")
        # self.groupBox = QGroupBox(self.centralwidget)
        # self.groupBox.setObjectName(u"groupBox")

        # self.verticalLayout.addWidget(self.groupBox)

        # self.horizontalSlider = QSlider(self.centralwidget)
        # self.horizontalSlider.setObjectName(u"horizontalSlider")
        # self.horizontalSlider.setOrientation(Qt.Horizontal)

        # self.verticalLayout.addWidget(self.horizontalSlider)

        # self.setCentralWidget(self.centralwidget)        
        # self.setGeometry(100, 100, 600, 400) 
        
        # imgpath = "perro.png"
        
        # imgdata = open(imgpath, 'rb').read() 
        
        # pixmap = mask_image(imgdata) 
        
        # self.bola = QLabel(self) 
        
        # self.bola.setPixmap(pixmap) 
        
        # self.bola.move(0, 45)

        # self.anim = QPropertyAnimation(self.bola, b"pos")
        # self.anim.setEndValue(QPoint(0, 0))
        # self.anim.setDuration(250)

        # self.anim_2 = QPropertyAnimation(self.bola, b"pos")
        # self.anim_2.setEndValue(QPoint(50, 50))
        # self.anim_2.setDuration(50)

        # self.anim_3 = QPropertyAnimation(self.bola, b"pos")
        # self.anim_3.setEndValue(QPoint(100, 100))
        # self.anim_3.setDuration(250)

        # self.anim_4 = QPropertyAnimation(self.bola, b"pos")
        # self.anim_4.setEndValue(QPoint(150, 150))
        # self.anim_4.setDuration(250)

        # self.anim_5 = QPropertyAnimation(self.bola, b"pos")
        # self.anim_5.setEndValue(QPoint(200, 200))
        # self.anim_5.setDuration(250)

        # self.anim_group = QSequentialAnimationGroup()
        # # Grupo de animación paralela
        # # self.anim_group = QParallelAnimationGroup()
        # self.anim_group.addAnimation(self.anim)
        # self.anim_group.addAnimation(self.anim_2)
        # self.anim_group.addAnimation(self.anim_3)
        # self.anim_group.addAnimation(self.anim_4)
        # self.anim_group.addAnimation(self.anim_5)
        # self.anim_group.start()
  
if __name__ == '__main__':   
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle('Rebotines')
    window.show()
    app.exec()