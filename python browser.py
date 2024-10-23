# Using the command line, install the correct PyQt version:
# pip install PyQt5 or pip install PyQt6
# pip install PyQtWebEngine

# Import necessary PyQt modules for creating the GUI components and web engine
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView

# Define the main class for the web browser


class MyWebBrowser:
    def __init__(self):
        # Create the main window of the browser
        self.window = QWidget()
        self.window.setWindowTitle(
            "Next level dronex... made by kaptain Divine")  # Set the window title

        # Ensure the window and elements use the system's default theme
        self.window.setStyle(QStyleFactory.create(
            'Fusion'))  # System default styling

        # Create a vertical layout for the main window
        self.layout = QVBoxLayout()  # Main layout to hold all elements vertically
        # Horizontal layout for the top bar (URL and buttons)
        self.horizontal = QHBoxLayout()

        # Create a URL bar for entering web addresses
        # Multiline text box for entering URLs (should be changed to QLineEdit ideally)
        self.url_bar = QTextEdit()
        # Limit height of the URL bar to 30px
        self.url_bar.setMaximumHeight(30)

        # Create the "Search" button
        self.go_btn = QPushButton("Search")  # Button to navigate to the URL
        self.go_btn.setMinimumHeight(30)  # Set minimum height for consistency

        # Create the "Back" button
        # Button to navigate back in the browser history
        self.back_btn = QPushButton("Previous page")
        self.back_btn.setMinimumHeight(30)

        # Create the "Forward" button
        # Button to navigate forward in the browser history
        self.forward_btn = QPushButton("Next page")
        self.forward_btn.setMinimumHeight(30)

        # Add the URL bar and buttons to the horizontal layout
        # Add URL bar to horizontal layout
        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)  # Add "Search" button
        self.horizontal.addWidget(self.back_btn)  # Add "Back" button
        self.horizontal.addWidget(self.forward_btn)  # Add "Forward" button

        # Create the web engine view (the actual browser window for displaying pages)
        self.browser = QWebEngineView()  # QWebEngineView is the widget to display web pages

        # Connect the buttons to their respective functions
        # Call navigate method when "Search" button is clicked
        self.go_btn.clicked.connect(
            lambda: self.navigate(self.url_bar.toPlainText()))
        # Go back in browser history
        self.back_btn.clicked.connect(self.browser.back)
        # Go forward in browser history
        self.forward_btn.clicked.connect(self.browser.forward)

        # Add the horizontal layout (with URL bar and buttons) and the browser widget to the main layout
        # Add the horizontal layout to the main layout
        self.layout.addLayout(self.horizontal)
        # Add the browser view to the layout
        self.layout.addWidget(self.browser)

        # Set the default URL to load when the browser starts
        # Load Google as the initial page
        self.browser.setUrl(QUrl("http://google.com"))

        # Set the layout of the main window and display it
        self.window.setLayout(self.layout)  # Apply the layout to the window
        self.window.show()  # Show the window

    # Function to handle navigation when the "Search" button is clicked
    def navigate(self, url):
        # If the entered URL doesn't start with "http://", add it
        if not url.startswith("http://"):
            url = "http://" + url  # Prefix "http://" if missing
            # Update the URL bar with the corrected URL
            self.url_bar.setText(url)
        # Navigate the browser to the entered URL
        self.browser.setUrl(QUrl(url))


# Main application loop
app = QApplication([])  # Initialize the Qt application
window = MyWebBrowser()  # Create an instance of the browser
app.exec_()  # Start the event loop for the application
