# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rebotines.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

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
        self.actionComenzar = QAction(MainWindow)
        self.actionComenzar.setObjectName(u"actionComenzar")
        icon = QIcon()
        icon.addFile(u":/botones/boton-de-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionComenzar.setIcon(icon)
        self.actionPausar = QAction(MainWindow)
        self.actionPausar.setObjectName(u"actionPausar")
        icon1 = QIcon()
        icon1.addFile(u":/botones/boton-de-pausa.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionPausar.setIcon(icon1)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(10, 500, 781, 16))
        self.horizontalSlider.setOrientation(Qt.Horizontal)
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
        self.menuAcciones.addAction(self.actionComenzar)
        self.menuAcciones.addAction(self.actionPausar)
        self.toolBar.addAction(self.actionComenzar)
        self.toolBar.addAction(self.actionPausar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionComenzar.setText(QCoreApplication.translate("MainWindow", u"Comenzar", None))
#if QT_CONFIG(shortcut)
        self.actionComenzar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.actionPausar.setText(QCoreApplication.translate("MainWindow", u"Pausar", None))
#if QT_CONFIG(shortcut)
        self.actionPausar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+T", None))
#endif // QT_CONFIG(shortcut)
        self.menuAcciones.setTitle(QCoreApplication.translate("MainWindow", u"Acciones", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

