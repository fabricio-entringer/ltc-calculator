#!/usr/bin/env python
"""
Test runner for LTC Calculator tests.
Run this script to execute all unit tests.
"""

import unittest
import sys

def run_tests():
    """Discover and run all tests"""
    # Discover all tests in the current directory
    loader = unittest.TestLoader()
    suite = loader.discover('.')
    
    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Return exit code based on test results
    return 0 if result.wasSuccessful() else 1

if __name__ == '__main__':
    sys.exit(run_tests())
