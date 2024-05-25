def navbar_stylesheet():
    return """
QToolBar {
    background-color: #333333;
    padding: 2px;
    border: none;
}

QToolButton {
    color: white;
    font-weight: bold;
    padding: 5px;
    margin: 0 2px;
    background-color: #555555;
    border: 1px solid #666666;
    border-radius: 4px;
}

QToolButton:hover {
    background-color: #777777;
}

QToolButton:pressed {
    background-color: #888888;
}
"""