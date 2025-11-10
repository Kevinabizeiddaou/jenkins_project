import unittest
from app import greet

class TestApp(unittest.TestCase):
    def test_greet(self):
        # Must match the exact string in app.py (update your name in both places)
        self.assertEqual(
            greet("World"),
            "Hello, World from YourFirstName YourLastName!"
        )

if __name__ == "__main__":
    unittest.main()
