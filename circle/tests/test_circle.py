
import unittest

from Circle import Circle

class CircleTestSuite(unittest.TestCase):
    """Test suite for the Circle exercise"""

    def test_init_radius(self):

        ccl = Circle()
        self.assertEqual(ccl.radius, 1)

        ccl = Circle(5)
        self.assertEqual(ccl.radius, 5)

    def test_diameter(self):

        ccl = Circle(9)
        self.assertEqual(ccl.diameter, 18)

    def test_area(self):

        ccl = Circle(5)
        self.assertEqual(ccl.area, 78.53981633974483)

    def test_repr(self):

        ccl = Circle(17)
        self.assertEqual(repr(ccl), 'Circle(17)')

    def test_reset(self):
        """Bonus question 1"""

        ccl = Circle(2)
        ccl.radius = 1

        self.assertEqual(ccl.diameter, 2)
        self.assertEqual(ccl.area, 3.141592653589793)
        self.assertEqual(repr(ccl), 'Circle(1)')
