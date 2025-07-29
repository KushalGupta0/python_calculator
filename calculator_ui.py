"""
Calculator UI Module
Handles all user interface components and layouts
"""

from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, 
                               QHBoxLayout, QGridLayout, QPushButton, 
                               QLineEdit, QTextEdit, QLabel, QSplitter)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeySequence, QShortcut, QFont
from styles import LIGHT_THEME_STYLESHEET
from calculator_logic import CalculatorLogic
from history_manager import HistoryManager

class CalculatorUI(QMainWindow):
    """Main calculator window class"""
    
    def __init__(self):
        super().__init__()
        self.logic = CalculatorLogic()
        self.history = HistoryManager()
        self.current_input = ""
        self.setup_ui()
        self.apply_theme()
        self.setup_keyboard_shortcuts()
        self.load_history_display()
    
    def setup_ui(self):
        """Initialize the user interface"""
        # Main window properties
        self.setWindowTitle("Python Calculator")
        self.setFixedSize(400, 600)
        self.setWindowFlags(Qt.Window | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # Create splitter for resizable sections
        splitter = QSplitter(Qt.Vertical)
        main_layout.addWidget(splitter)
        
        # Calculator section
        calc_widget = QWidget()
        calc_layout = QVBoxLayout(calc_widget)
        
        # Display screen
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setText("0")
        self.display.setAlignment(Qt.AlignRight)
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.display.setFont(font)
        self.display.setMinimumHeight(50)
        calc_layout.addWidget(self.display)
        
        # Button grid
        self.create_button_grid(calc_layout)
        
        # History section
        history_widget = QWidget()
        history_layout = QVBoxLayout(history_widget)
        
        history_label = QLabel("History:")
        history_layout.addWidget(history_label)
        
        self.history_display = QTextEdit()
        self.history_display.setReadOnly(True)
        self.history_display.setMaximumHeight(150)
        history_layout.addWidget(self.history_display)
        
        # Clear history button
        clear_history_btn = QPushButton("Clear History")
        clear_history_btn.clicked.connect(self.clear_history)
        history_layout.addWidget(clear_history_btn)
        
        # Add widgets to splitter
        splitter.addWidget(calc_widget)
        splitter.addWidget(history_widget)
        splitter.setStretchFactor(0, 3)
        splitter.setStretchFactor(1, 1)
    
    def create_button_grid(self, parent_layout):
        """Create the calculator button grid"""
        grid_layout = QGridLayout()
        
        # Button definitions (text, row, col, style_class)
        buttons = [
            ('C', 0, 0, 'clear'), ('CE', 0, 1, 'clear'), ('⌫', 0, 2, 'clear'), ('÷', 0, 3, 'operator'),
            ('7', 1, 0, 'number'), ('8', 1, 1, 'number'), ('9', 1, 2, 'number'), ('×', 1, 3, 'operator'),
            ('4', 2, 0, 'number'), ('5', 2, 1, 'number'), ('6', 2, 2, 'number'), ('-', 2, 3, 'operator'),
            ('1', 3, 0, 'number'), ('2', 3, 1, 'number'), ('3', 3, 2, 'number'), ('+', 3, 3, 'operator'),
            ('±', 4, 0, 'function'), ('0', 4, 1, 'number'), ('.', 4, 2, 'number'), ('=', 4, 3, 'equals')
        ]
        
        self.buttons = {}
        for text, row, col, style_class in buttons:
            btn = QPushButton(text)
            btn.setMinimumSize(60, 50)
            btn.setProperty("class", style_class)
            btn.clicked.connect(lambda checked, t=text: self.button_clicked(t))
            grid_layout.addWidget(btn, row, col)
            self.buttons[text] = btn
        
        parent_layout.addLayout(grid_layout)
    
    def button_clicked(self, text):
        """Handle button click events"""
        if text.isdigit() or text == '.':
            self.handle_number_input(text)
        elif text in ['+', '-', '×', '÷']:
            self.handle_operator_input(text)
        elif text == '=':
            self.handle_equals()
        elif text == 'C':
            self.handle_clear()
        elif text == 'CE':
            self.handle_clear_entry()
        elif text == '⌫':
            self.handle_backspace()
        elif text == '±':
            self.handle_sign_change()
    
    def handle_number_input(self, digit):
        """Handle number and decimal input"""
        current = self.display.text()
        
        # If we're building an expression and the display ends with an operator
        if self.current_input and current.strip() and current.strip()[-1] in ['×', '÷', '+', '-']:
            # Start new number after operator
            if digit == '.':
                self.display.setText(current + ' 0.')
            else:
                self.display.setText(current + ' ' + digit)
        # If we're continuing to build the current number
        elif self.current_input and not current.endswith(('×', '÷', '+', '-')):
            # Get the last part (current number being typed)
            parts = current.split()
            if parts:
                last_part = parts[-1]
                if digit == '.' and '.' in last_part:
                    return  # Prevent multiple decimals in same number
            self.display.setText(current + digit)
        else:
            # Normal number input behavior (starting fresh)
            if current == "0" or current == "Error":
                self.display.setText(digit)
            else:
                if digit == '.' and '.' in current:
                    return  # Prevent multiple decimals
                self.display.setText(current + digit)
    
    def handle_operator_input(self, operator):
        """Handle operator input"""
        current = self.display.text().strip()
        if current == "Error" or not current:
            return
        
        # Convert display operator to internal operator
        op_map = {'×': '*', '÷': '/'}
        internal_op = op_map.get(operator, operator)
        
        # If there's already a current input, we're chaining operations
        if self.current_input:
            # If the display already shows an expression, use it as is
            if any(op in current for op in ['×', '÷', '+', '-']):
                # Update the expression with new operator
                self.current_input = current.replace('×', '*').replace('÷', '/') + ' ' + internal_op + ' '
            else:
                # Add the current number and new operator
                self.current_input += current + ' ' + internal_op + ' '
        else:
            # Start new expression
            self.current_input = current + ' ' + internal_op + ' '
        
        # Show the building expression in display (with display operators)
        display_expr = self.current_input.replace('*', '×').replace('/', '÷')
        self.display.setText(display_expr)
    
    def handle_equals(self):
        """Handle equals button press - THIS IS WHERE WE CLEAR"""
        current = self.display.text().strip()
        if current == "Error" or not current:
            return
        
        # Determine the complete expression
        if self.current_input:
            # If we have a pending operation
            if any(op in current for op in ['×', '÷', '+', '-']):
                # The display already contains the full expression
                expression = current.replace('×', '*').replace('÷', '/')
            else:
                # Current display is just the last number
                expression = self.current_input + current
        else:
            # No pending operation, just evaluate what's shown
            expression = current.replace('×', '*').replace('÷', '/')
        
        if not expression.strip():
            return
        
        try:
            result = self.logic.calculate(expression)
            
            # Add to history before clearing
            display_expr = expression.replace('*', '×').replace('/', '÷')
            self.history.add_calculation(display_expr, str(result))
            self.update_history_display()
            
            # NOW we clear and show only result
            self.display.setText(str(result))
            self.current_input = ""
            
        except Exception as e:
            self.display.setText("Error")
            self.current_input = ""
    
    def handle_clear(self):
        """Clear everything"""
        self.display.setText("0")
        self.current_input = ""
        self.logic.clear()
    
    def handle_clear_entry(self):
        """Clear current entry only"""
        current = self.display.text().strip()
        
        if self.current_input:
            # If we're in the middle of building an expression
            # Just reset to show the pending operation
            display_expr = self.current_input.replace('*', '×').replace('/', '÷')
            self.display.setText(display_expr.rstrip())
        else:
            # Just clear the display
            self.display.setText("0")
    
    def handle_backspace(self):
        """Remove last character"""
        current = self.display.text()
        if current == "Error" or current == "0":
            return
        
        if len(current) <= 1:
            self.display.setText("0")
            self.current_input = ""
        else:
            new_text = current[:-1].rstrip()
            if not new_text:
                self.display.setText("0")
                self.current_input = ""
            else:
                self.display.setText(new_text)
                # Update current_input if we're modifying it
                if self.current_input:
                    self.current_input = new_text.replace('×', '*').replace('÷', '/') + ' '
    
    def handle_sign_change(self):
        """Change sign of current number"""
        current = self.display.text().strip()
        if current == "Error" or not current:
            return
        
        # If we're in the middle of an expression
        if self.current_input and any(op in current for op in ['×', '÷', '+', '-']):
            # Find the last number and change its sign
            parts = current.split()
            if parts and parts[-1].replace('-', '').replace('.', '').isdigit():
                last_num = parts[-1]
                if last_num.startswith('-'):
                    parts[-1] = last_num[1:]
                else:
                    parts[-1] = '-' + last_num
                self.display.setText(' '.join(parts))
        else:
            # Simple case - just the number on display
            if current.startswith('-'):
                self.display.setText(current[1:])
            else:
                self.display.setText('-' + current)
    
    def setup_keyboard_shortcuts(self):
        """Setup keyboard mappings"""
        # Number shortcuts
        for i in range(10):
            shortcut = QShortcut(QKeySequence(str(i)), self)
            shortcut.activated.connect(lambda i=i: self.handle_number_input(str(i)))
        
        # Operator shortcuts
        QShortcut(QKeySequence('+'), self).activated.connect(lambda: self.handle_operator_input('+'))
        QShortcut(QKeySequence('-'), self).activated.connect(lambda: self.handle_operator_input('-'))
        QShortcut(QKeySequence('*'), self).activated.connect(lambda: self.handle_operator_input('×'))
        QShortcut(QKeySequence('/'), self).activated.connect(lambda: self.handle_operator_input('÷'))
        
        # Other shortcuts
        QShortcut(QKeySequence('.'), self).activated.connect(lambda: self.handle_number_input('.'))
        QShortcut(QKeySequence(Qt.Key_Return), self).activated.connect(self.handle_equals)
        QShortcut(QKeySequence(Qt.Key_Enter), self).activated.connect(self.handle_equals)
        QShortcut(QKeySequence(Qt.Key_Escape), self).activated.connect(self.handle_clear)
        QShortcut(QKeySequence(Qt.Key_Backspace), self).activated.connect(self.handle_backspace)
    
    def apply_theme(self):
        """Apply light theme to all elements"""
        self.setStyleSheet(LIGHT_THEME_STYLESHEET)
    
    def load_history_display(self):
        """Load and display calculation history"""
        history = self.history.get_history()
        self.update_history_display()
    
    def update_history_display(self):
        """Update the history display"""
        history = self.history.get_history()
        history_text = ""
        for calc in history[-10:]:  # Show last 10 calculations
            history_text += f"{calc['expression']} = {calc['result']}\n"
        self.history_display.setText(history_text)
    
    def clear_history(self):
        """Clear calculation history"""
        self.history.clear_history()
        self.history_display.clear()
