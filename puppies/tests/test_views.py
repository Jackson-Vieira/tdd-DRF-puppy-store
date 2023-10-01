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


class GetSinglePuppyTest(APITestCase):
    def setUp(self):
        Puppy.objects.create(
            name='Casper', age=3, breed='Bull Dog', color='Black')

    def test_get_puppy_detail(self):
        puppy = Puppy.objects.get(id=1)
        response = self.client.get(
            reverse("get_delete_update_puppy", kwargs={"pk": 1}))
        serializer = PuppySerializer(instance=puppy)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_puppy(self):
        data = {
            "name": "Casper",
            "age": 3,
            "breed": "Bull Dog",
            "color":  "Black"
        }
        response = self.client.put(
            reverse("get_delete_update_puppy", kwargs={"pk": 1}), data
        )
        puppy = Puppy.objects.get(id=1)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data["name"], puppy.name)
        self.assertEqual(response.data["age"], puppy.age)
        self.assertEqual(response.data["breed"], puppy.breed)
        self.assertEqual(response.data["color"], puppy.color)
    
    def test_update_puppy_with_invalid(self):
        data = {
            "name": "Casper",
            "age": -2,
            "breed": "Bull Dog",
            "color":  "Black"
        }
        response = self.client.put(
            reverse("get_delete_update_puppy", kwargs={"pk": 1}), data=data
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_puppy(self):
        response = self.client.delete(
            reverse("get_delete_update_puppy",  kwargs={"pk": 1}))
        count_pupppies = Puppy.objects.count()
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(count_pupppies, 0)
