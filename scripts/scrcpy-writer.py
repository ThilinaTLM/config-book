#!/usr/bin/env python

from os import system

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QShortcut

app = QApplication([])
win = QWidget()
win.setWindowTitle("CopyPaste")
win.setWindowFlag(Qt.FramelessWindowHint + Qt.WindowStaysOnTopHint)
win.setGeometry(300, 300, 300, 30)

edit = QLineEdit(win)
edit.setGeometry(0, 0, 300, 30)



def moveText():
   wTitle = "SM-J701F" 
   content = str(edit.text())
   system(f'echo -n "{content}" | xclip -selection clipboard')
   system(f'wmctrl -a {wTitle} && xdotool key ctrl+shift+v')
   system(f'wmctrl -a CopyPaste')

def moveTextAndSend():
   wTitle = "SM-J701F"
   content = str(edit.text())
   system(f'echo -n "{content}" | xclip -selection clipboard')
   system(f'wmctrl -a {wTitle} && xdotool key ctrl+shift+v Tab Tab Return')
   system(f'wmctrl -a CopyPaste')

def close():
   quit()

sline = QShortcut(QKeySequence("Return"), win)
sline.activated.connect(moveText)

smsg = QShortcut(QKeySequence("Ctrl+Return"), win)
smsg.activated.connect(moveTextAndSend)

shortcut = QShortcut(QKeySequence("Esc"), win)
shortcut.activated.connect(close)

win.show()
app.exec_()
