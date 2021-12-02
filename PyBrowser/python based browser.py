import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.browser=QWebEngineView()
        self.browser.setUrl(QUrl("http://www.bing.com"))
        self.setCentralWidget(self.browser)
        self.showMaximised()

        navbar=QToolBar()
        self.addToolBar(navbar)
        back_button=QAction('back',self)
        back_button.triggered.connect(self.browser.back)
        back_button.addAction(back_button)

        forward_button=QAction('forward',self)
        forward_button.triggered.connect(self.browser.foreward)
        forward_button.addAction(forward_button)

        reload_button=QAction('reload',self)
        reload_button.triggered.connect(self.browser.reload)
        reload_button.addAction(reload_button)

        home_button=QAction('home',self)  
        home_button.triggered.connect(self.browser.home)
        home_button.addAction(home_button)

        self.url_bar=QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)

    def navigate_to_home(self):
        self.browser.setUrl(QUrl("http://www.google.com"))

    def navigate_to_url(self):
        url=self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self,q):      
        self.url_bar.setText(q.toString())

app=QApplication(sys.argv)
QApplication.setApplicationName('Home Made Browser By (Aayush Kumar)')
window=MainWindow()
app.exec_()