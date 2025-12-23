"""
@brief Main file for callibration tool
@author Edwin Mwiti
@email edwin@octaviacarbon.com
"""

from PyQt5.QtCore import Qt, QSize, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWidgets import (
    QDialog,
    QStyleFactory,
    QWidget,
    QAction,
    QApplication,
    QCheckBox,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
    QTabWidget,
    QPushButton,
    QStyle
)

import os, sys, subprocess
from pathlib import Path
import time 
from wifi_handler import WiFiHandler

# resolve icons absolute paths
script_dir = Path(__file__).parent
plus_icon_path = (script_dir / '..'/'assets'/'icons'/'plus.png').resolve()

# application metadata
metadata = {
    "app_name": "EasyCallibration tool",
    "version": "v1.0"
}

# button list 
side_panel_btns = ["Connect WiFi", "Callibrate", "Add Rig", "Settings", "Help", "About", "Logout"]

# rigs list   TODO: make this a JSON with configs for each rig
rigs = ["QC", "MCR", "Microcolumns", "Prod Lab"]

class Rig():
    def __init__(self):
        self.name = ""
        self.sensor_list = []

    def set_name(self, rig_name):
        self.name = rig_name
        
    def get_name(self):
        return self.name

    def start_calibration(self):
        pass

    def fetch_sensor_list(self):
        return self.sensor_list

    def end_calibration(self):
        pass
    
    def get_calibration_log(self):
        # todo: read from a file 
        return "calibration log"

    def update_calibration_log(self, line):
        # todo: update callibration log with line, line is created dynamically 
        pass

class QCRig(Rig):
    def __init__(self):
        super().__init__()
        self.set_name("QCRig")

        # placeholder for sensors
        s = ["Sprint IR 1", "Sprint IR 2", "K30 1", "K30 2"]

        for n, sensor in enumerate(s):
            sensor_id = str(n) + '_' + sensor
            self.sensor_list.append(sensor_id)

    def set_name(self, n):
        self.name = n

    def get_name(self):
        return self.name

    def fetch_sensor_list(self):
        return self.sensor_list

class MCRRig(Rig):
    def __init__(self):
        super().__init__()
        self.set_name("MCRRig")

    def set_name(self, n):
        self.name = n

    def get_name(self):
        return self.name

# create instances of Rigs 
qc_rig = QCRig()
mcr_rig = MCRRig()

rig_instances = [qc_rig, mcr_rig]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
      
        self.side_panel_btn_config = {
            'minimum_width': 150,
        }

        self.gui_spin_up()

    def configure_side_panel_push_buttons(self, button, config):
        """ apply configuration from a dictionary to a QPushButton """
        if 'minimum_width' in config:
            button.setMinimumWidth(config['minimum_width'])

    def update_status_bar(self):
        
        pass

    def gui_spin_up(self):
        self.setWindowTitle(metadata.get("app_name") + " " + metadata.get("version"))
        self.setFixedSize(QSize(1200, 700))
        self.setMinimumSize(QSize(600, 500))
        self.setMaximumSize(QSize(1200, 700))

        # create layouts
        self.parent_layout = QHBoxLayout()
        self.side_panel_layout = QVBoxLayout()
   
        self.main_panel_layout = QVBoxLayout()
        self.main_panel_title_layout = QHBoxLayout()
        self.rig_tabs_layout = QVBoxLayout()

        # add app title to panel title layout 
        app_title = QLabel(metadata.get("app_name") + " " + metadata.get("version"))
        self.main_panel_title_layout.addWidget(app_title)

        # populate tabs layout with widgets
        self.rig_tabs = QTabWidget()
        self.rig_tabs.setTabPosition(QTabWidget.North)
        self.rig_tabs.setMovable(False)
        self.rig_tabs.setIconSize(QSize(20, 20))

        ########################### PANES ###########################
        self.create_rig_panes()

        # append tabs layout to main_panel_layout
        self.main_panel_layout.addLayout(self.rig_tabs_layout)
        self.main_panel_layout.addWidget(self.rig_tabs)

        # create side panel push buttons
        self.create_side_panel_buttons()

        # main panel widgets
        self.create_main_panel_widgets()

        # arrange layouts
        self.parent_layout.addLayout(self.side_panel_layout)
        self.parent_layout.addLayout(self.main_panel_layout)

        # create status bar 
        self.status_bar = QStatusBar(self)
        self.status_bar.showMessage("Not connected", 0)
        self.setStatusBar(self.status_bar)

        self.update_status_bar()

        main_widget = QWidget()
        main_widget.setLayout(self.parent_layout)
        self.setCentralWidget(main_widget)

    def create_side_panel_buttons(self):
        for button in side_panel_btns:
            btn = QPushButton(button)
            self.configure_side_panel_push_buttons(btn, self.side_panel_btn_config)
            self.side_panel_layout.addWidget(btn)

            # add slots 
            if (button == "Connect WiFi"):
                btn.clicked.connect(self.connect_button_clicked)

        # tight look on buttons
        self.side_panel_layout.insertStretch(-1,1) 
        self.side_panel_layout.setSpacing(30)

    def create_main_panel_widgets(self):
        self.main_panel_tabs = QTabWidget()

    def create_rig_panes(self):
        for i, rig_inst in enumerate(rig_instances):
            pane_name = rig_inst.get_name()

            # display a list of available sensors on each rig
            sensor_list_layout = QVBoxLayout()

            lbl = QLabel("Available sensors")
            sensor_list_layout.addWidget(lbl)

            for gas_sensor in rig_inst.fetch_sensor_list():
                sensor_btn = QPushButton(gas_sensor)
                sensor_btn.setMinimumWidth(300)
                sensor_list_layout.addWidget(sensor_btn)
           
            page = QWidget(self)
            sensor_list_layout.addStretch()
            sensor_list_layout.setContentsMargins(0,40,0,0)
            sensor_list_layout.setAlignment(Qt.AlignCenter)
            page.setLayout(sensor_list_layout)

            self.rig_tabs.addTab(page, pane_name)

        # ####### new Rig pane ############
        new_rig_page = QWidget(self)
        lbl = QLabel("Add new Rig")
        new_rig_page_layout = QHBoxLayout()
        new_rig_page.setLayout(new_rig_page_layout)  
        new_rig_page_layout.addWidget(lbl)

        add_pane_index = i + 1
        self.rig_tabs.addTab(new_rig_page, "Add")
        self.rig_tabs.setTabIcon(add_pane_index, QIcon(str(plus_icon_path)))

    def connect_button_clicked(self, s):
        print("click",s )

        connect_dlg = WiFiHandler()

        if connect_dlg.exec():
            print("Success")
        else :
            print("Cancel")
        
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()

    # apply theming styles
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # dark theme
    #style_path = os.path.join(current_dir, 'dark-style.qss')

    # light theme
    style_path = os.path.join(current_dir, 'light-style.qss')

    with open(style_path, 'r') as f:
        _style = f.read()
        app.setStyleSheet(_style)

    app.exec()