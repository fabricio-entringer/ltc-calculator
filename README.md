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
- `first.py`: Main script that demonstrates the usage of LTC formulas with practical examples
- `TIPoly.py`: Contains sophisticated polynomial models and algorithms for LTC calculations optimized for TI calculators, including curve-fitting functions
- `ultils.py`: Comprehensive utility functions to support the calculator operations, data validation, and formula implementations
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
4. Transfer all the Python files (`first.py`, `TIPoly.py`, `ultils.py`) to your calculator
5. Disconnect your calculator and open the Python app (press [prgm] and select Python)
6. Select the `first.py` program to run the main interface

## Usage
The formulas can be accessed through the Python app on your TI-84 Calculator. The `first.py` file provides a user-friendly interface to access all implemented formulas.

### Key Features
- Formula selection menu
- Input validation to prevent calculation errors
- Clear display of results
- Option to save results for later use
- Compatible with TI-84 graphing capabilities

### Example
```python
# Example calculation using the LTC polynomial functions
from TIPoly import calc_polynomial
from ultils import format_result

# Define polynomial coefficients
coeffs = [3.5, 2.1, -0.5, 0.02]  # Example coefficients
x_value = 2.5                    # Input value

# Calculate polynomial result
result = calc_polynomial(coeffs, x_value)

# Display formatted result
print(format_result(result, 4))  # Shows result with 4 decimal places