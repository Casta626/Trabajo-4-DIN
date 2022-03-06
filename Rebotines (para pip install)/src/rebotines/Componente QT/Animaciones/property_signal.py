from typing import ValuesView
from PySide6.QtCore import Property, QObject, Signal

class CustomObject(QObject):

    valueChanged = Signal(int)

    def __init__(self):
        super().__init__()
        self._value = 0        # valor por defecto

    # cambiamos la función setter
    @ValuesView.setter
    def value(self, value):
        # Es importante la condición
        # para que la señal no se propague si no hay un cambio real
        if value != self._value:
            self._value = value
            self.valueChanged.emit(value)