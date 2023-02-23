from PyQt5.QtWidgets import (QApplication, 
                             QPushButton, 
                             QLabel, 
                             QMainWindow, 
                             QTextEdit,
                             QComboBox)
from PyQt5.QtGui import QFont
import sys
class mainForm(QMainWindow):
 
    def __init__(self):
        super(mainForm, self).__init__()
        self.initUI()
        self.show()

    def initUI(self):
        
        font = QFont()
        font.setPixelSize(20)
        font.setFamily("Times New Roman")
        font.setPointSize(14)

        self.setWindowTitle("Convolution Dimension Calculator")
        self.setGeometry(0, 0, 600, 300)

        self.combo = QComboBox(self)
        self.combo.addItem("Convolution")
        self.combo.addItem("Transposed Convolution")
        self.combo.move(50, 130)

        self.label_input_size = QLabel("Feature Size", self)
        self.label_input_size.move(60, 80)
        self.label_input_size.setFont(font)
        self.label_input_size.setFixedHeight(35)
 
        self.label_kernel_size = QLabel("Kernel Size", self)
        self.label_kernel_size.move(160, 80)
        self.label_kernel_size.setFont(font)
        self.label_kernel_size.setFixedHeight(35)
 
        self.label_stride_size = QLabel("Stride", self)
        self.label_stride_size.move(260, 80)
        self.label_stride_size.setFont(font)
        self.label_stride_size.setFixedHeight(35)
 
        self.label_padding_size = QLabel("Padding", self)
        self.label_padding_size.move(360, 80)
        self.label_padding_size.setFont(font)
        self.label_padding_size.setFixedHeight(35)

        self.label_output_padding_size = QLabel("Output Padding", self)
        self.label_output_padding_size.move(460, 80)
        self.label_output_padding_size.setFont(font)
        self.label_output_padding_size.setFixedHeight(35)

        self.label_output_size = QLabel("Output Size:", self)
        self.label_output_size.move(260, 200)
        self.label_output_size.setFont(font)
        self.label_output_size.setFixedHeight(35)
 
        self.text_input = QTextEdit(self)
        self.text_input.move(50, 50)
        self.text_input.setFixedHeight(30)
        self.text_input.setFont(font)
 
        self.text_kernel = QTextEdit(self)
        self.text_kernel.move(150, 50)
        self.text_kernel.setFont(font)
        self.text_kernel.setFixedHeight(30)
 
        self.text_stride = QTextEdit(self)
        self.text_stride.move(250, 50)
        self.text_stride.setFont(font)
        self.text_stride.setFixedHeight(30)
 
        self.text_padding = QTextEdit(self)
        self.text_padding.move(350, 50)
        self.text_padding.setFixedHeight(30)
        self.text_padding.setFont(font)

        self.text_output_padding = QTextEdit(self)
        self.text_output_padding.move(450,50)
        self.text_output_padding.setFixedHeight(30)
        self.text_output_padding.setFont(font)
 
        self.button_cal=QPushButton("Calculate",self)
        self.button_cal.move(250,130)
        self.button_cal.setFont(font)
        self.button_cal.setFixedHeight(35)
 
        self.button_cal.clicked.connect(self.cal)
    
    def default_params(self, text: str, default_value: int):
        if text == '':
            return default_value
        else:
            return int(text)
    
    def cal(self):
        i = self.default_params(self.text_input.toPlainText(), 32)
        k = self.default_params(self.text_kernel.toPlainText(), 3)
        s = self.default_params(self.text_stride.toPlainText(), 1)
        p = self.default_params(self.text_padding.toPlainText(), 0)
        op = self.default_params(self.text_output_padding.toPlainText(), 0)
        if self.combo.currentText()=="Convolution":
            out = (i-k+2*p) / s + 1
        else:
            out = (i-1) * s + k - 2*p + op
        self.label_output_size.setText("Output Size: "+str(int(out)))
        self.label_output_size.adjustSize()
 
app=QApplication(sys.argv)
f=mainForm()
sys.exit(app.exec())
