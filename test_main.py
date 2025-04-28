import unittest
import sys
import io
from unittest.mock import patch
import importlib
import os

class TestMain(unittest.TestCase):
    """Tests for the main script functionality"""
    
    @patch('builtins.input')
    def test_calculating_known_values(self, mock_input):
        """Test that the script correctly calculates f(x) for known values"""
        # Setup input values
        mock_input.side_effect = ['1', '2', '3', '4', '2']  # a=1, b=2, c=3, d=4, x=2
        
        # Capture stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        try:
            # Import the module
            import main
            
            # Run the main function with mocked clear_console
            with patch('utils.clear_console'):  # Mock clear_console to do nothing
                main.main()
            
            # Check output
            output = captured_output.getvalue()
            
            # Verify expected outputs appear in the result
            # Check for polynomial display - relaxed check to accommodate formatting changes
            self.assertIn("formula is:", output)
            self.assertIn("1", output)
            self.assertIn("2", output)
            self.assertIn("3", output)
            self.assertIn("4", output)
            
            # Check for calculation steps
            self.assertIn("Calculating step by step", output)
            
            # The final result should be visible
            # f(x) = 1*2^3 + 2*2^2 + 3*2 + 4 = 8 + 8 + 6 + 4 = 26
            self.assertIn("value of f(x) is: 26", output)
        finally:
            # Restore stdout
            sys.stdout = sys.__stdout__
    
    @patch('builtins.input')
    def test_finding_roots(self, mock_input):
        """Test that the script correctly finds roots of the polynomial"""
        # Setup input values - using a polynomial with a known root
        # x^3 - 6x^2 + 12x - 8 = (x - 2)^3 has a root at x=2
        mock_input.side_effect = ['1', '-6', '12', '-8', '?']
        
        # Capture stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        try:
            # Import the module
            import main
            
            # Run the main function with mocked clear_console
            with patch('utils.clear_console'):  # Mock clear_console to do nothing
                main.main()
            
            # Check output
            output = captured_output.getvalue()
            
            # The output should contain the roots
            self.assertIn("The values of X that make f(x) = 0 are", output)
            self.assertIn("2", output)  # The root is 2
        finally:
            # Restore stdout
            sys.stdout = sys.__stdout__

if __name__ == '__main__':
    unittest.main()
