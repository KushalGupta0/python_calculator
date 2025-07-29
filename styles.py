"""
Styles Module
Contains all UI styling and theme definitions
"""

LIGHT_THEME_STYLESHEET = """
/* Base Widget Styling */
QWidget {
    background-color: #f0f0f0;
    color: #000000;
    font-family: "Segoe UI", Arial, sans-serif;
    font-size: 12px;
}

/* Button Styling */
QPushButton {
    background-color: #ffffff;
    border: 1px solid #cccccc;
    color: #000000;
    padding: 8px;
    border-radius: 4px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #e6e6e6;
    border: 1px solid #999999;
}

QPushButton:pressed {
    background-color: #d9d9d9;
    border: 1px solid #666666;
}

/* Operator buttons */
QPushButton[class="operator"] {
    background-color: #e6f3ff;
    color: #0066cc;
}

QPushButton[class="operator"]:hover {
    background-color: #cce6ff;
}

/* Equals button */
QPushButton[class="equals"] {
    background-color: #0066cc;
    color: #ffffff;
}

QPushButton[class="equals"]:hover {
    background-color: #0052a3;
}

/* Clear buttons */
QPushButton[class="clear"] {
    background-color: #ffe6e6;
    color: #cc0000;
}

QPushButton[class="clear"]:hover {
    background-color: #ffcccc;
}

/* Display Screen (QLineEdit) */
QLineEdit {
    background-color: #ffffff;
    border: 2px solid #cccccc;
    color: #000000;
    padding: 10px;
    font-size: 18px;
    font-weight: bold;
    text-align: right;
    border-radius: 4px;
}

QLineEdit:focus {
    border: 2px solid #0078d4;
}

/* History Panel (QTextEdit) */
QTextEdit {
    background-color: #ffffff;
    border: 1px solid #cccccc;
    color: #000000;
    padding: 5px;
    font-size: 11px;
    border-radius: 4px;
}

/* Labels */
QLabel {
    background-color: transparent;
    color: #000000;
    font-size: 12px;
}

/* Main Window */
QMainWindow {
    background-color: #f0f0f0;
    color: #000000;
}

/* Dialog Boxes */
QDialog {
    background-color: #f0f0f0;
    color: #000000;
}

/* Splitter */
QSplitter::handle {
    background-color: #cccccc;
}

QSplitter::handle:horizontal {
    width: 3px;
}

QSplitter::handle:vertical {
    height: 3px;
}

/* Scroll Bars */
QScrollBar:vertical {
    background-color: #f0f0f0;
    width: 16px;
    border: 1px solid #cccccc;
}

QScrollBar::handle:vertical {
    background-color: #cccccc;
    border-radius: 8px;
    min-height: 20px;
}

QScrollBar::handle:vertical:hover {
    background-color: #999999;
}

/* Tool Tips */
QToolTip {
    background-color: #ffffff;
    color: #000000;
    border: 1px solid #cccccc;
    padding: 4px;
    border-radius: 4px;
}
"""
