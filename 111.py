import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Circle(QtWidgets.QWidget):
    def __init__(self, size, color):
        super().__init__()
        self._loading_angle = 0
        self.width = 0
        self.color = color
        self.pixmap_opacity = 1
        self.resize(size, size)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setStyleSheet("background:transparent;")
        self.center()
        self.initUI()

        timeline = QtCore.QTimeLine(4000, self)
        timeline.setFrameRange(0, 360)
        timeline.frameChanged.connect(self.setLoadingAngle)
        timeline.start()

    def initUI(self):
        self.width = 15
        self.setLoadingAngle(0)
        self.show()

    def loadingAngle(self):
        return self._loading_angle

    def setLoadingAngle(self, angle):
        self._loading_angle = angle
        self.update()

    loadingAngle = QtCore.pyqtProperty(int, fget=loadingAngle, fset=setLoadingAngle)

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        drawingRect  = QtCore.QRect(QtCore.QPoint(), self.rect().size() - 2*self.width*QtCore.QSize(1, 1))
        drawingRect.moveCenter(self.rect().center())

        gradient = QtGui.QConicalGradient()
        gradient.setCenter(drawingRect.center())
        gradient.setAngle(90)
        gradient.setColorAt(1, QtGui.QColor(0,0,0))
        gradient.setColorAt(0, self.color)
        arcLengthApproximation = self.width + self.width / 3
        pen = QtGui.QPen(QtGui.QBrush(gradient), self.width)
        pen.setCapStyle(QtCore.Qt.RoundCap)
        painter.setPen(pen)
        painter.drawArc(drawingRect, 90 * 16 - arcLengthApproximation, -self._loading_angle * 16)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Circle(400, QtGui.QColor("blue"))
    w.show()
    sys.exit(app.exec_())
