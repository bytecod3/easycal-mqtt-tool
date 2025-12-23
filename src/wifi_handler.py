"""

@brief custom dialog box for WIFI connection
@author Edwin Mwiti

"""

from os import waitstatus_to_exitcode
import subprocess
import sys
import time
from PyQt5.QtCore import QLine, Qt, QSize
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QLabel, QListWidget, QCheckBox, QHBoxLayout, QListWidgetItem, QVBoxLayout, QLineEdit, QPushButton

class WiFiHandler(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Connect to WiFi")
        self.wifi_networks = []

        self.gui_spin_up()
        self.scan_networks()
        self.populate_network_list()
          
        self.connection_status = 0

    def gui_spin_up(self):
        self.setFixedSize(QSize(600, 500))

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
        self.show_password_checkbox.toggled.connect(self.toggle_password_visibility)
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

        # append parent layout
        layout.addWidget(self.network_list_widget)
        self.setLayout(layout)

    def scan_networks(self):
        self.wifi_networks.clear()

        try:
            if sys.platform.startswith('win'):
                time.sleep(0.4)
                command = ['netsh', 'wlan', 'show','networks']
                output = subprocess.check_output(command, stderr=subprocess.STDOUT, text=True)

                #extract SSIDs
                current_ssid = None
                ssids = []

                for line in output.splitlines():
                    #print(line)
                    line = line.strip()

                    if line.startswith("SSID"):
                        parts = line.split(":", 1)
                        if len(parts) == 2:
                            current_ssid = parts[1].strip()
                            if current_ssid and current_ssid not in ssids:
                                ssids.append(current_ssid)


                # add each network individually to network list 
                for ssid in ssids:
                    self.wifi_networks.append(ssid)

        except subprocess.CalledProcessError as e:
            self.wifi_networks.append(f"Error scanning: {e.output}")
        except Exception as e:
            self.wifi_netwks.append(f"An error occured: {e}")

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

    def is_password_required(self, network_name):
        """ check if network requires password """
        pass


    def on_network_selected(self, item):
        """ handle network selection """
        network_name = item.data(Qt.UserRole) or item.text()
        self.selected_label.setText(network_name)

        # auto focus password field 
        self.password_input.setFocus()

    def on_network_double_clicked(self, item):
        """ connect immediately on double click """
        network_name = item.data(Qt.UserRole) or item.text()
        self.selected_label.setText(network_name)

        # for open networks, no password 
        if self.is_open_network(network_name):
            self.connect_to_network(network_name, "")

    def is_open_network(self, network_name):
        """ check if network is open or not """
        # todo: implement open check logic
        pass

    def toggle_password_visibility(self, checked):
        """ toggle password visibility"""
        if checked:
            self.password_input.setEchoMode(QLineEdit.Normal)
        else:
            self.password_input.setEchoMode(QLineEdit.Password)


    def accept_connection(self):
        """ handle OK button clicks"""
        selected_items = self.network_list_widget.selectedItems()
        if not selectected_items:
            QMessageBox.warning(self, "No selection","Please select a network first")

    def connect_to_wifi(self):
        """ connect to the selected network """
        pass 