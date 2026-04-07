import unittest

# Sample functions (your app logic)
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Test cases
class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_fail_case(self):
        self.assertNotEqual(add(2, 2), 5)  # intentional logic check


if __name__ == "__main__":
    unittest.main()
