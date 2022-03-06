import unittest

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QWidget
from animated_toggle import AnimatedToggle

class AnimatedToggleTestCase(unittest.TestCase):

   def test_sizeHint(self):
       app = QApplication([])
       window = QWidget()
       result = AnimatedToggle().sizeHint()
       self.assertEqual(result, QSize(58, 45))

if __name__ == '__main__':
    unittest.main()