"""
If this application had more than declarative components - that is, it
actually had logic to be tested - then unittests would go here.  Since it only
leverages other components (which, presumably, have their own unit tests),
there is little here that could be reasonably tested.
"""

from django.test import TestCase

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
