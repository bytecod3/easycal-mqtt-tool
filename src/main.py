"""
@brief Main file for callibration tool
@author Edwin Mwiti
@email edwin@octaviacarbon.com
"""

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWidgets import (
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
import os
from pathlib import Path

# resolve icons absolute paths
script_dir = Path(__file__).parent
plus_icon_path = (script_dir / '..'/'assets'/'icons'/'plus.png').resolve()

# application metadata
metadata = {
    "app_name": "EasyCallibration tool",
    "version": "v1.0"
}

# button list 
side_panel_btns = ["Callibrate", "Add Rig", "Settings", "Help", "About", "Logout"]

# rigs list   TODO: make this a JSON with configs for each rig
rigs = ["QC", "MCR", "Microcolumns", "Prod Lab"]



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.gui_spin_up()

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
        rig_tabs = QTabWidget()
        rig_tabs.setTabPosition(QTabWidget.North)
        rig_tabs.setMovable(False)
        rig_tabs.setIconSize(QSize(20, 20))

        ########################### PANES ###########################
        ########## QC Rig pane ############ 
        qc_rig_page = QWidget(self)
        lbl = QLabel("This is QC rig")
        qc_rig_page_layout = QHBoxLayout()
        qc_rig_page.setLayout(qc_rig_page_layout)  
        qc_rig_page_layout.addWidget(lbl)

        ####### MCR Rig pane ############
        mcr_rig_page = QWidget(self)
        lbl = QLabel("This is MCR rig")
        mcr_rig_page_layout = QHBoxLayout()
        mcr_rig_page.setLayout(mcr_rig_page_layout)  
        mcr_rig_page_layout.addWidget(lbl)

        ####### Microcolumns Rig pane ############
        microcolumns_rig_page = QWidget(self)
        lbl = QLabel("This is microcolumns rig")
        microcolumns_rig_page_layout = QHBoxLayout()
        microcolumns_rig_page.setLayout(microcolumns_rig_page_layout)  
        microcolumns_rig_page_layout.addWidget(lbl)

        ####### new Rig pane ############
        new_rig_page = QWidget(self)
        lbl = QLabel("Add new Rig")
        new_rig_page_layout = QHBoxLayout()
        new_rig_page.setLayout(new_rig_page_layout)  
        new_rig_page_layout.addWidget(lbl)

        ########## Consolidate all panes ###########
        rig_tabs.addTab(qc_rig_page, "QC Rig")
        rig_tabs.addTab(mcr_rig_page, "MCR Rig")
        rig_tabs.addTab(microcolumns_rig_page, "Microcolumns Rig")


        new_rig_index = rig_tabs.count()
        print(new_rig_index)
        rig_tabs.addTab(new_rig_page, "Add")
        rig_tabs.setTabIcon(new_rig_index, QIcon(str(plus_icon_path)))
        #rig_tabs.setTabIcon(new_rig_index, rig_tabs.style().standardIcon(QStyle.SP_FileDialogNewFolder))
        #rig_tabs.setTabToolTip(new_rig_index, "Add new rig")

        # append tabs layout to main_panel_layout
        self.main_panel_layout.addLayout(self.rig_tabs_layout)
        self.main_panel_layout.addWidget(rig_tabs)

        # create side panel push buttons 
        # self.callibrate_btn = QPushButton("Callibrate")
        # self.settings_btn = QPushButton("Add rig")
        # self.settings_btn = QPushButton("Settings")
        # self.help_btn = QPushButton("Help")
        # self.logout_btn = QPushButton("Logout")
        # self.side_panel_layout.addWidget(self)
        self.create_side_panel_buttons()

        # main panel widgets
        self.create_main_panel_widgets()

        # arrange layouts
        self.parent_layout.addLayout(self.side_panel_layout)
        self.parent_layout.addLayout(self.main_panel_layout)

        main_widget = QWidget()
        main_widget.setLayout(self.parent_layout)
        self.setCentralWidget(main_widget)

    def create_side_panel_buttons(self):
        for button in side_panel_btns:
            btn = QPushButton(button)
            self.side_panel_layout.addWidget(btn)

        # tight look on buttons
        self.side_panel_layout.insertStretch(-1,1) 
        self.side_panel_layout.setSpacing(30)

    def create_main_panel_widgets(self):
        self.main_panel_tabs = QTabWidget()

            

app = QApplication([])
window = MainWindow()
window.show()
app.exec()