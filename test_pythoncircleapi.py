# test_pythoncircleapi.py
import unittest
from pythoncircleapi.square import calculate_square_area
from pythoncircleapi.circle import calculate_circle_area

class TestPythonCircleAPI(unittest.TestCase):
    def test_square_area(self):
        self.assertEqual(calculate_square_area(2), 4)

    def test_circle_area(self):
        self.assertAlmostEqual(calculate_circle_area(3), 28.27, places=2)

if __name__ == '__main__':
    unittest.main()
