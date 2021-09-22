from PySide2.QtWidgets import QApplication
from controllers.main_window_controller import MainWindowController

if __name__ == "__main__":
    app = QApplication()
    window = MainWindowController()
    window.show()

    app.exec_()