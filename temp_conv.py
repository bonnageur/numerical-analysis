#!/usr/bin/env python3

# this python code embeds C code. it compiles it and get result.
# then display it in a new poped up window. the gui library is PyQt5.
# without gui, python code is much simpler and less complex.

import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QPushButton, QWidget, QLabel, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Temperature Conversion")
        self.setGeometry(100, 100, 600, 400)

        self.table = QTableWidget(17, 2, self)
        self.table.setHorizontalHeaderLabels(["Fahrensheit", "Celsius"])

        self.run_button = QPushButton("Run Temperature Conversion", self)
        self.run_button.clicked.connect(self.run_conversion)

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.run_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def run_conversion(self):
        try:
            # compile the C code
            compile_command = ["gcc", "003_temp.c", "-o", "003_temp"]
            subprocess.run(compile_command, check=True)

            # run the compiled C program and capture its output
            run_command = ["./003_temp"]
            completed_process = subprocess.run(run_command, text=True, capture_output=True)

            # split the output into lines and populate the table
            lines = completed_process.stdout.strip().split('\n')
            for row, line in enumerate(lines):
                fahrenheit, celsius = line.split()

                # create QTableWidgetItem with right alignment
                item_fahrenheit = QTableWidgetItem(fahrenheit)
                item_fahrenheit.setTextAlignment(Qt.AlignRight)      # align right (Qt::AlignRight)

                item_celsius = QTableWidgetItem(celsius)
                item_celsius.setTextAlignment(Qt.AlignRight)         # align right (QT::AlignRight)

                self.table.setItem(row, 0, item_fahrenheit)
                self.table.setItem(row, 1, item_celsius)

        except subprocess.CalledProcessError as e:
            self.table.clearContents()
            self.table.setRowCount(0)
            self.output_text.setPalinText("Error occured:\n" + e.stderr)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
