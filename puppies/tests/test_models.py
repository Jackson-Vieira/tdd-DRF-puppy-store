from django.test import TestCase
from puppies.models import Puppy


class PuppyTest(TestCase):
    """ Test module for Puppy model """

    def setUp(self):
        self.puppy = Puppy(
            name='Casper', age=3, breed='Bull Dog', color='Black')

    def test_puppy_breed(self):
        result = "Casper belongs to Bull Dog breed"
        self.assertEqual(
            self.puppy.get_breed(), result)
