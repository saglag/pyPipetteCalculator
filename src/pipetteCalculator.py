# Form implementation generated from reading ui file 'pipetteCalculator.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_PipetteCalculator(object):
    def setupUi(self, PipetteCalculator):
        PipetteCalculator.setObjectName("PipetteCalculator")
        PipetteCalculator.resize(827, 272)
        self.centralwidget = QtWidgets.QWidget(parent=PipetteCalculator)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked= lambda: self.calculate_pipette_entry())
        self.pushButton.setGeometry(QtCore.QRect(40, 196, 313, 31))
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(41, 41, 313, 151))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.manipulator_angle = QtWidgets.QLineEdit(parent=self.widget)
        self.manipulator_angle.setObjectName("manipulator_angle")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.manipulator_angle)
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.cell_depth = QtWidgets.QLineEdit(parent=self.widget)
        self.cell_depth.setObjectName("cell_depth")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cell_depth)
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.glass_distance = QtWidgets.QLineEdit(parent=self.widget)
        self.glass_distance.setObjectName("glass_distance")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.glass_distance)
        self.label_4 = QtWidgets.QLabel(parent=self.widget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.x_start = QtWidgets.QLineEdit(parent=self.widget)
        self.x_start.setObjectName("x_start")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.x_start)
        self.z_start = QtWidgets.QLineEdit(parent=self.widget)
        self.z_start.setObjectName("z_start")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.z_start)
        self.label_5 = QtWidgets.QLabel(parent=self.widget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.widget1 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(381, 40, 305, 114))
        self.widget1.setObjectName("widget1")
        self.formLayout_2 = QtWidgets.QFormLayout(self.widget1)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setHorizontalSpacing(5)
        self.formLayout_2.setVerticalSpacing(9)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_6 = QtWidgets.QLabel(parent=self.widget1)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.cell_entry = QtWidgets.QLabel(parent=self.widget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cell_entry.setFont(font)
        self.cell_entry.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.cell_entry.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.cell_entry.setLineWidth(2)
        self.cell_entry.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.cell_entry.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.cell_entry.setObjectName("cell_entry")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cell_entry)
        self.label_7 = QtWidgets.QLabel(parent=self.widget1)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_7)
        self.glass_entry = QtWidgets.QLabel(parent=self.widget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.glass_entry.setFont(font)
        self.glass_entry.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.glass_entry.setLineWidth(2)
        self.glass_entry.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.glass_entry.setObjectName("glass_entry")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.glass_entry)
        self.label_8 = QtWidgets.QLabel(parent=self.widget1)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_8)
        self.x_tar = QtWidgets.QLabel(parent=self.widget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.x_tar.setFont(font)
        self.x_tar.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.x_tar.setLineWidth(2)
        self.x_tar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.x_tar.setObjectName("x_tar")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.x_tar)
        self.z_tar = QtWidgets.QLabel(parent=self.widget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.z_tar.setFont(font)
        self.z_tar.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.z_tar.setLineWidth(2)
        self.z_tar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.z_tar.setObjectName("z_tar")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.z_tar)
        self.label_9 = QtWidgets.QLabel(parent=self.widget1)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_9)
        PipetteCalculator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=PipetteCalculator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 827, 20))
        self.menubar.setObjectName("menubar")
        PipetteCalculator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=PipetteCalculator)
        self.statusbar.setObjectName("statusbar")
        PipetteCalculator.setStatusBar(self.statusbar)

        self.retranslateUi(PipetteCalculator)
        QtCore.QMetaObject.connectSlotsByName(PipetteCalculator)

    def retranslateUi(self, PipetteCalculator):
        _translate = QtCore.QCoreApplication.translate
        PipetteCalculator.setWindowTitle(_translate("PipetteCalculator", "Pipette Entry Calculator"))
        self.pushButton.setText(_translate("PipetteCalculator", "Calcuate"))
        self.label.setText(_translate("PipetteCalculator", "Manipulator angle (degrees):"))
        self.label_2.setText(_translate("PipetteCalculator", "Cell depth (um):"))
        self.label_3.setText(_translate("PipetteCalculator", "Cell distance from glass (um):"))
        self.label_4.setText(_translate("PipetteCalculator", "Manipulator X start:"))
        self.label_5.setText(_translate("PipetteCalculator", "Manipulator Z start:"))
        self.label_6.setText(_translate("PipetteCalculator", "Brain entry distance from cell (um):"))
        self.cell_entry.setText(_translate("PipetteCalculator", "0"))
        self.label_7.setText(_translate("PipetteCalculator", "Brain entry distance from glass (um):"))
        self.glass_entry.setText(_translate("PipetteCalculator", "0"))
        self.label_8.setText(_translate("PipetteCalculator", "X target:"))
        self.x_tar.setText(_translate("PipetteCalculator", "0"))
        self.z_tar.setText(_translate("PipetteCalculator", "0"))
        self.label_9.setText(_translate("PipetteCalculator", "Z target:"))
    
    # do some math
    def calculate_pipette_entry(self):
        try:
            try:
                manipulator_angle = float(self.manipulator_angle.text())
            except:
                manipulator_angle = 20
                print("No angle entered, set to:", manipulator_angle)
            try:
                cell_depth = float(self.cell_depth.text())
            except:
                cell_depth = 150
            try:
                cell_distance_glass = float(self.glass_distance.text())
            except:
                cell_distance_glass = 150
            try:
                x_start = int(self.x_start.text())
            except:
                x_start = 0
            try:
                z_start = int(self.z_start.text())
            except:
                z_start = 0
            # Math!\
            import math       
            
            # convert from degrees to radians
            beta_angle = math.radians(90)
            gamma_angle = math.radians(70)
            manipulator_angle = math.radians(float(manipulator_angle))
            
            # Calculate base distance of entry
            distance_from_cell = (cell_depth * math.sin(gamma_angle)) / (math.sin(manipulator_angle))
            
            # Pipette distance from glass
            pipette_distance_from_glass = distance_from_cell - cell_distance_glass
            
            # X target
            x_tar = x_start - pipette_distance_from_glass
            z_tar = z_start + cell_depth
            
            # Output the measurements
            self.cell_entry.setText(str(int(distance_from_cell)))
            self.glass_entry.setText(str(int(pipette_distance_from_glass)))
            self.x_tar.setText(str(int(x_tar)))
            self.z_tar.setText(str(int(z_tar)))
            
        except:
            self.cell_entry.setText("Error")
                
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PipetteCalculator = QtWidgets.QMainWindow()
    ui = Ui_PipetteCalculator()
    ui.setupUi(PipetteCalculator)
    PipetteCalculator.show()
    sys.exit(app.exec())
