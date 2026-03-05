from PySide6.QtWidgets import QApplication
from menu import MenuWindow
from ui import MainWindow

app = QApplication([])

def start_call():

    menu.close()

    global call_window
    call_window = MainWindow()
    call_window.show()


menu = MenuWindow(start_call)
menu.show()

app.exec()