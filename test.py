__author__ = 'SolPie'
import unittest


class TagreatTest(unittest.TestCase):
    def setUp(self):
        from mainwin import main
        main()

    def test_add_dir(self):
        pass