from windowClasses import *
from PySide2.QtCore import QCoreApplication
from PySide2.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication([])
    QCoreApplication.setOrganizationName("kingavatar")
    # QCoreApplication.setOrganizationDomain("")
    QCoreApplication.setApplicationName("App Name")
    window = SplashScreen()
    sys.exit(app.exec_())
