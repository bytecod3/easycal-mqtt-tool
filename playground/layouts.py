import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QStackedLayout, QPushButton

from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import QSize

from app import QPushButton
from layout_colorwidget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setFixedSize(QSize(700, 500))
        self.setWindowTitle("Layouts")

        # vertical layout 
        # layout = QVBoxLayout()
        # layout.addWidget(Color('red'))
        # layout.addWidget(Color('green'))
        # layout.addWidget(Color('blue'))

        # nested layout 
        # layout1 = QHBoxLayout()
        # layout2 = QVBoxLayout()
        # layout3 = QVBoxLayout()

        # layout1.setContentsMargins(10,10,10,10)
        # layout1.setSpacing(5)

        # layout2.addWidget(Color('red'))
        # layout2.addWidget(Color('yellow'))
        # layout2.addWidget(Color('purple'))

        # layout1.addLayout(layout2)
        # layout1.addWidget(Color('green'))

        # layout3.addWidget(Color('red'))
        # layout3.addWidget(Color('purple'))

        # layout1.addLayout(layout3)

        # # stacked layout
        # layout = QStackedLayout()
        # layout.addWidget(Color('red'))
        # layout.addWidget(Color('green'))
        # layout.addWidget(Color('blue'))
        # layout.addWidget(Color('yellow'))

        # layout.setCurrentIndex(2)

        # tabs demo
        page_layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.stacklayout = QStackedLayout()

        page_layout.addLayout(button_layout)
        page_layout.addLayout(self.stacklayout)

        btn = QPushButton('red')
        btn.pressed.connect(self.activate_tab_1)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Color('red'))

        btn = QPushButton('green')
        btn.pressed.connect(self.activate_tab_2)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Color('green'))

        btn = QPushButton('yellow')
        btn.pressed.connect(self.activate_tab_3)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Color('yellow'))

        widget = QWidget()
        widget.setLayout(page_layout)
        self.setCentralWidget(widget)

    def activate_tab_1(self):
        self.stacklayout.setCurrentIndex(0)

    def activate_tab_2(self):
        self.stacklayout.setCurrentIndex(1)

    def activate_tab_3(self):
        self.stacklayout.setCurrentIndex(2)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()