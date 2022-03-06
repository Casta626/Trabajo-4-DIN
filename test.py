import unittest
from PySide6.QtWidgets import QApplication
import sqlite3
from rebotines import MainWindow


class TestTrabajo5 (unittest.TestCase):

    def testAniadir(self):
        app=QApplication.instance()
        if app==None:
            app= QApplication([])
        
        window=MainWindow()
        window.nueva()
        window.lineEdit_DNI.setText('74125636X')
        window.lineEdit_Nombre.setText('Javier')
        window.lineEdit_Curso.setText('2 DAM')
        window.lineEdit_Apellidos.setText('Fernandez Gutierrez')
        window.lineEdit_Nota1Ev.setText('5')
        window.lineEdit_Nota2Ev.setText('6.2')
        window.lineEdit_Nota3Ev.setText('6')
        window.modificar()
        conexion=sqlite3.connect("BDDalumnos.db")
        cursor=conexion.execute("select NOMBRE from PERSONA where DNI=?", (window.lineEdit_DNI.text(), ))
        fila=cursor.fetchone()
        if fila!=None:
            print(fila)
        else:
            print("No existe una persona con dicho dni.")
        resultado = fila
        self.assertEqual(resultado[0],'Javier')
        conexion.close()

    def testEliminar(self):
        app=QApplication.instance()
        if app==None:
            app= QApplication([])
        
        window=MainWindow()
        window.fila = 0
        conexion=sqlite3.connect("BDDalumnos.db")

        cursor=conexion.execute("select NOMBRE from PERSONA where APELLIDOS=?", (window.lineEdit_Apellidos.text(), ))
        fila=cursor.fetchone()
        self.assertIsNone(fila)
        conexion.close()
        


if _name_ == '_main_':
    unittest.main()