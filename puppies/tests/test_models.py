from django.test import TestCase
from puppies.models import Puppy


class PuppyModelTest(TestCase):
    def setUp(self) -> None:
        self.puppy = Puppy(
            name="Casper",
            age=4,
            breed="Bull Dog",
            color="Black"
        )

    def test_puppy_breed(self):
        result = 'Casper belongs to Bull Dog breed'
        self.assertEqual(self.puppy.get_breed(), result)

    def test_str(self):
        self.assertEqual(str(self.puppy), 'Casper')
