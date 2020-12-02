import unittest
import script

class TestScript(unittest.TestCase):
    def run(self, result=None):
        if not result.errors:
            super(TestScript, self).run(result)
        else:
            print("ERROORRRRR")


    def test_script(self):
        self.assertEqual(script.foo(2,3), 5)


if __name__ == '__main__':
    unittest.main()
