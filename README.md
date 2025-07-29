# Python Calculator with PySide6

A modern calculator application built with Python and PySide6, featuring a unique "calculator tape" experience where expressions build up visually until you press equals. The interface enforces a consistent light theme and provides full keyboard support with persistent calculation history.

## Features

- **Expression Building**: See your complete calculation as you type (e.g., `12 + 7 - 3`) before getting the result
- **Calculator Tape Experience**: Screen only clears when you press equals, mimicking traditional desktop calculators
- **Basic Arithmetic**: Addition (+), subtraction (-), multiplication (×), division (÷) with proper operator chaining
- **Full Keyboard Support**: All calculator functions mapped to intuitive keyboard shortcuts
- **Persistent History**: Calculation history with timestamps, automatically saved between sessions
- **Forced Light Theme**: Consistent light interface regardless of system dark mode settings
- **Error Handling**: Graceful handling of division by zero and invalid expressions
- **Cross-Platform**: Works seamlessly on Windows, macOS, and Linux


## Installation \& Setup

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)


### Installation Steps

1. Navigate to the project directory:

```
cd python_calculator
```

2. Install required dependencies:

```
pip install -r requirements.txt
```

3. Launch the calculator:

```
python main.py
```


## User Interface

### Calculator Behavior

- **Number Input**: Numbers accumulate in the display as you type
- **Operator Input**: Operators are added to the expression (e.g., `12 +` then `7` shows `12 + 7`)
- **Expression Building**: Complete expressions build up visually: `12 + 7 - 3 × 2`
- **Equals Function**: Only when you press `=` does the screen clear to show just the result
- **History Panel**: Shows your last 10 calculations with timestamps


### Keyboard Shortcuts

- **Numbers**: 0-9 keys for digit input
- **Basic Operations**:
    - `+` for addition
    - `-` for subtraction
    - `*` for multiplication (displays as ×)
    - `/` for division (displays as ÷)
- **Special Functions**:
    - `.` (period) for decimal point
    - `Enter` or `Return` to calculate (equals)
    - `Escape` to clear all
    - `Backspace` to delete last character
- **Additional**: All buttons are also clickable with mouse


## Project Structure

```
python_calculator/
├── main.py                 # Application entry point and launch script
├── calculator_ui.py        # User interface components and event handling
├── calculator_logic.py     # Core mathematical operations and validation
├── history_manager.py      # Calculation history persistence and management  
├── styles.py              # PySide6 stylesheet definitions for light theme
├── requirements.txt       # Python package dependencies
├── README.md             # Project documentation (this file)
├── .gitignore           # Git version control ignore rules
├── assets/              # Directory for images or additional resources
├── tests/               # Directory for unit tests (if implemented)
└── history.json         # User calculation history (auto-generated)
```


## Architecture \& Development

### Code Organization

- **Modular Design**: Clear separation between UI, calculation logic, and data persistence
- **Event-Driven**: Uses PySide6's signal-slot system for responsive user interactions
- **Theme Management**: Centralized styling system ensures consistent appearance across all components
- **Data Persistence**: History automatically saves to JSON file with error handling


### Key Implementation Details

- **Expression Building Logic**: Numbers and operators accumulate in display until equals is pressed
- **Smart Input Handling**: Proper spacing and validation for complex expressions
- **Operator Conversion**: Internal operators (* /) convert to display symbols (× ÷) for user clarity
- **History Limitation**: Keeps last 100 calculations to prevent excessive memory usage


## Extending the Calculator

### Adding New Features

- **UI Modifications**: Edit `calculator_ui.py` for interface changes
- **Mathematical Functions**: Extend `calculator_logic.py` for new operations
- **Styling Updates**: Modify `styles.py` for appearance customization
- **History Features**: Enhance `history_manager.py` for advanced history functions


### Testing Recommendations

Test edge cases including:

- Division by zero scenarios
- Very large number calculations
- Complex chained operations
- Decimal precision handling
- Invalid expression inputs


## Troubleshooting

### Common Issues

- **Import Errors**: Ensure PySide6 is properly installed with `pip install PySide6`
- **Display Issues**: Restart application if light theme doesn't apply correctly
- **History Problems**: Check file permissions in project directory for history.json access
- **Keyboard Shortcuts**: Ensure calculator window has focus for keyboard input


### Platform Notes

- **Windows**: May require Visual C++ redistributables for PySide6
- **macOS**: Compatible with both Intel and Apple Silicon processors
- **Linux**: Requires Qt6 development libraries installed


## License

This project is open source and available under the MIT License.

Experience the classic calculator tape feel with modern Python technology! 🧮


