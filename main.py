from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys  
task_dict = {}    

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("TO DO LIST APP")
        self.setGeometry(100, 100, 600, 350)
        self.UiComponents()

    def UiComponents(self):
        layout = QVBoxLayout()

        self.list_widget = QListWidget(self)
        self.update_task_list()
        layout.addWidget(self.list_widget)

        hint = QLabel("Select task first to edit or delete task")
        layout.addWidget(hint) 

        # Buttons
        add_task = QPushButton("Add Task", self)
        layout.addWidget(add_task)

        edit_task = QPushButton("Edit Task", self)
        layout.addWidget(edit_task)

        delete_task = QPushButton("Delete Task", self)
        layout.addWidget(delete_task)

        button_effect = QGraphicsColorizeEffect()
        button_effect.setColor(Qt.red)
        delete_task.setGraphicsEffect(button_effect)

        # layout to the main window's central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # actions to buttons
        add_task.clicked.connect(self.add_window)
        edit_task.clicked.connect(self.edit_window)
        delete_task.clicked.connect(self.delete_window)


    #functions for actions
    def add_window(self):
        text, ok = QInputDialog.getText(self, "Add New Task", "Enter your task:")
        if ok:
            position = len(task_dict) + 1
            task_dict[position] = text
            print(task_dict)

            self.list_widget.clear()
            for pos, task in task_dict.items():
                self.list_widget.addItem(f"Task {pos}: {task}")

    def update_task_list(self):
        self.list_widget.clear()
        for key, task in task_dict.items():
            self.list_widget.addItem(f"Task {key}: {task}")
              
    def edit_window(self):
        selected_item = self.list_widget.currentItem()
        if selected_item:
            task_text = selected_item.text()
            key = int(task_text.split()[1][:-1])
            current_task = task_dict[key]
            new_text, ok = QInputDialog.getText(self, "Edit task","Edit the task:",text=current_task)
            if ok and new_text:
                task_dict[key] = new_text
                self.update_task_list()
        
    def delete_window(self):
        selected_item = self.list_widget.currentItem()
        if selected_item:
            task_text = selected_item.text()
            key = int(task_text.split()[1][:-1])
            
            #delete task from dictionary
            if key in task_dict:
                del task_dict[key]

            #update list
            self.update_task_list()
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()