import unittest
from runner import Runner

class TestRunner(unittest.TestCase):
    def setUp(self):
        self.runner = Runner("Василий", 5)

    def test_run_positive_speed(self):
        self.runner.run()
        self.assertEqual(self.runner.distance_covered, 5)

    def test_run_zero_speed(self):
        self.runner.speed = 0
        self.runner.run()
        self.assertEqual(self.runner.distance_covered, 0)

    def test_negative_speed_raises_valueerror(self):
        with self.assertRaises(ValueError):
            Runner("Василий", -1)

    def test_non_string_name_raises_typeerror(self):
        with self.assertRaises(TypeError):
            Runner(123, 5)

if __name__ == '__main__':
    unittest.main()