import unittest
from polynomial import calculate_fx, newton_raphson

class TestPolynomial(unittest.TestCase):
    """Tests for the polynomial functions in polynomial.py"""
    
    def test_calculate_fx(self):
        """Test that calculate_fx returns the correct result"""
        # Test case 1: Simple values
        self.assertEqual(calculate_fx(1, 0, 0, 0, 2), 8)  # 1*2^3 + 0*2^2 + 0*2 + 0 = 8
        
        # Test case 2: All coefficients are non-zero
        self.assertEqual(calculate_fx(2, 3, 4, 5, 1), 14)  # 2*1^3 + 3*1^2 + 4*1 + 5 = 14
        
        # Test case 3: Negative coefficients
        self.assertEqual(calculate_fx(-1, 2, -3, 4, 2), -2)  # -1*2^3 + 2*2^2 + -3*2 + 4 = -8 + 8 - 6 + 4 = -2
        
        # Test case 4: Negative x value
        self.assertEqual(calculate_fx(1, 1, 1, 1, -1), 0)  # 1*(-1)^3 + 1*(-1)^2 + 1*(-1) + 1 = -1 + 1 - 1 + 1 = 0
        
        # Test case 5: Zero coefficients and x
        self.assertEqual(calculate_fx(0, 0, 0, 5, 0), 5)  # Just the constant term

    def test_newton_raphson(self):
        """Test that newton_raphson correctly finds roots"""
        # Test case 1: Simple cubic with known root at x=1
        # (x-1)^3 = x^3 - 3x^2 + 3x - 1
        root = newton_raphson(1, -3, 3, -1, 0.5)
        if root is not None:
            # Check if f(root) is very close to zero
            fx = calculate_fx(1, -3, 3, -1, root)
            self.assertLess(abs(fx), 1e-5, f"f({root}) = {fx} is not close enough to zero")
        else:
            self.fail("newton_raphson did not find a root")
        
        # Test case 2: Cubic with known root at x=2
        # (x-2)^3 = x^3 - 6x^2 + 12x - 8
        root = newton_raphson(1, -6, 12, -8, 1.5)
        if root is not None:
            # Check if f(root) is very close to zero
            fx = calculate_fx(1, -6, 12, -8, root)
            self.assertLess(abs(fx), 1e-5, f"f({root}) = {fx} is not close enough to zero")
        else:
            self.fail("newton_raphson did not find a root")
        
        # Test case 3: Cubic with no real roots at specified starting point
        # For x^3 + x + 1, newton_raphson with x0=0 may not converge
        root = newton_raphson(1, 0, 1, 1, 0, max_iter=10)
        # We'll accept either None or a value that makes f(x) very close to 0
        if root is not None:
            fx = calculate_fx(1, 0, 1, 1, root)
            self.assertLess(abs(fx), 1e-4)  # If a root is found, it should be valid
        
        # Test case 4: Zero derivative
        # If fpx becomes 0, the function should exit and return None
        # Using a case where derivative becomes 0
        root = newton_raphson(0, 0, 0, 1, 0)  # f(x) = 1, f'(x) = 0
        self.assertIsNone(root)
        
        # Test case 5: Tolerance test
        # Create a function where the root is very near zero but not exactly
        root = newton_raphson(1, 0, 0, 1e-10, 0, tol=1e-9)
        if root is not None:  # If a root is found
            fx = calculate_fx(1, 0, 0, 1e-10, root)
            self.assertLess(abs(fx), 1e-8)  # Should be very close to zero

if __name__ == '__main__':
    unittest.main()
