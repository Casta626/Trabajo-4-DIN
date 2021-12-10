import unittest, pytest
from PySide6 import QtCore
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QWidget
from animated_toggle import AnimatedToggle

class AnimatedToggleTestCase(unittest.TestCase):

   def test_sizeHint(self):
       app = QApplication([])
       window = QWidget()
       result = AnimatedToggle().sizeHint()
       self.assertEqual(result, QSize(58, 45))

@pytest.fixture
def animated_toggle(qtbot):
    test_animated_toggle = AnimatedToggle()
    qtbot.addWidget(test_animated_toggle)
    return test_animated_toggle

def test_initial_status(animated_toggle):
    assert animated_toggle.isChecked() == False

def test_postclick_status(animated_toggle,qtbot):
    qtbot.mouseClick(animated_toggle, QtCore.Qt.LeftButton)
    assert animated_toggle.isChecked() == True

if __name__ == '__main__':
    unittest.main()