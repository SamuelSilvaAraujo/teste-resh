from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse_lazy

from django.contrib.auth import get_user_model


User = get_user_model()


class RegisterTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.url = reverse_lazy("api:register")

        self.register_data = {
            "email": "usuario01@gmail.com",
            "first_name": "Fulano",
            "last_name": "da silva",
            "password": "Admin123-",
        }

    def test_register(self):
        request = self.client.post(self.url, self.register_data, format="json")

        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
        self.assertTrue(
            User.objects.filter(username=self.register_data["email"]).exists()
        )
        self.assertEqual(
            User.objects.filter(username=self.register_data["email"])
            .first()
            .first_name,
            self.register_data["first_name"],
        )
        self.assertEqual(
            User.objects.filter(username=self.register_data["email"]).first().last_name,
            self.register_data["last_name"],
        )


class LoginTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.url = reverse_lazy("api:login")

        self.register_data = {
            "email": "usuario01@gmail.com",
            "first_name": "Fulano",
            "last_name": "da silva",
            "password": "Admin123-",
        }

        User.objects.create_user(
            first_name=self.register_data["first_name"],
            last_name=self.register_data["last_name"],
            password=self.register_data["password"],
            email=self.register_data["email"],
            username=self.register_data["email"],
        )

        self.login_data = {
            "username": self.register_data["email"],
            "password": self.register_data["password"],
        }

    def test_login(self):
        request = self.client.post(self.url, self.login_data, format="json")

        self.assertEqual(request.status_code, status.HTTP_201_CREATED)


class ProfileTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.url = reverse_lazy("api:profile")

        self.register_data = {
            "email": "usuario01@gmail.com",
            "first_name": "Fulano",
            "last_name": "da silva",
            "password": "Admin123-",
        }

        self.user = User.objects.create_user(
            first_name=self.register_data["first_name"],
            last_name=self.register_data["last_name"],
            password=self.register_data["password"],
            email=self.register_data["email"],
            username=self.register_data["email"],
        )

    def test_profile(self):
        self.client.force_authenticate(self.user)

        request = self.client.get(self.url, format="json")

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(request.data["name"], self.user.get_full_name())
        self.assertEqual(request.data["email"], self.user.email)
    
    def test_delete(self):
        self.client.force_authenticate(self.user)

        request = self.client.delete(self.url, format="json")

        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(
            User.objects.filter(username=self.register_data["email"]).exists()
        )


class ChangePasswordTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.url = reverse_lazy("api:change_password")

        self.register_data = {
            "email": "usuario01@gmail.com",
            "first_name": "Fulano",
            "last_name": "da silva",
            "password": "Admin123-",
        }

        self.user = User.objects.create_user(
            first_name=self.register_data["first_name"],
            last_name=self.register_data["last_name"],
            password=self.register_data["password"],
            email=self.register_data["email"],
            username=self.register_data["email"],
        )

        self.change_password = {
            "password": self.register_data["password"],
            "new_password": "Test123-",
        }

    def test_change_password(self):
        self.client.force_authenticate(self.user)

        request = self.client.put(self.url, self.change_password, format="json")

        self.assertEqual(request.status_code, status.HTTP_200_OK)


class ChangeEmailTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.url = reverse_lazy("api:change_email")

        self.register_data = {
            "email": "usuario01@gmail.com",
            "first_name": "Fulano",
            "last_name": "da silva",
            "password": "Admin123-",
        }

        self.user = User.objects.create_user(
            first_name=self.register_data["first_name"],
            last_name=self.register_data["last_name"],
            password=self.register_data["password"],
            email=self.register_data["email"],
            username=self.register_data["email"],
        )

        self.change_email = {
            "email": "fulanodasilva@gmail.com",
        }

    def test_change_password(self):
        self.client.force_authenticate(self.user)

        request = self.client.put(self.url, self.change_email, format="json")

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(self.user.email, self.change_email['email'])
        self.assertEqual(self.user.username, self.change_email['email'])
