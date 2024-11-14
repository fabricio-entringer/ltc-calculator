# Function to calculate the formula f(x)
def calculate_fx(a, b, c, d, x):
    return a * x**3 + b * x**2 + c * x + d

# Function to find the roots of a cubic equation using the Newton-Raphson method
def newton_raphson(a, b, c, d, x0, tol=1e-6, max_iter=1000):
    def f(x):
        return a * x**3 + b * x**2 + c * x + d
    
    def f_prime(x):
        return 3 * a * x**2 + 2 * b * x + c
    
    x = x0
    for _ in range(max_iter):
        fx = f(x)
        fpx = f_prime(x)
        if abs(fx) < tol:
            return x
        if fpx == 0:
            break
        x = x - fx / fpx
    return None

# Load the variables A, B, C, D and X from user input
a = float(input("Enter the value of A: "))
b = float(input("Enter the value of B: "))
c = float(input("Enter the value of C: "))
d = float(input("Enter the value of D: "))
x_input = input("Enter the value of X (or ? to find the value that zeros the function): ")

if x_input == '?':
    # Try to find a root of the cubic equation
    x0 = 0  # Initial point for the Newton-Raphson method
    root = newton_raphson(a, b, c, d, x0)
    if root is not None:
        print(f"The value of X that makes f(x) = 0 is: {root}")
    else:
        print("It was not possible to find a root.")
else:
    # Calculate the formula f(x)
    x = float(x_input)
    f_x = calculate_fx(a, b, c, d, x)

    # Display the complete formula
    print(f"The formula is: f(x) = {a}*x^3 - {b}*x^2 - {c}*x + {d}")

    # Explain the calculation step by step
    print("Calculating step by step:")
    print(f"{a} * ({x}^3) = {a * x**3}")
    print(f"+ {b} * ({x}^2) = {-b * x**2}")
    print(f"+ {c} * {x} = {-c * x}")
    print(f"+ {d} = {d}")

    # Show the result of the calculation
    print(f"The value of f(x) is: {f_x}")