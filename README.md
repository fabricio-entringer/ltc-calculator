# LTC Calculator for TI-84 Calculator Python Edition

## Overview
This repository contains a comprehensive collection of Lifetime Control (LTC) formulas implemented in Python specifically designed for use with the TI-84 Calculator Python Edition. These formulas provide powerful functionality for performing complex LTC calculations directly on your graphing calculator, saving time and enhancing precision in engineering, statistical, and mathematical applications.

## Why Use This Calculator?
- **Specialized for TI-84**: Optimized specifically for the computational capabilities of the TI-84 Calculator Python Edition
- **Accurate Calculations**: Implements industry-standard LTC formulas with high precision
- **Time-saving**: Eliminates the need for manual calculations of complex formulas
- **Educational Value**: Helps students understand LTC principles through practical application
- **Portable Solution**: Carry sophisticated calculation power wherever you go

## Files and Structure
- `main.py`: Main script that demonstrates the usage of LTC formulas with practical examples
- `polynomial.py`: Contains sophisticated polynomial models and algorithms for LTC calculations optimized for TI calculators, including curve-fitting functions
- `utils.py`: Comprehensive utility functions to support the calculator operations, data validation, and formula implementations
- `test_main.py`, `test_polynomial.py`, `test_utils.py`: Unit tests for verifying correctness of the implementation
- `run_tests.py`: Script to run all tests at once
- `LICENSE`: License information for this project with usage terms
- `README.md`: This detailed documentation file

## Technical Specifications
- **Python Version**: Compatible with TI-84 Python implementation (based on Python 3.x)
- **Memory Requirements**: Optimized for the memory constraints of the TI-84 Calculator
- **Calculation Speed**: Efficient algorithms designed for calculator processing capabilities
- **Mathematical Methods**: Implements numerical methods appropriate for calculator execution

## Installation
To use these formulas on your TI-84 Calculator Python Edition:

1. Connect your TI-84 Calculator to your computer using the USB cable
2. Install the TI Connect™ CE software if you haven't already (available from the [Texas Instruments website](https://education.ti.com/en/products/computer-software/ti-connect-ce-sw))
3. Open TI Connect™ CE and select "Calculator Explorer"
4. Transfer all the Python files (`main.py`, `polynomial.py`, `utils.py`) to your calculator
5. Disconnect your calculator and open the Python app (press [prgm] and select Python)
6. Select the `main.py` program to run the main interface

## Usage
The formulas can be accessed through the Python app on your TI-84 Calculator. The `main.py` file provides a user-friendly interface to access all implemented formulas.

### Key Features
- Formula selection menu
- Input validation to prevent calculation errors
- Clear display of results
- Option to save results for later use
- Compatible with TI-84 graphing capabilities

## Testing
The code includes a comprehensive test suite to ensure reliable operation. To run the tests:

### Prerequisites
- Python 3.x installed on your computer
- `sympy` library installed (run `pip install sympy` if not already installed)

### Running All Tests
You can run all tests at once using the provided test runner script:

```bash
# Method 1: Using the executable script
./run_tests.py

# Method 2: Using Python directly
python run_tests.py
```

### Running Individual Tests
You can also run tests for specific modules:

```bash
# Test the polynomial functions
python -m unittest test_polynomial.py

# Test the utility functions
python -m unittest test_utils.py

# Test the main script
python -m unittest test_main.py
```

### Test Coverage
The test suite covers:
- Core polynomial calculations
- Root-finding algorithms
- Utility functions
- Script operation with various inputs

## Example
```python
# Example calculation using the LTC polynomial functions
from polynomial import calculate_fx
from utils import clear_console

# Define polynomial coefficients
a = 3.5    # Coefficient of x^3
b = 2.1    # Coefficient of x^2
c = -0.5   # Coefficient of x
d = 0.02   # Constant term
x_value = 2.5

# Calculate polynomial result
result = calculate_fx(a, b, c, d, x_value)

# Display result
print(f"f({x_value}) = {result:.4f}")
```