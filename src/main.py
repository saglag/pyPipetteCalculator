# -*- coding: utf-8 -*-
"""
Main file for pyPipetteCalculator

"""

import sys
from PyQt6.QtWidgets import (
    QApplication, 
    QLabel, 
    QWidget, 
    QFormLayout, 
    QLineEdit,
    QDialog,
    QMainWindow,
    QVBoxLayout
)

WINDOW_SIZE = 800
DISPLAY_HEIGHT = 800
class PipetteCalcWindow(QMainWindow):
    """Pipette Calculator's main window (GUI)."""
    
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("Pipette Calculator")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)
        self.generalLayout = QVBoxLayout()
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self._createDisplay()
        self._createButtons()




def main():
 """Pipette Calculator's main function"""
    app = QApplication([])
    window = PipetteCalcWindow()
    window.show()
    sys.exit(app.exec())
    dialogLayout = QVBoxLayout()
    formLayout = QFormLayout()
    window = QWidget()
    window.setWindowTitle("Pipette Calculator")
    
    layout = QFormLayout()
    layout.addRow("Manipulator Angle (degrees):", QLineEdit())
    layout.addRow("Cell depth (um):", QLineEdit())
    layout.addRow("Cell distance from glass (um):", QLineEdit())
    layout.addRow("Manipulator X start:", QLineEdit())
    layout.addRow("Manipulator Z start:", QLineEdit())
    window.setLayout(layout)


if __name__ == "__main__":
    main()
