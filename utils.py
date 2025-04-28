import os
import platform
import sys
import math

def clear_console():
    """
    Clear the console screen based on the operating system.
    """
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def format_number(number, decimal_places=4):
    """
    Format a number to a specific number of decimal places.
    Removes trailing zeros and decimal point when possible.
    
    Args:
        number (float): The number to format
        decimal_places (int): Number of decimal places to display
        
    Returns:
        str: Formatted number string
    """
    if number is None:
        return "None"
    
    # Check if number is very close to an integer
    if abs(number - round(number)) < 1e-10:
        return str(int(round(number)))
        
    # Format the number with specified decimal places
    formatted = f"{number:.{decimal_places}f}"
    
    # Remove trailing zeros and decimal point if possible
    formatted = formatted.rstrip('0').rstrip('.') if '.' in formatted else formatted
    
    return formatted

def is_near_zero(value, tolerance=1e-10):
    """
    Check if a value is very close to zero.
    
    Args:
        value (float): The value to check
        tolerance (float): Tolerance threshold
        
    Returns:
        bool: True if value is within tolerance of zero
    """
    return abs(value) < tolerance

def polynomial_to_string(coeffs, var_name='x'):
    """
    Convert a list of polynomial coefficients to a readable string.
    
    Args:
        coeffs (list): List of coefficients [a, b, c, d]
                      representing ax^3 + bx^2 + cx + d
        var_name (str): Variable name to use (default: 'x')
        
    Returns:
        str: String representation of the polynomial
    """
    if not coeffs:
        return "0"
    
    terms = []
    degree = len(coeffs) - 1
    
    for i, coeff in enumerate(coeffs):
        if is_near_zero(coeff):
            continue
            
        power = degree - i
        term = ""
        
        # Format the coefficient
        if abs(coeff) == 1 and power > 0:
            term = "-" if coeff < 0 else ""
        else:
            term = format_number(coeff)
            
        # Add variable with power
        if power > 1:
            term += f"{var_name}^{power}"
        elif power == 1:
            term += var_name
            
        terms.append(term)
    
    if not terms:
        return "0"
        
    # Join terms with plus signs
    result = terms[0]
    for term in terms[1:]:
        if term.startswith("-"):
            result += f" {term}"
        else:
            result += f" + {term}"
            
    return result

def validate_input(prompt, validator=None, error_msg=None):
    """
    Prompt the user for input with validation.
    
    Args:
        prompt (str): The prompt message
        validator (function): A function that returns True if input is valid
        error_msg (str): Message to display if validation fails
        
    Returns:
        str: Validated user input
    """
    while True:
        user_input = input(prompt)
        
        if validator is None or validator(user_input):
            return user_input
        
        print(error_msg or "Invalid input. Please try again.")

def float_validator(value):
    """
    Validate if a string can be converted to a float.
    
    Args:
        value (str): String to validate
        
    Returns:
        bool: True if the string can be converted to a float
    """
    try:
        float(value)
        return True
    except ValueError:
        return False