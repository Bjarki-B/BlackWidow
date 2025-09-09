import unittest
from scaling_relations_Curti2020 import line_ratios

class TestLineRatios(unittest.TestCase):
    def test_Z_zero(self):
        Z = 0
        results = line_ratios(Z)
        
        # 1. Check that the result is a dictionary
        self.assertIsInstance(results, dict)
        
        # 2. Check that all expected diagnostics are present
        expected_diagnostics = [
            "R2", "R3", "O3O2", "R23", "N2", "O3N2", "S2", "RS32", "O3S2"
        ]
        for diag in expected_diagnostics:
            self.assertIn(diag, results)
        
        # 3. Check that all values are floats
        for val in results.values():
            self.assertIsInstance(val, float)

if __name__ == "__main__":
    unittest.main()

