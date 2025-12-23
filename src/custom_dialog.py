"""

@brief custom dialog box for WIFI connection
@author Edwin Mwiti

"""

from os import waitstatus_to_exitcode
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QLabel, QListWidget, QCheckBox, QHBoxLayout, QListWidgetItem, QVBoxLayout, QLineEdit, QPushButton

class CustomDialog(QDialog):
    def __init__(self, wifi_networks=None):
        super().__init__()
        self.setWindowTitle("Connect to WiFi")
        self.wifi_networks = wifi_networks if wifi_networks is not None else []

        self.gui_spin_up()
        self.populate_network_list()

    def gui_spin_up(self):

        layout = QVBoxLayout()

        # show selected item
        self.network_list_widget = QListWidget()
        self.network_list_widget.itemClicked.connect(self.on_network_selected)
        self.network_list_widget.itemDoubleClicked.connect(self.on_network_double_clicked)

        # show selected WIFI network
        selected_layout = QHBoxLayout()
        selected_layout.addWidget(QLabel("Selected:"))
        self.selected_label = QLabel("None")
        selected_layout.addWidget(self.selected_label)
        selected_layout.addStretch()
        layout.addLayout(selected_layout)

        # password selection 
        layout.addWidget(QLabel("Password:"))
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setPlaceholderText("Password")
        layout.addWidget(self.password_input)

        # show/hide password checkbox
        self.show_password_checkbox = QCheckBox("Show password")
        #self.show_password_checkbox.toggled.connect(self.toggle_password_visibility)
        layout.addWidget(self.show_password_checkbox)

        # buttons 
        button_layout = QHBoxLayout()

        # refresh button 
        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.clicked.connect(self.refresh_networks)
        button_layout.addWidget(self.refresh_button)
        

        # connect button
        self.connect_button = QPushButton("Connect")
        self.connect_button.clicked.connect(self.connect_to_wifi)
        button_layout.addWidget(self.connect_button)

        button_layout.addStretch()
        layout.addLayout(button_layout)
        

        # dialog buttons
        # QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel 
        # self.button_box = QDialogButtonBox(QBtn)

        # self.button_box.accepted.connect(self.accept)
        # self.button_box.rejected.connect(self.reject)
        # layout.addWidget(self.button_box)

        # append parent layout
        layout.addWidget(self.network_list_widget)
        self.setLayout(layout)

    def refresh_networks(self):
        pass

    def populate_network_list(self):
        self.network_list_widget.clear()

        if not self.wifi_networks:
            item = QListWidgetItem("No networks found")
            item.setFlags(Qt.NoItemFlags)
            self.network_list_widget.addItem(item)
            return

        for network in self.wifi_networks:
            item = QListWidgetItem(network)

            item.setData(Qt.UserRole, network)

            self.network_list_widget.addItem(item)



    def on_network_selected(self):
        pass

    def on_network_double_clicked(self):
        pass

    def connect_to_wifi(self):
        pass