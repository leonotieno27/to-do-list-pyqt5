from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("TO DO LIST APP")
        self.setGeometry(100, 100, 600, 350)
        self.UiComponents()

    def UiComponents(self):
        self.label = QLabel(self) 
        self.label.setGeometry(5, 5, 590, 250)
        self.label.setWordWrap(True)

        self.label.setStyleSheet(
            "QLabel"
            "{"
            "border : 2px solid grey;"
            "background : white"
            "}"
        )
        self.label.setAlignment(Qt.AlignRight)
        self.label.setFont(QFont('Times New Roman', 15))

        #buttons
        add_task = QPushButton("Add Task", self)
        add_task.setGeometry(5,280, 80, 40)
        

        edit_task = QPushButton("Edit Task", self)
        edit_task.setGeometry(100,280, 80, 40)

        delete_task = QPushButton("Delete Task", self)
        delete_task.setGeometry(195, 280, 80, 40)

        button_effect = QGraphicsColorizeEffect()
        button_effect.setColor(Qt.red)
        delete_task.setGraphicsEffect(button_effect)

        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()