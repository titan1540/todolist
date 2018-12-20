import os
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog
from PyQt5.QtWidgets import QDesktopWidget, QMessageBox

from initial import Ui_Initial
from workplace import Ui_WorkPlace


class Initial(QMainWindow, Ui_Initial):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle('ToDoList')
        self.setWindowIcon(QIcon('icon.png'))
        self.center()

        self.todo = ''
        files = list(os.walk(os.getcwd()))[0][2]
        lst = ['']
        for i in files:
            if i.split('.')[-1] == 'todo':
                lst.append(i)
        self.listTodo.addItems(lst)

        self.openTodoButtom.clicked.connect(self.open_todo)
        self.newTodoButtom.clicked.connect(self.showDialog)
        self.listTodo.activated[str].connect(self.choice_todo)

        self.show()

    def new_todo(self):
        pass

    def open_todo(self):
        global window
        window = WorkPlace(self.todo)
        self.close()

    def choice_todo(self, todo):
        self.todo = todo

    def showDialog(self):
        name, ok = QInputDialog.getText(self, 'Названеи заметки',
                                        'Введите название файла:')

        if ok:
            global window
            window = WorkPlace(name)
            self.close()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class WorkPlace(QMainWindow, Ui_WorkPlace):
    def __init__(self, file_name):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Initial()
    sys.exit(app.exec_())
