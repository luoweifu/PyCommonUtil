import unittest

# from ParseArgument import getValue
import ParseArgument

# code from module you're testing


class SimpleTestCase(unittest.TestCase):
    def setUp(self):
        """Call before every test case."""
        print("Call before every test case.")


def tearDown(self):
    """Call after every test case."""
    print("Call after every test case.")


def testGetValue(self):
        args = ParseArgument.getArgumentsFromString("D:\Workspace\compile.py -e master  -r teacher -v 1.2.0.0", ' ')
        value = ParseArgument.getValueFromArgument('-r', args)
        print("value:" + value)
        self.assertEqual(value, 'student', 'Result Fail')


# class OtherTestCase(unittest.TestCase):
#     def setUp(self):
#         blah_blah_blah()
#
#     def tearDown(self):
#         blah_blah_blah()
#
#     def testBlah(self):
#         assert self.blahblah == "blah", "blah isn't blahing blahing correctly"


if __name__ == "__main__":
    unittest.main()  # run all tests