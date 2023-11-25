import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication
from Conversions import TempConverter


class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('mainwindow.ui', self)
        self.build_ui()
        self.show()

    def build_ui(self):
        conversions = ['Fahrenheit to Celsius', 'Celsius to Fahrenheit']
        self.ui.cmb_conv_type.addItems(conversions)
        self.ui.btn_convert.clicked.connect(self.handle_click)

    def handle_click(self):
        temp = float(self.ui.txt_input.text())
        if self.ui.cmb_conv_type.currentIndex() == 0:
            result = str(round(TempConverter.f_to_c(temp), 1)) + '°C'
        else:
            result = str(round(TempConverter.c_to_f(temp), 1)) + '°F'
        self.ui.lbl_result.setText(result)


app = QApplication(sys.argv)
w = AppWindow()
sys.exit(app.exec())
