import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("images.jpg"))

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 30))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: #292929;"
                            "background-color: #6fdcf7;"
                            "font_weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")
        
        #label.setAlignment(Qt.AlignTop) #vertically top
        #label.setAlignment(Qt.AlignBottom) #vertically bottom
        #label.setAlignment(Qt.AlignVCenter) #vertically center

        #label.setAlignment(Qt.AlignRight) #horizontally right
        #label.setAlignment(Qt.AlignHCenter) #horizontally center
        #label.setAlignment(Qt.AlignLeft) #horizontally left

        #label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # center & top
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # center & bottom
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # center & center
        label.setAlignment(Qt.AlignCenter) # center and center

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()