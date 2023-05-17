from django.test import TestCase

# Create your tests here.
class TestDjango(TestCase):
    # (self) is TestDjango
    def test_this_thing_works(self):
        self.assertEqual(1, 1)
            