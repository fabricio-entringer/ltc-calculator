from sympy import symbols, Eq, solve
from utils import clear_console, format_number, polynomial_to_string, validate_input, float_validator

def solve_equation_sympy(a, b, c, d):
    """
    Solve the cubic equation ax^3 + bx^2 + cx + d = 0 using sympy
    
    Args:
        a (float): Coefficient of x^3
        b (float): Coefficient of x^2
        c (float): Coefficient of x
        d (float): Constant term
    
    Returns:
        list: List of solutions
    """
    # Define the symbol X to be discovered by the sympy library
    x = symbols('x')
    
    # Create the equation ax^3 + bx^2 + cx + d = 0
    equation = Eq(a * x**3 + b * x**2 + c * x + d, 0)
    
    # Solve the equation
    solutions = solve(equation, x)
    return solutions

def calculate_value(a, b, c, d, x):
    """
    Calculate and display the polynomial value at a given point
    
    Args:
        a (float): Coefficient of x^3
        b (float): Coefficient of x^2
        c (float): Coefficient of x
        d (float): Constant term
        x (float): The x value
        
    Returns:
        float: The calculated value
    """
    # Calculate the formula: f(x)
    f_x = a * x**3 + b * x**2 + c * x + d

    # Print the entire formula
    print(f"The formula is: f(x) = {format_number(a)}x^3 + {format_number(b)}x^2 + {format_number(c)}x + {format_number(d)}")

    # Explain the calculation step by step
    print(f"Calculating step by step:")
    print(f"{format_number(a)} * ({format_number(x)}^3) = {format_number(a * x**3)}")
    print(f"+ {format_number(b)} * ({format_number(x)}^2) = {format_number(b * x**2)}")
    print(f"+ {format_number(c)} * {format_number(x)} = {format_number(c * x)}")
    print(f"+ {format_number(d)} = {format_number(d)}")

    # Show the result of the calculation
    print(f"The value of f(x) is: {format_number(f_x)}")
    
    return f_x

def main():
    """
    Main function to run the polynomial calculator with sympy
    """
    clear_console()
    
    print("Symbolic Cubic Polynomial Calculator")
    print("===================================")
    print("This program calculates f(x) = ax^3 + bx^2 + cx + d")
    print("or finds exact symbolic solutions to f(x) = 0")
    print()

    # Load the variables A, B, C, D and X from user input
    a = float(validate_input("Inform the A value: ", float_validator, "Please enter a valid number"))
    b = float(validate_input("Inform the B value: ", float_validator, "Please enter a valid number"))
    c = float(validate_input("Inform the C value: ", float_validator, "Please enter a valid number"))
    d = float(validate_input("Inform the D value: ", float_validator, "Please enter a valid number"))
    
    # Display the formula in standard form
    coeffs = [a, b, c, d]
    print(f"Your polynomial: f(x) = {polynomial_to_string(coeffs)}")
    
    x_input = validate_input("Inform the X (or ? to find the value that zeros the function): ",
                             lambda x: x == '?' or float_validator(x),
                             "Please enter a number or ? for root finding")

    if x_input == '?':
        # Solve the equation symbolically
        solutions = solve_equation_sympy(a, b, c, d)
        
        if solutions:
            print(f"The values of X that make f(x) = 0 are:")
            for i, sol in enumerate(solutions, 1):
                print(f"  x{i} = {sol}")
                
            # If solutions are numerical, verify them
            try:
                print("\nVerification:")
                for i, sol in enumerate(solutions, 1):
                    sol_float = float(sol)
                    f_x = a * sol_float**3 + b * sol_float**2 + c * sol_float + d
                    print(f"  f(x{i}) = f({format_number(sol_float)}) = {format_number(f_x)}")
            except:
                # If some solutions are complex or symbolic expressions, skip verification
                print("\nSome solutions are complex or symbolic expressions.")
        else:
            print("No solutions found for the equation.")
    else:
        # Calculate f(x) for the provided x value
        x = float(x_input)
        calculate_value(a, b, c, d, x)

if __name__ == "__main__":
    main()

