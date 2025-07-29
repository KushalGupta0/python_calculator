"""
History Manager Module
Handles calculation history storage and retrieval
"""

import json
import os
from datetime import datetime
from typing import List, Dict

class HistoryManager:
    """Manages calculation history persistence"""
    
    def __init__(self):
        self.history_file = "history.json"
        self.calculations = self.load_history()
    
    def add_calculation(self, expression: str, result: str):
        """Add new calculation to history"""
        calculation = {
            "expression": expression,
            "result": result,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.calculations.append(calculation)
        
        # Keep only last 100 calculations to prevent file from growing too large
        if len(self.calculations) > 100:
            self.calculations = self.calculations[-100:]
        
        self.save_history()
    
    def get_history(self) -> List[Dict]:
        """Get all calculations from history"""
        return self.calculations
    
    def get_recent_history(self, count: int = 10) -> List[Dict]:
        """Get recent calculations from history"""
        return self.calculations[-count:] if self.calculations else []
    
    def clear_history(self):
        """Clear all calculation history"""
        self.calculations = []
        self.save_history()
    
    def load_history(self) -> List[Dict]:
        """Load history from JSON file"""
        if os.path.exists(self.history_file):
            try:
                with open(self.history_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    return data.get('calculations', [])
            except (json.JSONDecodeError, FileNotFoundError, UnicodeDecodeError):
                return []
        return []
    
    def save_history(self):
        """Save history to JSON file"""
        try:
            data = {"calculations": self.calculations}
            with open(self.history_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving history: {e}")
    
    def export_history(self, filename: str = None) -> bool:
        """Export history to a file"""
        if not filename:
            filename = f"calculator_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump({"calculations": self.calculations}, f, indent=2, ensure_ascii=False)
            return True
        except Exception:
            return False
    
    def search_history(self, search_term: str) -> List[Dict]:
        """Search calculations by expression or result"""
        if not search_term:
            return self.calculations
        
        search_term = search_term.lower()
        return [
            calc for calc in self.calculations
            if search_term in calc['expression'].lower() or search_term in calc['result'].lower()
        ]
