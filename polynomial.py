from utils import format_number, is_near_zero, polynomial_to_string, validate_input, float_validator

# Function to calculate the formula f(x)
def calculate_fx(a, b, c, d, x):
    """
    Calculate the value of a cubic polynomial: a*x^3 + b*x^2 + c*x + d
    
    Args:
        a (float): Coefficient of x^3
        b (float): Coefficient of x^2
        c (float): Coefficient of x
        d (float): Constant term
        x (float): Input value
        
    Returns:
        float: Result of the polynomial evaluation
    """
    return a * x**3 + b * x**2 + c * x + d

# Function to find the roots of a cubic equation using the Newton-Raphson method
def newton_raphson(a, b, c, d, x0, tol=1e-6, max_iter=1000):
    """
    Find a root of the cubic polynomial a*x^3 + b*x^2 + c*x + d using Newton-Raphson method
    
    Args:
        a (float): Coefficient of x^3
        b (float): Coefficient of x^2
        c (float): Coefficient of x
        d (float): Constant term
        x0 (float): Initial guess for the root
        tol (float): Tolerance for convergence
        max_iter (int): Maximum number of iterations
        
    Returns:
        float or None: Approximated root if found, None otherwise
    """
    def f(x):
        return a * x**3 + b * x**2 + c * x + d
    
    def f_prime(x):
        return 3 * a * x**2 + 2 * b * x + c
    
    x = x0
    for _ in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return x
        fpx = f_prime(x)
        if fpx == 0:
            break
        x = x - fx / fpx
    return None

def calculate_and_display_result(a, b, c, d, x):
    """
    Calculate and display the result of evaluating the polynomial
    
    Args:
        a (float): Coefficient of x^3
        b (float): Coefficient of x^2
        c (float): Coefficient of x
        d (float): Constant term
        x (float): Input value
        
    Returns:
        float: Result of the calculation
    """
    # Calculate the formula f(x)
    f_x = calculate_fx(a, b, c, d, x)
    
    # Display the complete formula
    print(f"The formula is: f(x) = {format_number(a)}x^3 + {format_number(b)}x^2 + {format_number(c)}x + {format_number(d)}")
    
    # Explain the calculation step by step
    print("**************************")
    print(f"{format_number(a)} * ({format_number(x)}^3) = {format_number(a * x**3)}")
    print(f"+ {format_number(b)} * ({format_number(x)}^2) = {format_number(b * x**2)}")
    print(f"+ {format_number(c)} * {format_number(x)} = {format_number(c * x)}")
    print(f"+ {format_number(d)} = {format_number(d)}")
    print(" ")
    
    # Show the result of the calculation
    print(f"The value of f(x) is: {format_number(f_x)}")
    
    return f_x

def find_root(a, b, c, d):
    """
    Find a root of the cubic polynomial
    
    Args:
        a (float): Coefficient of x^3
        b (float): Coefficient of x^2
        c (float): Coefficient of x
        d (float): Constant term
        
    Returns:
        float or None: Found root or None if not found
    """
    # Try to find a root of the cubic equation
    x0 = 0  # Initial point for the Newton-Raphson method
    root = newton_raphson(a, b, c, d, x0)
    
    if root is not None:
        print(f"The value of X that makes f(x) = 0 is: {format_number(root)}")
        
        # Verify the result
        fx_at_root = calculate_fx(a, b, c, d, root)
        print(f"Verification: f({format_number(root)}) = {format_number(fx_at_root)}")
    else:
        print("It was not possible to find a root with the starting point x=0.")
        print("Try again with a different starting value or use a different method.")
    
    return root

def main():
    """
    Main function to run the polynomial calculator
    """
    print("Cubic Polynomial Calculator")
    print("==========================")
    print("This program calculates f(x) = ax^3 + bx^2 + cx + d")
    print("or finds a value of x where f(x) = 0")
    print()
    
    # Load the variables A, B, C, D and X from user input with validation
    a = float(validate_input("Enter the value of A: ", float_validator, "Please enter a valid number"))
    b = float(validate_input("Enter the value of B: ", float_validator, "Please enter a valid number"))
    c = float(validate_input("Enter the value of C: ", float_validator, "Please enter a valid number"))
    d = float(validate_input("Enter the value of D: ", float_validator, "Please enter a valid number"))
    
    # Display the formula in standard form
    coeffs = [a, b, c, d]
    print(f"Your polynomial: f(x) = {polynomial_to_string(coeffs)}")
    
    x_input = validate_input("Enter the value of X (or ? to find the value that zeros): ", 
                            lambda x: x == '?' or float_validator(x),
                            "Please enter a number or ? for root finding")

    if x_input == '?':
        find_root(a, b, c, d)
    else:
        x = float(x_input)
        calculate_and_display_result(a, b, c, d, x)

if __name__ == "__main__":
    main()