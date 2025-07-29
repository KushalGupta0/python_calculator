#!/usr/bin/env python3
"""
Python Calculator with PySide6
Entry point for the calculator application
"""

import sys
from PySide6.QtWidgets import QApplication
from calculator_ui import CalculatorUI

def main():
    """Main application entry point"""
    app = QApplication(sys.argv)
    
    # Set application properties
    app.setApplicationName("Python Calculator")
    app.setApplicationVersion("1.0")
    app.setOrganizationName("Calculator App")
    
    # Create and show calculator window
    calculator = CalculatorUI()
    calculator.show()
    
    # Start event loop
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
