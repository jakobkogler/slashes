from slashes import execute_code
import sys
#from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QShortcut
from PyQt5.QtGui import QTextCursor, QKeySequence
from mainwindow import Ui_MainWindow


class InterpreterWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.intermedBox.hide()
        self.step_counter = 0

        self.runButton.clicked.connect(self.runCode)
        self.run_shortcut = QShortcut(QKeySequence("Ctrl+R"), self)
        self.run_shortcut.activated.connect(self.runCode)
        self.stepButton.clicked.connect(self.stepCode)
        self.step_shortcut = QShortcut(QKeySequence("Ctrl+S"), self)
        self.step_shortcut.activated.connect(self.stepCode)
        self.resetButton.clicked.connect(self.resetSteps)
        self.reset_shortcut = QShortcut(QKeySequence("Ctrl+C"), self)
        self.reset_shortcut.activated.connect(self.resetSteps)
        self.increaseSize.clicked.connect(self.increaseTextSize)
        self.decreaseSize.clicked.connect(self.decreaseTextSize)

    def runCode(self):
        self.intermedBox.hide()
        self.resultTextEdit.clear()
        code = self.codeTextEdit.toPlainText()
        execute_code(code, int(self.limitationLineEdit.text()), self.appendToResultTextEdit, False, self.intermediateTextEdit.setPlainText)
        if self.intermediateTextEdit.toPlainText():
            self.intermedBox.show()

    def stepCode(self):
        if self.step_counter == 0:
            self.intermedBox.show()
            self.resultTextEdit.clear()
            self.intermediateTextEdit.clear()
            code = self.codeTextEdit.toPlainText()
        else:
            code = self.intermediateTextEdit.toPlainText()
        
        self.step_counter += 1
        execute_code(code, int(self.limitationLineEdit.text()), self.appendToResultTextEdit, True, self.intermediateTextEdit.setPlainText) 

    def appendToResultTextEdit(self, text):
        self.resultTextEdit.moveCursor(QTextCursor.End)
        self.resultTextEdit.insertPlainText(text)
        self.resultTextEdit.moveCursor(QTextCursor.End)

    def resetSteps(self):
        self.step_counter = 0
        self.resultTextEdit.clear()
        self.intermediateTextEdit.clear()

    def increaseTextSize(self):
        for text_edit in [self.codeTextEdit, self.resultTextEdit, self.intermediateTextEdit]:
            font = text_edit.font()
            size = font.pointSize() + 1
            font.setPointSize(size)
            text_edit.setFont(font)

    def decreaseTextSize(self):
        for text_edit in [self.codeTextEdit, self.resultTextEdit, self.intermediateTextEdit]:
            font = text_edit.font()
            size = font.pointSize() - 1
            font.setPointSize(size)
            text_edit.setFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = InterpreterWindow()
    window.show()
    sys.exit(app.exec_())
