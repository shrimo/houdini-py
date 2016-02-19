import json
import os
import sys
from PySide import QtGui, QtCore

_lsel = []
  
class LoadSelect(QtGui.QMainWindow):
    
    def __init__(self):
        super(LoadSelect, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)       
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()
        
    def showDialog(self):

        f_name, _ = QtGui.QFileDialog.getOpenFileName(self, 'Open file',
                    '/home/victor/Documents/PointsOfPower/selected')
        
        with open(f_name) as jdf:
            _lsel = json.load(jdf)
        for _name in _lsel:
            #print _name
            snode=hou.node(_name)
            snode.setSelected(True)

            
exe=LoadSelect()
exe.show()
