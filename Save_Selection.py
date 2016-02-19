import json
import os
import sys
from PySide import QtGui

_sel = []

for node in hou.selectedNodes():
    _sel.append(node.path())
    #print node.path()
   
class SaveSelect(QtGui.QMainWindow):
    
    def __init__(self):
        super(SaveSelect, self).__init__()
        
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

        f_name, _ = QtGui.QFileDialog.getSaveFileName(self, 'Save file',
                    '/home/victor/Documents/PointsOfPower/selected')
        
        with open(f_name, 'wb') as outfile:
            json.dump(_sel, outfile)
            
exe=SaveSelect()
exe.show()
