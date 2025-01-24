import unittest
from functools import wraps

def freeze_control(method):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        return method(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @freeze_control
    def test_run(self):
        self.assertEqual(1 + 1, 2)

    @freeze_control
    def test_walk(self):
        self.assertTrue(True)

    @freeze_control
    def test_challenge(self):
        self.assertIn(3, [1, 2, 3])

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @freeze_control
    def test_first_tournament(self):
        self.assertEqual("Hello".upper(), "HELLO")

    @freeze_control
    def test_second_tournament(self):
        self.assertGreater(10, 5)

    @freeze_control
    def test_third_tournament(self):
        self.assertIsNone(None)

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(RunnerTest))
    test_suite.addTest(unittest.makeSuite(TournamentTest))
    return test_suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
