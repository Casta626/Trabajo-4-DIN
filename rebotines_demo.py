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