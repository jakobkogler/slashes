from slashes import execute_code
import sys
#from PyQt5.QtCore import 
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QTextCursor
from mainwindow import Ui_MainWindow


class InterpreterWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.runButton.clicked.connect(self.runCode)

    def runCode(self):
        self.resultTextEdit.clear()
        code = self.codeTextEdit.toPlainText()
        execute_code(code, False, self.appendToResultTextEdit)

    def appendToResultTextEdit(self, text):
        self.resultTextEdit.moveCursor(QTextCursor.End)
        self.resultTextEdit.insertPlainText(text)
        self.resultTextEdit.moveCursor(QTextCursor.End)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = InterpreterWindow()
    window.show()
    sys.exit(app.exec_())
