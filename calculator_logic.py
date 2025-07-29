"""
Calculator Logic Module
Handles all mathematical operations and calculations
"""

import re
from decimal import Decimal, InvalidOperation, getcontext

# Set precision for decimal calculations
getcontext().prec = 15

class CalculatorLogic:
    """Core calculator logic and operations"""
    
    def __init__(self):
        self.current_expression = ""
        self.result = 0
        self.last_result = 0
    
    def add(self, a, b):
        """Addition operation"""
        try:
            return float(Decimal(str(a)) + Decimal(str(b)))
        except (InvalidOperation, ValueError):
            raise ValueError("Invalid numbers for addition")
    
    def subtract(self, a, b):
        """Subtraction operation"""
        try:
            return float(Decimal(str(a)) - Decimal(str(b)))
        except (InvalidOperation, ValueError):
            raise ValueError("Invalid numbers for subtraction")
    
    def multiply(self, a, b):
        """Multiplication operation"""
        try:
            return float(Decimal(str(a)) * Decimal(str(b)))
        except (InvalidOperation, ValueError):
            raise ValueError("Invalid numbers for multiplication")
    
    def divide(self, a, b):
        """Division operation with zero check"""
        try:
            if float(b) == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return float(Decimal(str(a)) / Decimal(str(b)))
        except (InvalidOperation, ValueError):
            raise ValueError("Invalid numbers for division")
    
    def calculate(self, expression):
        """Evaluate mathematical expression safely"""
        if not expression or not expression.strip():
            return 0
        
        # Clean the expression
        expression = expression.replace(' ', '')
        
        # Validate expression contains only allowed characters
        if not re.match(r'^[0-9+\-*/().]+$', expression):
            raise ValueError("Invalid characters in expression")
        
        # Check for balanced parentheses
        if expression.count('(') != expression.count(')'):
            raise ValueError("Unbalanced parentheses")
        
        try:
            # Safely evaluate the expression
            # Using eval here is generally not recommended, but with proper validation it's acceptable
            # In production, consider using a proper expression parser
            result = eval(expression)
            
            # Handle division by zero and other math errors
            if not isinstance(result, (int, float)) or str(result) in ['inf', '-inf', 'nan']:
                raise ValueError("Invalid calculation result")
            
            # Round to avoid floating point precision issues
            if isinstance(result, float):
                result = round(result, 10)
            
            self.last_result = result
            return result
            
        except ZeroDivisionError:
            raise ZeroDivisionError("Cannot divide by zero")
        except (ValueError, TypeError, SyntaxError):
            raise ValueError("Invalid expression")
        except Exception:
            raise ValueError("Calculation error")
    
    def clear(self):
        """Clear current calculation"""
        self.current_expression = ""
        self.result = 0
    
    def clear_entry(self):
        """Clear last entry only"""
        # This would be implemented based on UI needs
        pass
    
    def validate_number(self, num_str):
        """Validate if string represents a valid number"""
        try:
            float(num_str)
            return True
        except ValueError:
            return False
