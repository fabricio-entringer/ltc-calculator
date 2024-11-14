from sympy import symbols, Eq, solve
from ultils import clear_console

clear_console();

# Load the variables A, B, C, D and X from user input
a = float(input("Inform the A value: "))
b = float(input("Inform the B value: "))
c = float(input("Inform the C value: "))
d = float(input("Inform the D value: "))
x_input = input("Inform the X (or ? to find the value that zeros the function): ")

# Define the symbol X to be discovered by the sympy library
x = symbols('x')

if x_input == '?':
    # Resolve the formula ax^3 - bx^2 - cx + d = 0
    equation = Eq(a * x**3 + b * x**2 + c * x + d, 0) 
    # The active selection `Eq` refers to a function from the `sympy` library in Python. `sympy` is a powerful symbolic mathematics library that allows 
    #       for algebraic manipulation and solving of mathematical expressions.
    # The `Eq` function is used to create an equation object. It takes two arguments, representing the left-hand side and the right-hand side of the equation, 
    #       respectively. For example, `Eq(a * x**3 - b * x**2 - c * x + d, 0)` creates an equation representing `a*x^3 - b*x^2 - c*x + d = 0`.
    # This equation object can then be used with other `sympy` functions, such as `solve`, to find the values of variables that satisfy the equation. 
    #       This is particularly useful for solving algebraic equations symbolically, rather than numerically, allowing for exact solutions where possible.
    
    solutions = solve(equation, x)
    # When using solve, you typically pass an equation or a system of equations as the first argument, 
    #       and the variable(s) for which you want to solve as the second argument. For example, solve(Eq(a * x**3 - b * x**2 - c * x + d, 0), x) would solve the cubic equation a*x^3 - b*x^2 - c*x + d = 0 for the variable x.
    # The function returns a list of solutions. If the equation has multiple solutions, all of them will be included in the list. 
    #       If there are no solutions, the list will be empty. This makes solve an essential function for algebraic manipulation and solving mathematical 
    #       problems symbolically in Python.

    print(f"The values of X that make f(x) = 0 are: {solutions}")
else:
    # Calculate the formula: f(x)
    x = float(x_input)
    f_x = a * x**3 - b * x**2 - c * x + d

    # Print the entire formula
    print(f"The fórmula is: f(x) = {a}*x^3 - {b}*x^2 - {c}*x + {d}")

    # Explain the calculation step by step
    print(f"Calculating step by step:")
    print(f"{a} * ({x}^3) = {a * x**3}")
    print(f"+ {b} * ({x}^2) = {-b * x**2}")
    print(f"+ {c} * {x} = {-c * x}")
    print(f"+ {d} = {d}")

    # Show the result of the calculation
    print(f"The value if f(x) is: {f_x}")

 