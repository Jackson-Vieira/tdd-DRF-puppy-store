from rest_framework.test import APITestCase
from rest_framework import status
from puppies.models import Puppy
from puppies.serializers import PuppySerializer

from django.urls import reverse

from django.contrib.auth.models import User


class GetAllPuppiesTest(APITestCase):
    def setUp(self):
        Puppy.objects.create(
            name='Casper', age=3, breed='Bull Dog', color='Black')
        Puppy.objects.create(
            name='Muffin', age=1, breed='Gradane', color='Brown')
        Puppy.objects.create(
            name='Rambo', age=2, breed='Labrador', color='Black')
        Puppy.objects.create(
            name='Ricky', age=6, breed='Labrador', color='Brown')

    def test_get_all_puppies(self):
        response = self.client.get(reverse('get_post_puppies'))
        puppies = Puppy.objects.all()
        serializer = PuppySerializer(puppies, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)


class PostPuppyTest(APITestCase):
    def setUp(self):
        User.objects.create_superuser(
            username="admin",
            password="admin"
        )
        self.valid_data = {
            "name": "Casper",
            "age": 3,
            "breed": "Bull Dog",
            "color":  "Black"
        }
        self.invalid_data = {
            "name": "Casper",
            "age": -2,
            "breed": "Bull Dog",
            "color":  ""
        }

    def _authenticate(self):
        self.client.login(
            username="admin",
            password="admin"
        )

    def test_create_puppy_unauthenticated(self):
        response = self.client.post(
            reverse("get_post_puppies"), self.valid_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_puppy_with_valid_data(self):
        self._authenticate()
        response = self.client.post(
            reverse("get_post_puppies"), self.valid_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.client.logout()

    def test_create_puppy_with_invalid_data(self):
        self._authenticate()
        response = self.client.post(
            reverse("get_post_puppies"), self.invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.client.logout()
