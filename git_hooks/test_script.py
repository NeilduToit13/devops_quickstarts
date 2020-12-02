import unittest
import script

class TestScript(unittest.TestCase):
    def test_script(self):
        self.assertEqual(script.foo(2,3), 5)


if __name__ == '__main__':
    unittest.main()
