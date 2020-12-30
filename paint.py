from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu, QMenuBar, QAction, QFileDialog
from PyQt5.QtGui import QIcon, QImage, QPainter, QPen, QBrush
from PyQt5.QtCore import Qt, QPoint
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        top = 400
        left = 400
        width = 800
        height = 600

        self.setGeometry(top, left, width, height)
        self.setWindowTitle("Paint Application")

        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

        self.mode = "Scribble"
        self.drawing = False
        self.brush = False
        self.penColor = Qt.black
        self.penSize = 3
        self.brushColor = Qt.black

        self.lastPoint = QPoint()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        brushSize = mainMenu.addMenu("Brush Size")
        brushColor = mainMenu.addMenu("Brush Color")
        canvasColor = mainMenu.addMenu("Canvas Fill")
        shapesMenu = mainMenu.addMenu("Shapes")

        loadAction = QAction("Open File", self)
        loadAction.setShortcut("Ctrl+O")
        fileMenu.addAction(loadAction)
        loadAction.triggered.connect(self.loadIntoCanvas)

        saveAction = QAction("Save File", self)
        saveAction.setShortcut("Ctrl+S")
        fileMenu.addAction(saveAction)
        saveAction.triggered.connect(self.saveCanvas)

        clearAction = QAction("Clear File", self)
        clearAction.setShortcut("Ctrl+C")
        fileMenu.addAction(clearAction)
        clearAction.triggered.connect(self.clearCanvas)

        action3_px = QAction("3 px", self)
        brushSize.addAction(action3_px)
        action3_px.triggered.connect(self.brush3)

        action5_px = QAction("5 px", self)
        brushSize.addAction(action5_px)
        action5_px.triggered.connect(self.brush5)

        action7_px = QAction("7 px", self)
        brushSize.addAction(action7_px)
        action7_px.triggered.connect(self.brush7)

        action9_px = QAction("9 px", self)
        brushSize.addAction(action9_px)
        action9_px.triggered.connect(self.brush9)

        blackAction = QAction("Black", self)
        blackAction.setShortcut("Ctrl+B")
        brushColor.addAction(blackAction)
        blackAction.triggered.connect(self.blackColor)

        whiteAction = QAction("White", self)
        whiteAction.setShortcut("Ctrl+W")
        brushColor.addAction(whiteAction)
        whiteAction.triggered.connect(self.whiteColor)

        redAction = QAction("Red", self)
        redAction.setShortcut("Ctrl+R")
        brushColor.addAction(redAction)
        redAction.triggered.connect(self.redColor)

        yellowAction = QAction("Yellow", self)
        yellowAction.setShortcut("Ctrl+Y")
        brushColor.addAction(yellowAction)
        yellowAction.triggered.connect(self.yellowColor)

        greenAction = QAction("Red", self)
        greenAction.setShortcut("Ctrl+G")
        brushColor.addAction(greenAction)
        greenAction.triggered.connect(self.greenColor)

        actionBlack = QAction("Black Fill", self)
        actionBlack.setShortcut("Ctrl+Shift+B")
        canvasColor.addAction(actionBlack)
        actionBlack.triggered.connect(self.imageColorBlack)

        actionWhite = QAction("White Fill", self)
        actionWhite.setShortcut("Ctrl+Shift+W")
        canvasColor.addAction(actionWhite)
        actionWhite.triggered.connect(self.imageColorWhite)

        actionRed = QAction("Red Fill", self)
        actionRed.setShortcut("Ctrl+Shift+R")
        canvasColor.addAction(actionRed)
        actionRed.triggered.connect(self.imageColorRed)

        actionYellow = QAction("Yellow Fill", self)
        actionYellow.setShortcut("Ctrl+Shift+Y")
        canvasColor.addAction(actionYellow)
        actionYellow.triggered.connect(self.imageColorYellow)

        actionGreen = QAction("Green Fill", self)
        actionGreen.setShortcut("Ctrl+Shift+G")
        canvasColor.addAction(actionGreen)
        actionGreen.triggered.connect(self.imageColorGreen)

        rectAction = QAction("Rectangle", self)
        shapesMenu.addAction(rectAction)
        rectAction.triggered.connect(self.rectangleDraw)

        scribbleAction = QAction("Scribble", self)
        shapesMenu.addAction(scribbleAction)
        scribbleAction.triggered.connect(self.scribbleDraw)

        ellipseAction = QAction("Ellipse", self)
        shapesMenu.addAction(ellipseAction)
        ellipseAction.triggered.connect(self.ellipseDraw)

        shapeFill = shapesMenu.addMenu("Shape Fill")
        noFillAction = QAction("No Fill", self)
        shapeFill.addAction(noFillAction)
        noFillAction.triggered.connect(self.brushDown)

        fillAction = QAction("Color Fill", self)
        shapeFill.addAction(fillAction)
        fillAction.triggered.connect(self.brushUp)

    def brushUp(self):
        self.brush = True
        
    def brushDown(self):
        self.brush = False

    def rectangleDraw(self):
        self.mode = "Rectangle"

    def ellipseDraw(self):
        self.mode = "Ellipse"

    def scribbleDraw(self):
        self.mode = "Scribble"

    def mousePressEvent(self, event):
        if(event.button() == Qt.LeftButton):
            self.drawing = True
            self.lastPoint = event.pos()
            if(not (self.mode == "Scribble")):
                self.x1y1 = event.pos()

    def mouseMoveEvent(self, event):
        if(Qt.LeftButton and event.buttons()) and self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.penColor, self.penSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            if(self.brush):
                painter.setBrush(QBrush(self.brushColor, Qt.SolidPattern))
            if self.mode == "Scribble":
                painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        painter = QPainter(self.image)
        painter.setPen(QPen(self.penColor, self.penSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        if(self.brush):
            painter.setBrush(QBrush(self.brushColor, Qt.SolidPattern))
        if(event.button() == Qt.LeftButton):
            if(self.mode == "Rectangle"):
                self.x2y2 = event.pos() - self.x1y1
                painter.drawRect(self.x1y1.x(), self.x1y1.y(), self.x2y2.x(), self.x2y2.y())
            if(self.mode == "Ellipse"):
                self.x2y2 = event.pos() - self.x1y1
                painter.drawEllipse(self.x1y1.x(), self.x1y1.y(), self.x2y2.x(), self.x2y2.y())
            self.update()
            self.drawing = False

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(self.rect(), self.image, self.image.rect())
    
    def imageColorGreen(self):
        self.image.fill(Qt.green)
        self.update()

    def imageColorYellow(self):
        self.image.fill(Qt.yellow)
        self.update()
    
    def imageColorRed(self):
        self.image.fill(Qt.red)
        self.update()

    def imageColorWhite(self):
        self.image.fill(Qt.white)
        self.update()

    def imageColorBlack(self):
        self.image.fill(Qt.black)
        self.update()

    def greenColor(self):
        self.penColor = Qt.green

    def yellowColor(self):
        self.penColor = Qt.yellow
    
    def redColor(self):
        self.penColor = Qt.red

    def blackColor(self):
        self.penColor = Qt.black

    def whiteColor(self):
        self.penColor = Qt.white

    def brush3(self):
        self.penSize = 3

    def brush5(self):
        self.penSize = 5

    def brush7(self):
        self.penSize = 7

    def brush9(self):
        self.penSize = 9

    def clearCanvas(self):
        self.image.fill(Qt.white)
        self.update()

    def saveCanvas(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save File", "", "PNG (*.png);;JPEG (*.jpg or *.jpeg);;All files (*.*)")
        if filePath == "":
            return
        self.image.save(filePath)

    def loadIntoCanvas(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Load File", "", "PNG (*.png);;JPEG (*.jpg or *.jpeg);;All files (*.*)")
        if filePath == "":
            return
        self.resize(self.size())
        self.image.load(filePath)
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()