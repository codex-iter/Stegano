import sys
from PyQt5.QtWidgets import *  #QApplication ,QMainWindow, QWidget, QPushButton, QToolTip,QDesktopWidget ,QMessageBox
from PyQt5.QtGui import *  #QIcon,QFont
from PyQt5.QtCore import Qt

modeSet="default"
class Center(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        hbox = QHBoxLayout(self)

        topleft = QFrame(self)
        algo=QLabel("Choose Algo",topleft)
        algo.move(2,5)
        combo=QComboBox(topleft)
        combo.move(70,0)
        combo.addItem("Algo1")
        combo.addItem("Algo2")
        combo.addItem("Algo3")
        combo.addItem("Algo4")
        combo.addItem("Algo5")
        topleft.setFrameShape(QFrame.StyledPanel)

        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)
        splitter1.resize(self.sizeHint())
        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
        splitter2.resize(self.sizeHint())

        hbox.addWidget(splitter2)

        self.setLayout(hbox)

class GUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('SteganoV:0.1 ,AlgoCount:2,Encryption:N/A,Med:Img')
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('Read Instructions to Use this program correctly')
        Embed= QAction(QIcon('Embed.png'),'Write/Embed',self)
        Retreive= QAction(QIcon('Retreive.png'),'Read/Verify',self)
        self.toolbar=self.addToolBar('Write/Embed')
        self.toolbar.addAction(Embed)
        self.toolbar.addAction(Retreive)
        #self.toolbar.setOrientation(Qt.Vertical)
        Embed.setToolTip('Write Data into your medium.')
        Retreive.setToolTip('Read Data from your medium.')


        readWidget=Center
        writeWidget=Center

        Central=Center()
        self.setCentralWidget(Central)
        self.setGeometry(300, 300, 300, 320)
        self.setWindowTitle('Stegano')
        self.setWindowIcon(QIcon('Logo PNG.png'))
        self.center()
        self.show()

    def closeEvent(self, event):                      #redifining close event for simple message box
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):                                   #centering on screen
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = GUI()
    sys.exit(app.exec_())
