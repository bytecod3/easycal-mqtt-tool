
from PyQt5.QtCore import QLine, QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget


# widgets demo 
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget
)

# application metadata
metadata = {
    "app_name": "EasyCallibration tool",
    "version": "v1.0"

}

# subclass QMainWindow to customize applications main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # create widgets
        self.gui_spin_up()

    def gui_spin_up(self):
        self.setWindowTitle(metadata.get("app_name") + " " + metadata.get("version"))
        button = QPushButton("Press me")
        self.setFixedSize(QSize(1200, 700))
        self.setMinimumSize(QSize(600, 500))
        self.setMaximumSize(QSize(1200, 700))


        layout = QVBoxLayout()
        widgets = [
            QCheckBox,
            QComboBox,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit,
            ]

        # for w in widgets:
        #     layout.addWidget(w())

        widget = QLabel("Hello")
        font = widget.font()
        font.setPointSize(60) 
        widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.setCentralWidget(widget)

    def test_gui(self):
        self.button = QPushButton("Click")

        # self.button.clicked.connect(self.test_push_button_clicked)
        #button.clicked.connect(self.test_push_button_toggled)

        #self.setCentralWidget(self.button)

        #line edit - direct connection of signals and slots 
        """
        self.label = QLabel()
        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        
        container = QWidget();
        container.setLayout(layout)

        # set the central widget of the window
        self.setCentralWidget(container)
        
    def test_push_button_clicked(self):
        self.button.setText("You already clicked me")
        self.button.setEnabled(False)

    def test_push_button_toggled(self, checked):
        self.button_is_checked = checked
        print(self.button_is_checked) """

    def contextMenuEvent(self,e):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(e.globalPos())


app = QApplication([])

window = MainWindow()
window.show()

app.exec()