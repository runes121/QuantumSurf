from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow, QApplication, QStatusBar, QToolBar, QLineEdit, QAction, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView
from stylesheets import *
import urllib.parse

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl.fromLocalFile(r"C:\Users\Admin\PycharmProjects\Browser\home.html"))
        self.browser.urlChanged.connect(self.update_urlbar)
        self.browser.loadFinished.connect(self.update_title)
        self.setCentralWidget(self.browser)

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        navtb = QToolBar("Navigation")
        navtb.setStyleSheet(navbar_stylesheet())
        self.addToolBar(navtb)

        back_btn = QAction("Back", self)
        back_btn.setStatusTip("Back to previous page")
        back_btn.triggered.connect(self.browser.back)
        navtb.addAction(back_btn)

        next_btn = QAction("Forward", self)
        next_btn.setStatusTip("Forward to next page")
        next_btn.triggered.connect(self.browser.forward)
        navtb.addAction(next_btn)

        reload_btn = QAction("Reload", self)
        reload_btn.setStatusTip("Reload page")
        reload_btn.triggered.connect(self.browser.reload)
        navtb.addAction(reload_btn)

        home_btn = QAction("Home", self)
        home_btn.setStatusTip("Go home")
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)

        chat_btn = QAction("Chat", self)
        chat_btn.setStatusTip("Chat with your preferred service.")
        chat_btn.triggered.connect(self.gotochat)
        navtb.addAction(chat_btn)

        quickto_gmail = QAction("gmail", self)
        quickto_gmail.setStatusTip("Go to gmail, quicker.")
        quickto_gmail.triggered.connect(self.opengmail)
        navtb.addAction(quickto_gmail)

        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        self.urlbar.setPlaceholderText("say anything...")
        navtb.addWidget(self.urlbar)

        AI_summarise = QAction("Summarise", self)
        AI_summarise.setStatusTip("Summarise the page, it's this easy.")
        AI_summarise.triggered.connect(self.summarise_page)
        navtb.addAction(AI_summarise)

    def summarise_page(self):
        msg = QMessageBox()
        msg.setWindowTitle("Coming soon.")
        msg.setText("This feature is coming soon.\n\nthe future is near...")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def opengmail(self):
        self.browser.setUrl(QUrl("https://gmail.com"))

    def update_urlbar(self, q):
        if q.toString() != "file:///C:/Users/Admin/PycharmProjects/Browser/home.html":
            self.urlbar.setText(q.toString())
            self.urlbar.setCursorPosition(0)
        else:
            self.urlbar.clear()

    def navigate_home(self):
        self.browser.setUrl(QUrl.fromLocalFile(r"C:\Users\Admin\PycharmProjects\Browser\home.html"))

    def gotochat(self):
        self.browser.setUrl(QUrl("https://bing.com/chat"))

    def navigate_to_url(self):
        url = self.urlbar.text()
        if not url.startswith("http://") and not url.startswith("https://") and not url.startswith("www."):
            url = "https://www.bing.com/search?q=" + urllib.parse.quote_plus(url)
        elif url.startswith("www."):
            url = "https://" + url
        self.browser.setUrl(QUrl(url))

    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle(f"QuantumSurf - {title}")


app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
