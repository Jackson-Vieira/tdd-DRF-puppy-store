from rest_framework.serializers import ModelSerializer
from puppies.models import Puppy

from django.test import TestCase


class PuppySerializer(ModelSerializer):
    class Meta:
        model = Puppy
        fields = [
            'name', 'age', 'breed', 'color', 'created_at', 'updated_at'
        ]


class PuppySerializerTest(TestCase):
    def setUp(self):
        self.puppy = Puppy(
            name="Casper",
            age=4,
            breed="Bull Dog",
            color="Black"
        )

        self.serializer = PuppySerializer(self.puppy)

    def test_serializer_fields(self):
        result = set(['name', 'age', 'breed', 'color',
                     'created_at', 'updated_at'])
        self.assertEqual(result, set(self.serializer.data.keys()))