from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Paint")
        self.setGeometry(150,150,800,600)
        self.image=QImage(self.size(),QImage.Format_RGB32)
        self.image.fill(Qt.white)
        self.drawing=False
        self.brushSize=5
        self.brushColor=Qt.black
        self.lastPoint=QPoint()
        mainMenu=self.menuBar()
        fileMenu=mainMenu.addMenu("File")
        b_size=mainMenu.addMenu("Brush Size")
        b_color=mainMenu.addMenu("Brush Color")
        saveAction=QAction("Save",self)
        saveAction.setShortcut("Command+S")
        fileMenu.addAction(saveAction)
        saveAction.triggered.connect(self.save)
        clearAction=QAction("Clear",self)
        clearAction.setShortcut("Command+C")
        fileMenu.addAction(clearAction)
        clearAction.triggered.connect(self.clear)
        pix_4=QAction("4px",self)
        b_size.addAction(pix_4)
        pix_4.triggered.connect(self.pix_4)
        pix_7=QAction("7px",self)
        b_size.addAction(pix_7)
        pix_7.triggered.connect(self.pix_7)
        pix_10=QAction("10px",self)
        b_size.addAction(pix_10)
        pix_10.triggered.connect(self.pix_10)
        pix_15=QAction("15px",self)
        b_size.addAction(pix_15)
        pix_15.triggered.connect(self.pix_15)
        black=QAction("Black",self)
        b_color.addAction(black)
        black.triggered.connect(self.blackColor)
        white=QAction("White",self)
        b_color.addAction(white)
        white.triggered.connect(self.whiteColor)
        red=QAction("Red",self)
        b_color.addAction(red)
        red.triggered.connect(self.redColor)
        green=QAction("Green",self)
        b_color.addAction(green)
        green.triggered.connect(self.greenColor)
        blue=QAction("Blue",self)
        b_color.addAction(blue)
        blue.triggered.connect(self.blueColor)
        yellow=QAction("Yellow",self)
        b_color.addAction(yellow)
        yellow.triggered.connect(self.yellowColor)
        magenta=QAction("Magenta",self)
        b_color.addAction(magenta)
        magenta.triggered.connect(self.magentaColor)
    def mousePressEvent(self,event):
        if event.button()==Qt.LeftButton:
            self.drawing=True
            self.lastPoint=event.pos()
    def mouseMoveEvent(self,event):
        if(event.buttons()&Qt.LeftButton) and self.drawing:
            painter=QPainter(self.image)
            painter.setPen(QPen(self.brushColor,self.brushSize,Qt.SolidLine,Qt.RoundCap,Qt.RoundJoin))
            painter.drawLine(self.lastPoint,event.pos())
            self.lastPoint=event.pos()
            self.update()
    def mouseReleaseEvent(self,event):
        if event.button()==Qt.LeftButton:
            self.drawing=False
    def paintEvent(self,event):
        canvasPainter=QPainter(self)
        canvasPainter.drawImage(self.rect(),self.image,self.image.rect())
    def save(self):
        fileName,_=QFileDialog.getSaveFileName(self,"Save","","PNG(*.png);;JPG(*.jpg *.jpeg);;BMP(*.bmp);;All Files(*.*)")
        if fileName:
            self.image.save(fileName)
    def clear(self):
        self.image.fill(Qt.white)
        self.update()
    def pix_4(self):
        self.brushSize=4
    def pix_7(self):
        self.brushSize=7
    def pix_10(self):
        self.brushSize=10
    def pix_15(self):
        self.brushSize=15
    def blackColor(self):
        self.brushColor=Qt.black
    def whiteColor(self):
        self.brushColor=Qt.white
    def redColor(self):
        self.brushColor=Qt.red
    def greenColor(self):
        self.brushColor=Qt.green
    def blueColor(self):
        self.brushColor=Qt.blue
    def yellowColor(self):
        self.brushColor=Qt.yellow
    def magentaColor(self):
        self.brushColor=Qt.magenta
app=QApplication(sys.argv)
window=Window()
window.show()
sys.exit(app.exec_())