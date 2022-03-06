# Documentación Rebotines
Componente Personalizado con QT y Python
## Antes que nada decir que es mejor ver el código o descargarlo desde el [repositorio](https://github.com/Casta626/Trabajo-4-DIN).
## Tambiém puedes descargarlo desde la ventana de comandos con el comando:
pip install -i https://test.pypi.org/simple/ rebotines==0.1
### El código de rebotines es bastante simple, se divide en tres archivos:
## ui_rebotines.py
### Aquí esta todo el código que se refiere a la interfaz, si quieres contribuir puedes modificar lo que quieras siempre y cuando no afecte luego a los test (más adelante los enseñaré), este es su código:
      from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
          QMetaObject, QObject, QPoint, QRect,
          QSize, QTime, QUrl, Qt)
      from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
          QCursor, QFont, QFontDatabase, QGradient,
          QIcon, QImage, QKeySequence, QLinearGradient,
          QPainter, QPalette, QPixmap, QRadialGradient,
          QTransform)
      from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
          QSizePolicy, QSlider, QStatusBar, QToolBar,
          QWidget)
      import recursos

      class Ui_MainWindow(object):

          def setupUi(self, MainWindow):
              if not MainWindow.objectName():
                  MainWindow.setObjectName(u"MainWindow")
              MainWindow.resize(800, 600)
              self.velocidad = 750
              self.actionPlay_Resume = QAction(MainWindow)
              self.actionPlay_Resume.setObjectName(u"actionPlay_Resume")
              icon = QIcon()
              icon.addFile(u":/botones/boton-doble.png", QSize(), QIcon.Normal, QIcon.Off)
              self.actionPlay_Resume.setIcon(icon)
              self.actionStop = QAction(MainWindow)
              self.actionStop.setObjectName(u"actionStop")
              icon1 = QIcon()
              icon1.addFile(u":/botones/stop.png", QSize(), QIcon.Normal, QIcon.Off)
              self.actionStop.setIcon(icon1)
              self.actionAdvance_velocity = QAction(MainWindow)
              self.actionAdvance_velocity.setObjectName(u"actionAdvance_velocity")
              icon2 = QIcon()
              icon2.addFile(u":/botones/fast-forward.png", QSize(), QIcon.Normal, QIcon.Off)
              self.actionAdvance_velocity.setIcon(icon2)
              self.actionRewind_velocity = QAction(MainWindow)
              self.actionRewind_velocity.setObjectName(u"actionRewind_velocity")
              icon3 = QIcon()
              icon3.addFile(u":/botones/rewind.png", QSize(), QIcon.Normal, QIcon.Off)
              self.actionRewind_velocity.setIcon(icon3)
              self.centralwidget = QWidget(MainWindow)
              self.centralwidget.setObjectName(u"centralwidget")
              self.horizontalSlider = QSlider(self.centralwidget)
              self.horizontalSlider.setObjectName(u"horizontalSlider")
              self.horizontalSlider.setGeometry(QRect(10, 500, 781, 16))
              self.horizontalSlider.setOrientation(Qt.Horizontal)
              self.horizontalSlider.setStyleSheet("color:yellow")
              MainWindow.setCentralWidget(self.centralwidget)
              self.menubar = QMenuBar(MainWindow)
              self.menubar.setObjectName(u"menubar")
              self.menubar.setGeometry(QRect(0, 0, 800, 22))
              self.menuAcciones = QMenu(self.menubar)
              self.menuAcciones.setObjectName(u"menuAcciones")
              MainWindow.setMenuBar(self.menubar)
              self.statusbar = QStatusBar(MainWindow)
              self.statusbar.setObjectName(u"statusbar")
              MainWindow.setStatusBar(self.statusbar)
              self.toolBar = QToolBar(MainWindow)
              self.toolBar.setObjectName(u"toolBar")
              MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

              self.menubar.addAction(self.menuAcciones.menuAction())
              self.menuAcciones.addAction(self.actionPlay_Resume)
              self.menuAcciones.addAction(self.actionStop)
              self.menuAcciones.addAction(self.actionAdvance_velocity)
              self.menuAcciones.addAction(self.actionRewind_velocity)
              self.toolBar.addAction(self.actionStop)
              self.toolBar.addAction(self.actionRewind_velocity)
              self.toolBar.addAction(self.actionPlay_Resume)
              self.toolBar.addAction(self.actionAdvance_velocity)




              self.retranslateUi(MainWindow)

              QMetaObject.connectSlotsByName(MainWindow)
          # setupUi

          def retranslateUi(self, MainWindow):
              MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
              self.actionPlay_Resume.setText(QCoreApplication.translate("MainWindow", u"Play/Resume", None))
      #if QT_CONFIG(shortcut)
              self.actionPlay_Resume.setShortcut(QCoreApplication.translate("MainWindow", u"Toggle Media Play/Pause", None))
      #endif // QT_CONFIG(shortcut)
              self.actionStop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
      #if QT_CONFIG(shortcut)
              self.actionStop.setShortcut(QCoreApplication.translate("MainWindow", u"Media Stop", None))
      #endif // QT_CONFIG(shortcut)
              self.actionAdvance_velocity.setText(QCoreApplication.translate("MainWindow", u"Advance (velocity)", None))
      #if QT_CONFIG(shortcut)
              self.actionAdvance_velocity.setShortcut(QCoreApplication.translate("MainWindow", u"Media Next", None))
      #endif // QT_CONFIG(shortcut)
              self.actionRewind_velocity.setText(QCoreApplication.translate("MainWindow", u"Rewind (velocity)", None))
      #if QT_CONFIG(shortcut)
              self.actionRewind_velocity.setShortcut(QCoreApplication.translate("MainWindow", u"Media Previous", None))
      #endif // QT_CONFIG(shortcut)
              self.menuAcciones.setTitle(QCoreApplication.translate("MainWindow", u"Actions", None))
              self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
          # retranslateUi 
  ## rebotines.py
  ### Esta clase es la que se encarga de cargar los métodos y funciones al componente, si quieres contribuir puedes modificar lo que quieras siempre y cuando no afecte luego a los test (más adelante los enseñaré) y esta clase a su vez se divide principalmente en dos funciones:
  #### La función generaImagen:
  ##### Esta función se encarga de obtener el nombre del archivo, el tipo de archivo (png, jpg, etc) y el tamaño de escalado de la imagen (al ser una versiuón beta quizas cueste recortar la imagen y ponerlo a una grande, con una pequeña no debería de dar problemas), dicho esto este es su código:
    def generaImagen(self,imgdata, imgtype, sizex): 
  
        self.sizex = 100
        self.imgtype ='jpg'
        self.img = QImage.fromData(imgdata, imgtype) 
        self.img.convertToFormat(QImage.Format_ARGB32) 
    
        self.imgsize = min(self.img.width(), self.img.height()) 
        rect = QRect( 
            (self.img.width() - self.imgsize) / 2, 
            (self.img.height() - self.imgsize) / 2, 
            self.imgsize, 
            self.imgsize, 
        ) 
        
        self.img = self.img.copy(rect) 
    
        self.out_img = QImage(self.imgsize, self.imgsize, QImage.Format_ARGB32) 
        self.out_img.fill(Qt.transparent) 
    
        self.brush = QBrush(self.img) 
    
        self.painter = QPainter(self.out_img) 
        self.painter.setBrush(self.brush) 
    
        self.painter.setPen(Qt.NoPen) 
    
        self.painter.drawEllipse(0, 0, self.imgsize, self.imgsize) 
        
        self.painter.end() 
    
        self.pr = QWindow().devicePixelRatio() 
        self.pm = QPixmap.fromImage(self.out_img) 
        self.pm.setDevicePixelRatio(self.pr) 
        sizex *= self.pr 
        self.pm = self.pm.scaled(sizex, sizex, Qt.KeepAspectRatio,  
                                Qt.SmoothTransformation) 
        return self.pm
   #### La función __init__:
   ##### Esta es la función padre donde se obtienen los datos de generaImagen y se realizan todas las operaciones, las funciones a destacar son las últimas que son los getters y setters y aquí su código:
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
        
        self.imgpath = "amsiedad.jpg"

        self.imgtype = "jpg"

        self.sizex = 25

        # self.imagenes("kk.png", "png", 56)

        print(self.imgpath)
        print(self.imgtype)
        print(self.sizex)
        
        self.imgdata = open(self.imgpath, 'rb').read() 
        
        self.pixmap = self.generaImagen(self.imgdata,self.imgtype,self.sizex) 
        
        self.bola = QLabel(self) 
        
        self.bola.setPixmap(self.pixmap) 
        
        self.bola.move(0, altura/2)

        self.horizontalSlider.setValue(600)
        

        # self.velocidad = self.horizontalSlider.value()

        self.anim = QPropertyAnimation(self.bola, b"pos")
        self.anim.setEndValue(QPoint(anchura/4, altura-74))
        # self.anim.setDuration(self.gestorVelocidad(self.velocidad))
        self.anim.setDuration(750)

        self.anim_2 = QPropertyAnimation(self.bola, b"pos")
        self.anim_2.setEndValue(QPoint(anchura-100, altura*2/5))
        # self.anim_2.setDuration(self.gestorVelocidad(self.velocidad))
        self.anim_2.setDuration(750)

        self.anim_3 = QPropertyAnimation(self.bola, b"pos")
        self.anim_3.setEndValue(QPoint(anchura*2/5, 54)) #Ahora hay que añadir 54 pixeles por la toolbar y la actionBar
        # self.anim_3.setDuration(self.gestorVelocidad(self.velocidad))
        self.anim_3.setDuration(750)

        self.anim_4 = QPropertyAnimation(self.bola, b"pos")
        self.anim_4.setEndValue(QPoint(0, altura/2))
        # self.anim_4.setDuration(self.gestorVelocidad(self.velocidad))
        self.anim_4.setDuration(750)

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
        
        # self.anim_group.start()
        # self.anim_group.pause()
        # self.anim_group.resume()
        # self.anim_group.stop() # Lo para por completo
        
        self.loops = 2

        self.anim_group.setLoopCount(self.loops)
        self.anim_group.start() # Solo falta ajustar la variable de velocidad para que la pille los .setDuration al momento que se cambia 

        self.horizontalSlider.setGeometry(QRect(50, altura-100, anchura-100, 16))
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(10000)

        self.bool = True
        self.bool2 = True

        self.actionPlay_Resume.triggered.connect(self.gestorAnimacion)
        self.actionStop.triggered.connect(self.gestorParado)
        self.actionAdvance_velocity.triggered.connect(self.aumentarVelocidad)
        self.actionRewind_velocity.triggered.connect(self.disminuirVelocidad)


        self.horizontalSlider.valueChanged.connect(self.gestorVelocidad)

        stl = """{
                margin = 0,
                bg_size = 20,
                bg_radius = 1e,
                bg color = "#1ble23",
                bg_color_hover = "#1e2229",
                handle_margin = 2,
                handle_size = 16,
                handle_radius = 8,
                handle color = "#568af2",
                handle_color_hover = "#6c99f4",
                handle_color_pressed = "#3f6fd1"
                }"""

        self.horizontalSlider.setStyleSheet("color:yellow")

    def gestorVelocidad(self, velocidad):
        print(self.horizontalSlider.value())
        self.velocidad = 10000 - velocidad
        return velocidad

    def gestorVelocidad2(self):
        self.anim_group.start()              

    def aumentarVelocidad(self):
        self.velocidad += 500
        print(self.velocidad)
    
    def disminuirVelocidad(self):
        self.velocidad -= 500
        print(self.velocidad)

    def gestorParado(self):
        if self.bool2 ==True:
            self.anim_group.stop()
            self.bool2 = False
        else:
            self.anim_group.start()
            self.bool2 = True

    
    def gestorAnimacion(self):
        if self.bool ==True:
            self.anim_group.pause()
            self.bool = False
        else:
            self.anim_group.resume()
            self.bool = True

    def getImage(self):
        return self.imgpath
    def setImage(self, img):
        self.imgpath = img
    def getImageType(self):
        return self.imgtype
    def setImageType(self, extension):
        self.imgtype = extension
    def getImageSize(self):
        return self.sizex
    def setImageSize(self, size):
        self.sizex = size

    def getLoop(self):
        return self.loops
    def setLoop(self, loop):
        self.loops = loop

    
    value1 = Property(str, getImage, setImage)
    value2 = Property(str, getImageType, setImageType)
    value3 = Property(int, getImageSize, setImageSize)
    value4 = Property(int, getLoop, setLoop)
    
   ## test.py
   ### Como su nombre indica esta es la clase donde se prueban los test despues de hacer las modificaciones que creas convenientes para mejorar el componente asegurate de que los test se ejecutan sin dar problemas (además de que la aplicación compile), aquí esta su código:
    from PySide6 import QtWidgets
    from rebotines import MainWindow

    class Window(QtWidgets.QMainWindow):

        def __init__(self):
            super().__init__()
            mainToggle = MainWindow()
            mainToggle.imgpath = "cocos.png"
            mainToggle.imgtype = "png"
            mainToggle.imgsize = 120
            mainToggle.imgdata = open(mainToggle.imgpath, 'rb').read() 
            mainToggle.pixmap = mainToggle.generaImagen(mainToggle.imgdata,mainToggle.imgtype,mainToggle.imgsize)
            self.setCentralWidget(mainToggle)



    app = QtWidgets.QApplication([])
    w = Window()
    w.show()
    app.exec()
   ### Para que los test funcionen hay que instalar dependencias en el ordenador desde la ventana de comandos, utiliza:
   pip install unitest
   pip install pytest
   
   ## Por último está el archivp rebotines_demo.py que en él se encuentra una forma de instanciarlo, pero igualmente la dejo por aquí:
      from PySide6 import QtWidgets
      from rebotines import MainWindow

      class Window(QtWidgets.QMainWindow):

          def __init__(self):
              super().__init__()
              mainToggle = MainWindow()
              mainToggle.setLoop(2)
              mainToggle.setImage("amsiedad.png")
              mainToggle.setImageType("png")
              mainToggle.setImageSize(120)
              self.setCentralWidget(mainToggle)
        
        

      app = QtWidgets.QApplication([])
      w = Window()
      w.show()
      app.exec()
   
   
  
