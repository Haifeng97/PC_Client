import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import ui2
import time


class MyForm(QMainWindow, ui2.Ui_MainWindow):
    def __init__(self):
        super(MyForm, self).__init__()
        self.setupUi(self)
        self.lineEdit.setText('192.168.1.147')
        self.lineEdit_2.setText('1586')
        self.log('Start')
        self.pushButton_RST.clicked.connect(self.reset)
        self.pushButton_CL.clicked.connect(self.clear_log)

        self.horizontalSlider.valueChanged.connect(self.openGLWidget.setXRotation)
        self.openGLWidget.xRotationChanged.connect(self.horizontalSlider.setValue)
        self.horizontalSlider_2.valueChanged.connect(self.openGLWidget.setYRotation)
        self.openGLWidget.yRotationChanged.connect(self.horizontalSlider_2.setValue)
        self.horizontalSlider_3.valueChanged.connect(self.openGLWidget.setZRotation)
        self.openGLWidget.zRotationChanged.connect(self.horizontalSlider_3.setValue)

        self.horizontalSlider.valueChanged.connect(self.update_slider_value)
        self.horizontalSlider_2.valueChanged.connect(self.update_slider_value)
        self.horizontalSlider_3.valueChanged.connect(self.update_slider_value)
        self.horizontalSlider.name = 's1'
        self.horizontalSlider_2.name = 's2'
        self.horizontalSlider_3.name = 's3'
        self.horizontalSlider.setValue(348)
        self.horizontalSlider_2.setValue(5422)
        self.horizontalSlider_3.setValue((0 * 16))
        self.label_x.setText(str(348))
        self.label_y.setText(str(5422))
        self.label_z.setText(str(0 * 16))

    def clear_log(self):
        self.textEdit.setText('')

    def update_slider_value(self, v):
        sender = self.sender()
        if sender.name == 's1':
            self.label_x.setText(str(v))
            self.log('lx set')
        elif sender.name == 's2':
            self.label_y.setText(str(v))
            self.log('ly set')
        elif sender.name == 's3':
            self.label_z.setText(str(v))
            self.log('lz set')

    def reset(self):
        self.log('Reset')
        # todo
        self.openGLWidget.setXRotation(0)
        self.openGLWidget.setYRotation(0)
        self.openGLWidget.setZRotation(0)

    def log(self, s):
        self.localtime = time.asctime(time.localtime(time.time()))
        self.textEdit.append(self.localtime[11:19] + ' ' + s)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
