from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


NEWSPAPER_LIST_URL = reverse("manage_app:newspapers")


class PublicNewspaperTest(TestCase):
    def test_login_required(self):
        response = self.client.get(NEWSPAPER_LIST_URL)
        self.assertEqual(response.status_code, 302)


class PrivateNewspaperTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.redactor = get_user_model().objects.create_user(
            username="testuser",
            password="nqpknpks113",
        )
        self.client.force_login(self.redactor)

    def test_authorised_user_can_access(self):
        response = self.client.get(NEWSPAPER_LIST_URL)
        self.assertEqual(response.status_code, 200)
