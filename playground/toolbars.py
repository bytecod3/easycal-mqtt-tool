## author Edwin Mwiti
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QCheckBox,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
    QAction
)

from app import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        # toolbar 
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        # connect button
        button_action = QAction(QIcon("../icons/plug-connect.png"), "Connect", self)
        button_action.setStatusTip("Connect")
        button_action.triggered.connect(self.toolbar_button_clicked)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action2 = QAction("Edit", self)
        button_action2.setStatusTip("Edit")
        button_action2.triggered.connect(self.toolbar_button_clicked)
        toolbar.addAction(button_action2)

        # create a status bar
        self.setStatusBar(QStatusBar(self))

    def toolbar_button_clicked(self, s):
        print("click", s)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()