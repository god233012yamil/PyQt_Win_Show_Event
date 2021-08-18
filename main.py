import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QEvent


class AppWindow(QMainWindow):

    def __init__(self):
        super(AppWindow, self).__init__()

        # Installs an event filter on AppWindow.
        # An event filter is an object that receives
        # all events that are sent to this object.
        self.installEventFilter(self)
        # Set window title.
        self.setWindowTitle("Widget show event example")
        # Set window size.
        self.setFixedSize(600, 200)

    # This event filter is used to capture the event that
    # occurred when the main window is shown.
    def eventFilter(self, obj, event):
        # If the AppWindow widget is shown on screen.
        if event.type() == QEvent.Show:
            print("The AppWindow shown event was captured")
            # Return true to inform that this event was consumed.
            return True
        # Return the object and event.
        return super(AppWindow, self).eventFilter(obj, event)


def main():
    # Start the Qt event loop.
    app = QApplication(sys.argv)
    # Create an instance of AppWindow.
    window = AppWindow()
    # Show the window.
    window.show()
    # Exit.
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

