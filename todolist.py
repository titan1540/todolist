import os
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog
from PyQt5.QtWidgets import QDesktopWidget, QMessageBox, QAction

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
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle('ToDoList - {}'.format(file_name))
        self.setWindowIcon(QIcon('icon.png'))
        self.center()

        self.file_name = file_name + '.todo'
        try:
            with open(self.file_name, mode='r', encoding='utf-8') as f:
                self.TextBlock.setPlainText(f.read())
        except Exception:
            pass

        saveAction = QAction(QIcon('icon.png'), '&Сохранить', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Сохранить изменения')
        saveAction.triggered.connect(self.saveFile)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Сохранить')
        fileMenu.addAction(saveAction)

        self.show()

    def saveFile(self):
        with open(self.file_name, mode='w', encoding='utf-8') as file:
            file.write(self.TextBlock.toPlainText())
            print(self.TextBlock.toPlainText())

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Выйти',
                                     "Вы действительно хотите выйти?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Initial()
    sys.exit(app.exec_())
