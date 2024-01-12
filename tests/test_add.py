from package import add
import unittest


class TestPackge(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_throws(self):
        with self.assertRaises(AssertionError):
            self.assertEqual(add(1, 2), 4)
