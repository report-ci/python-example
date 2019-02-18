import unittest
import xmlrunner

class SimpleTestCase(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""

    def tearDown(self):
        """Call after every test case."""

    def testA(self):
        """Test case A. note that all test method names must begin with 'test.'"""
        assert 0x21F == 543, "bar() not calculating values correctly"

    def testB(self):
        """test case B"""
        assert 23 + 12 == 35, "can't add Foo instances"

    def testC(self):
        """test case C"""
        assert "blah" == "blah", "baz() not returning blah correctly"



class OtherTestCase(unittest.TestCase):
    def setUp(self):
        self.blahblah  = "blah"

    def testBlah(self):
        assert self.blahblah == "blah", "blah isn't blahing blahing correctly"


if __name__ == "__main__":
    testRunner = xmlrunner.XMLTestRunner(output=".")
    simpleSuite = unittest.defaultTestLoader.loadTestsFromTestCase(SimpleTestCase)
    otherSuite  = unittest.defaultTestLoader.loadTestsFromTestCase(OtherTestCase)

    success = True
    success &= testRunner.run(simpleSuite).wasSuccessful()
    success &= testRunner.run(otherSuite).wasSuccessful()

    exit(0 if success else 1)